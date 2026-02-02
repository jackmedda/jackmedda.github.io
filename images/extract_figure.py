#!/usr/bin/env python3
"""
Extract a specific Form XObject (vector figure) from a PDF as a standalone PDF.
This properly copies the XObject with all its resources.
"""

import pymupdf as fitz
import re
import os

def extract_form_xobject(src_doc, xref, output_path):
    """
    Extract a Form XObject as a standalone PDF file.
    
    This creates a new PDF where the page content directly uses
    the Form XObject's stream and resources.
    """
    # Get XObject dictionary
    xobj_dict = src_doc.xref_object(xref, compressed=False)
    
    # Check it's a Form XObject
    if '/Subtype /Form' not in xobj_dict and '/Subtype/Form' not in xobj_dict:
        raise ValueError(f"XRef {xref} is not a Form XObject")
    
    # Parse BBox
    bbox_match = re.search(r'/BBox\s*\[\s*([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s+([\d.-]+)\s*\]', xobj_dict)
    if not bbox_match:
        raise ValueError("Could not find BBox in XObject")
    
    x0, y0, x1, y1 = map(float, bbox_match.groups())
    width, height = x1 - x0, y1 - y0
    
    print(f"Figure size: {width:.2f} x {height:.2f} points")
    
    # Get the decompressed stream (the actual drawing commands)
    stream = src_doc.xref_stream(xref)
    print(f"Stream size: {len(stream)} bytes")
    
    # Parse Resources from the XObject
    # We need to extract the entire Resources dictionary
    res_start = xobj_dict.find('/Resources')
    if res_start == -1:
        resources_dict = "<< >>"
    else:
        # Find the matching closing >>
        depth = 0
        res_content_start = xobj_dict.find('<<', res_start)
        i = res_content_start
        while i < len(xobj_dict):
            if xobj_dict[i:i+2] == '<<':
                depth += 1
                i += 2
            elif xobj_dict[i:i+2] == '>>':
                depth -= 1
                i += 2
                if depth == 0:
                    break
            else:
                i += 1
        resources_dict = xobj_dict[res_content_start:i]
    
    print(f"Resources dict length: {len(resources_dict)} chars")
    
    # Now we need to copy all referenced objects
    # Find all xref references in resources
    refs = set(int(m) for m in re.findall(r'(\d+)\s+0\s+R', resources_dict))
    print(f"Direct resource references: {len(refs)}")
    
    # Recursively find all dependencies
    all_refs = set()
    def collect_refs(xrefs):
        for x in xrefs:
            if x in all_refs:
                continue
            all_refs.add(x)
            try:
                obj = src_doc.xref_object(x, compressed=False)
                sub_refs = set(int(m) for m in re.findall(r'(\d+)\s+0\s+R', obj))
                collect_refs(sub_refs)
            except:
                pass
    
    collect_refs(refs)
    print(f"Total dependencies: {len(all_refs)}")
    
    # Create new document
    new_doc = fitz.open()
    
    # We'll use a different approach: copy the XObject to a new page
    # and invoke it as the page content
    
    new_page = new_doc.new_page(width=width, height=height)
    
    # The simplest correct approach: set the Form's stream AS the page content
    # and copy its resources to the page resources
    
    # Get the page xref
    page_xref = new_page.xref
    
    # Create xref mapping for copying objects
    xref_map = {}
    
    def copy_xref(old_xref):
        """Copy an xref from src to new doc, handling dependencies."""
        if old_xref in xref_map:
            return xref_map[old_xref]
        
        # Create new xref
        new_xref = new_doc.get_new_xref()
        xref_map[old_xref] = new_xref
        
        # Get object and its refs
        obj_str = src_doc.xref_object(old_xref, compressed=False)
        sub_refs = re.findall(r'(\d+)\s+0\s+R', obj_str)
        
        # Copy dependencies first
        for ref in sub_refs:
            ref_int = int(ref)
            if ref_int not in xref_map:
                copy_xref(ref_int)
        
        # Update references in object string
        def replace_ref(m):
            old_ref = int(m.group(1))
            return f"{xref_map.get(old_ref, old_ref)} 0 R"
        
        new_obj_str = re.sub(r'(\d+)\s+0\s+R', replace_ref, obj_str)
        
        # Set object
        new_doc.update_object(new_xref, new_obj_str)
        
        # Copy stream if exists
        try:
            stream_data = src_doc.xref_stream_raw(old_xref)
            if stream_data:
                new_doc.update_stream(new_xref, stream_data, new=True)
        except:
            pass
        
        return new_xref
    
    # Copy all resources
    for ref in all_refs:
        copy_xref(ref)
    
    print(f"Copied {len(xref_map)} objects")
    
    # Update references in resources dict
    def replace_ref(m):
        old_ref = int(m.group(1))
        return f"{xref_map.get(old_ref, old_ref)} 0 R"
    
    new_resources = re.sub(r'(\d+)\s+0\s+R', replace_ref, resources_dict)
    
    # Create content stream xref
    content_xref = new_doc.get_new_xref()
    new_doc.update_object(content_xref, f"<< /Length {len(stream)} >>")
    new_doc.update_stream(content_xref, stream)
    
    # Update page with content and resources
    page_dict = f"""<<
  /Type /Page
  /MediaBox [0 0 {width} {height}]
  /Contents {content_xref} 0 R
  /Resources {new_resources}
  /Parent 3 0 R
>>"""
    new_doc.update_object(page_xref, page_dict)
    
    # Save
    new_doc.save(output_path, garbage=4, deflate=True, clean=True)
    new_doc.close()
    
    file_size = os.path.getsize(output_path)
    print(f"Saved: {output_path} ({file_size/1024:.1f} KB)")
    
    return output_path


def verify_pdf(pdf_path, preview_path=None):
    """Verify the PDF and optionally save a preview."""
    doc = fitz.open(pdf_path)
    page = doc[0]
    
    print(f"Verification:")
    print(f"  Pages: {doc.page_count}")
    print(f"  Size: {page.rect.width:.1f} x {page.rect.height:.1f}")
    
    # Try to render
    try:
        pix = page.get_pixmap(dpi=150)
        if preview_path:
            pix.save(preview_path)
            print(f"  Preview: {preview_path} ({pix.width}x{pix.height})")
    except Exception as e:
        print(f"  Render error: {e}")
    
    doc.close()


if __name__ == "__main__":
    # Test with FairDiffRec Kiviat diagram
    src = fitz.open("files/how_fair_diffusion_recsys_3705328.3759318.pdf")
    
    output = "images/projects/fairdiffrec/kiviat_form_extract.pdf"
    extract_form_xobject(src, 208, output)
    
    src.close()
    
    verify_pdf(output, "images/projects/fairdiffrec/kiviat_form_extract.png")
