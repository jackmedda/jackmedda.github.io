import pymupdf as fitz
import os
import argparse

try:
    from PIL import Image
    import io
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("Note: PIL not installed. Advanced content analysis disabled. Install with: pip install Pillow")

try:
    import pikepdf
    HAS_PIKEPDF = True
except ImportError:
    HAS_PIKEPDF = False
    print("Note: pikepdf not installed. Vector figure extraction will use rendering fallback. Install with: pip install pikepdf")

def analyze_image_content(image_bytes, width, height):
    """
    Analyze image content to classify it.
    
    Returns: dict with analysis results including:
        - is_photo: bool - likely a photograph (portrait, landscape)
        - is_chart: bool - likely a chart/diagram (high contrast, geometric)
        - is_solid: bool - mostly solid color
        - color_variance: float - measure of color diversity
        - unique_colors: int - number of unique colors sampled
        - dominant_color: tuple - most common RGB color
        - edge_density: float - measure of edges (high for charts, low for photos)
    """
    result = {
        'is_photo': False,
        'is_chart': False,
        'is_solid': False,
        'color_variance': 0,
        'unique_colors': 0,
        'dominant_color': (255, 255, 255),
        'edge_density': 0,
        'skin_tone_ratio': 0,
    }
    
    if not HAS_PIL:
        return result
    
    try:
        img = Image.open(io.BytesIO(image_bytes))
        
        # Convert to RGB
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Sample pixels - use new API if available (Pillow 14+)
        try:
            pixels = list(img.get_flattened_data())
        except AttributeError:
            pixels = list(img.getdata())
        sample_size = min(2000, len(pixels))
        sample_step = max(1, len(pixels) // sample_size)
        sampled = pixels[::sample_step]
        
        if len(sampled) < 10:
            return result
        
        # Calculate color variance
        r_vals = [p[0] for p in sampled]
        g_vals = [p[1] for p in sampled]
        b_vals = [p[2] for p in sampled]
        
        def variance(vals):
            mean = sum(vals) / len(vals)
            return sum((x - mean) ** 2 for x in vals) / len(vals)
        
        result['color_variance'] = variance(r_vals) + variance(g_vals) + variance(b_vals)
        
        # Count unique colors
        unique_colors = set(sampled)
        result['unique_colors'] = len(unique_colors)
        
        # Find dominant color
        from collections import Counter
        color_counts = Counter(sampled)
        result['dominant_color'] = color_counts.most_common(1)[0][0]
        
        # Detect skin tones (for author photo detection)
        skin_tone_count = 0
        for r, g, b in sampled:
            # Common skin tone ranges (various ethnicities)
            if (r > 60 and g > 40 and b > 20 and
                r > b and r > g and
                abs(r - g) < 100 and
                r - b > 15 and g - b > 15):
                skin_tone_count += 1
        result['skin_tone_ratio'] = skin_tone_count / len(sampled)
        
        # Detect solid color images
        if result['color_variance'] < 100:
            result['is_solid'] = True
        
        # Heuristics for photo vs chart
        # Photos: significant skin tones in a reasonably sized image (portraits/author photos)
        # Charts: discrete colors, high contrast, geometric patterns
        
        # Only mark as portrait photo if significant skin tones AND reasonable size
        if result['skin_tone_ratio'] > 0.12 and width > 80 and height > 80:
            # Likely a portrait/author photo
            result['is_photo'] = True
            result['is_portrait'] = True
        elif result['color_variance'] > 5000 and result['unique_colors'] > 200:
            # High variance and many colors = photo
            result['is_photo'] = True
        elif result['unique_colors'] < 50 and result['color_variance'] > 500:
            # Few distinct colors but some variance = chart/diagram
            result['is_chart'] = True
        
        # Edge detection (simplified - check neighboring pixel differences)
        try:
            # Resize for faster processing
            small = img.resize((min(100, width), min(100, height)))
            try:
                small_pixels = list(small.get_flattened_data())
            except AttributeError:
                small_pixels = list(small.getdata())
            small_width = small.width
            
            edge_count = 0
            for i in range(len(small_pixels) - small_width - 1):
                if i % small_width < small_width - 1:  # Not at right edge
                    p1 = small_pixels[i]
                    p2 = small_pixels[i + 1]  # Right neighbor
                    p3 = small_pixels[i + small_width]  # Bottom neighbor
                    
                    # High difference = edge
                    diff1 = sum(abs(p1[j] - p2[j]) for j in range(3))
                    diff2 = sum(abs(p1[j] - p3[j]) for j in range(3))
                    
                    if diff1 > 100 or diff2 > 100:
                        edge_count += 1
            
            result['edge_density'] = edge_count / (len(small_pixels) - small_width)
        except:
            pass
        
    except Exception as e:
        pass
    
    return result

def is_likely_stub_image(image_bytes, width, height, ext):
    """
    Determine if an image is likely a stub/placeholder based on multiple heuristics.
    
    Returns: (is_stub: bool, reason: str, analysis: dict)
    """
    analysis = {}
    
    # Very small dimensions (icons, bullets, tiny decorations)
    if width < 20 or height < 20:
        return True, f"tiny dimensions ({width}x{height})", analysis
    
    # Extreme aspect ratios (likely lines, borders, separators)
    aspect_ratio = max(width, height) / max(min(width, height), 1)
    if aspect_ratio > 15:
        return True, f"extreme aspect ratio ({aspect_ratio:.1f})", analysis
    
    # Very narrow strips (headers, footers, lines)
    if width < 30 or height < 30:
        if aspect_ratio > 5:
            return True, f"narrow strip ({width}x{height})", analysis
    
    # Advanced content analysis
    if HAS_PIL:
        analysis = analyze_image_content(image_bytes, width, height)
        
        # Solid color blocks
        if analysis['is_solid'] and width * height < 10000:
            return True, f"solid color block (variance={analysis['color_variance']:.1f})", analysis
        
        # Very few unique colors in small image
        if width * height < 5000 and analysis['unique_colors'] < 5:
            return True, f"low color count ({analysis['unique_colors']} unique)", analysis
    
    return False, "passed all checks", analysis


def extract_xobject_image(doc, xref, output_base, page_num, rect, verbose=True, 
                          convert_to_png=False, png_dpi=200, pdf_path=None, xobj_name=None):
    """
    Extract an XObject as its native format (image or vector PDF).
    Uses pikepdf for proper Form XObject extraction (preserving vector graphics).
    Optionally convert vector PDFs to PNG for web use.
    
    Returns: (success: bool, final_path: str, format: str, width: int, height: int, size_kb: float)
    """
    # First, try to extract as a raster image
    try:
        img_data = doc.extract_image(xref)
        if img_data and img_data.get('image'):
            ext = img_data.get('ext', 'png')
            width = img_data.get('width', 0)
            height = img_data.get('height', 0)
            image_bytes = img_data['image']
            
            final_path = f"{output_base}.{ext}"
            with open(final_path, 'wb') as f:
                f.write(image_bytes)
            
            return True, final_path, ext, width, height, len(image_bytes) / 1024
    except Exception:
        pass
    
    # Check if it's a Form XObject (vector content)
    try:
        xobj_dict = doc.xref_object(xref, compressed=False)
        is_form = '/Subtype /Form' in xobj_dict or '/Subtype/Form' in xobj_dict
        
        if is_form:
            # Try pikepdf extraction first (proper vector extraction)
            if HAS_PIKEPDF and pdf_path and xobj_name:
                try:
                    success, path, fmt, w, h, size = extract_form_xobject_pikepdf(
                        pdf_path, page_num, xobj_name, output_base, 
                        convert_to_png=convert_to_png, png_dpi=png_dpi, verbose=verbose
                    )
                    if success:
                        return success, path, fmt, w, h, size
                except Exception as e:
                    if verbose:
                        print(f"    pikepdf extraction failed: {e}, falling back to render")
            
            # Fallback: render the region (screenshot approach)
            if rect:
                width = rect.width
                height = rect.height
                
                pdf_path_out = f"{output_base}.pdf"
                
                # Create a new PDF with just this region
                new_doc = fitz.open()
                new_page = new_doc.new_page(width=width, height=height)
                
                # Copy the region from source
                new_page.show_pdf_page(new_page.rect, doc, page_num, clip=rect)
                new_doc.save(pdf_path_out)
                
                import os as os_module
                
                if convert_to_png:
                    # Convert the PDF to PNG for web use
                    png_path = f"{output_base}.png"
                    zoom = png_dpi / 72
                    mat = fitz.Matrix(zoom, zoom)
                    pix = new_doc[0].get_pixmap(matrix=mat)
                    pix.save(png_path)
                    new_doc.close()
                    
                    # Remove the intermediate PDF
                    os_module.remove(pdf_path_out)
                    
                    size_kb = os_module.path.getsize(png_path) / 1024
                    return True, png_path, 'png', pix.width, pix.height, size_kb
                else:
                    new_doc.close()
                    size_kb = os_module.path.getsize(pdf_path_out) / 1024
                    return True, pdf_path_out, 'pdf', int(width), int(height), size_kb
            
    except Exception as e:
        if verbose:
            print(f"    Could not extract XObject: {e}")
    
    return False, None, None, 0, 0, 0


def extract_form_xobject_pikepdf(pdf_path, page_num, xobj_name, output_base, 
                                  convert_to_png=False, png_dpi=200, verbose=True):
    """
    Extract a Form XObject as a standalone PDF using pikepdf.
    This properly preserves vector graphics, fonts, and all resources.
    
    Args:
        pdf_path: Path to the source PDF
        page_num: Page number (0-indexed)
        xobj_name: Name of the XObject (e.g., '/Im1', '/Xi4')
        output_base: Base path for output (without extension)
        convert_to_png: Whether to convert to PNG
        png_dpi: DPI for PNG conversion
        
    Returns: (success: bool, final_path: str, format: str, width: int, height: int, size_kb: float)
    """
    src = pikepdf.open(pdf_path)
    src_page = src.pages[page_num]
    
    # Get the XObject
    if not hasattr(src_page, 'Resources') or '/XObject' not in src_page.Resources:
        raise ValueError(f"Page {page_num} has no XObjects")
    
    # Handle name format (may or may not have leading /)
    name_key = xobj_name if xobj_name.startswith('/') else f'/{xobj_name}'
    
    if name_key not in src_page.Resources.XObject:
        raise ValueError(f"XObject {name_key} not found on page {page_num}")
    
    xobj = src_page.Resources.XObject[name_key]
    
    # Check if it's a Form XObject
    if xobj.Subtype != pikepdf.Name('/Form'):
        raise ValueError(f"XObject {name_key} is not a Form (type: {xobj.Subtype})")
    
    # Get dimensions from BBox
    bbox = xobj.BBox
    width = float(bbox[2]) - float(bbox[0])
    height = float(bbox[3]) - float(bbox[1])
    
    # Create new PDF
    new_pdf = pikepdf.new()
    new_pdf.add_blank_page(page_size=(width, height))
    new_page = new_pdf.pages[0]
    
    # Copy the XObject with all dependencies
    copied_xobj = new_pdf.copy_foreign(xobj)
    
    # Set up resources - use the copied XObject's own resources
    new_page.Resources = pikepdf.Dictionary(
        XObject=pikepdf.Dictionary({'/Form0': copied_xobj})
    )
    
    # If the XObject has its own resources, merge them
    if hasattr(copied_xobj, 'Resources') and copied_xobj.Resources:
        for key, value in copied_xobj.Resources.items():
            if key != '/XObject':  # Don't overwrite our XObject reference
                new_page.Resources[key] = value
    
    # Create content stream that invokes the XObject
    content = b'q 1 0 0 1 0 0 cm /Form0 Do Q'
    new_page.Contents = new_pdf.make_stream(content)
    
    # Save PDF
    pdf_out_path = f"{output_base}.pdf"
    new_pdf.save(pdf_out_path)
    
    import os as os_module
    
    if convert_to_png:
        # Render to PNG using pymupdf
        render_doc = fitz.open(pdf_out_path)
        zoom = png_dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        pix = render_doc[0].get_pixmap(matrix=mat, alpha=False)
        
        png_path = f"{output_base}.png"
        pix.save(png_path)
        render_doc.close()
        
        # Remove intermediate PDF
        os_module.remove(pdf_out_path)
        
        size_kb = os_module.path.getsize(png_path) / 1024
        src.close()
        return True, png_path, 'png', pix.width, pix.height, size_kb
    else:
        size_kb = os_module.path.getsize(pdf_out_path) / 1024
        src.close()
        return True, pdf_out_path, 'pdf', int(width), int(height), size_kb
    
    return False, None, None, 0, 0, 0


def find_vector_figures(doc, page_num, min_size=100, verbose=True):
    """
    Find vector graphics (PDF, SVG, EPS-like content) on a page by analyzing 
    Form XObjects.
    
    Returns: list of dicts with 'rect' (bounding box), 'type', 'xref', etc.
    """
    page = doc[page_num]
    page_rect = page.rect
    page_area = page_rect.width * page_rect.height
    figures = []
    
    # Look for Form XObjects (contain vector figures)
    try:
        xobjects = page.get_xobjects()
        for xobj in xobjects:
            # xobj is (xref, name, invoker, bbox)
            if len(xobj) >= 4:
                bbox = xobj[3]  # Bounding box
                if bbox:
                    rect = fitz.Rect(bbox)
                    width = rect.width
                    height = rect.height
                    area = width * height
                    
                    # Filter out tiny objects
                    if width < min_size or height < min_size:
                        continue
                    
                    # Filter out full-page XObjects (>85% of page = likely template)
                    if area > page_area * 0.85:
                        if verbose:
                            print(f"    Skipping full-page XObject on page {page_num+1} ({width:.0f}x{height:.0f})")
                        continue
                    
                    # Filter out header/footer strips
                    if width > page_rect.width * 0.9 and height < page_rect.height * 0.1:
                        if verbose:
                            print(f"    Skipping header/footer XObject on page {page_num+1}")
                        continue
                    
                    # Check if this is a Form (vector) XObject
                    xobj_dict = doc.xref_object(xobj[0], compressed=False)
                    is_form = '/Subtype /Form' in xobj_dict or '/Subtype/Form' in xobj_dict
                    
                    if is_form:
                        figures.append({
                            'rect': rect,
                            'type': 'form',
                            'xref': xobj[0],
                            'name': xobj[1],
                        })
    except Exception as e:
        if verbose:
            print(f"  Note: Could not get XObjects: {e}")
    
    return figures


def merge_rectangles(rects, margin=10):
    """Merge overlapping or adjacent rectangles."""
    if not rects:
        return []
    
    # Expand each rect by margin for adjacency detection
    expanded = [r + (-margin, -margin, margin, margin) for r in rects]
    
    # Simple greedy merge
    merged = []
    used = [False] * len(expanded)
    
    for i, rect in enumerate(expanded):
        if used[i]:
            continue
        
        current = fitz.Rect(rect)
        used[i] = True
        changed = True
        
        while changed:
            changed = False
            for j, other in enumerate(expanded):
                if not used[j] and current.intersects(other):
                    current = current | other  # Union
                    used[j] = True
                    changed = True
        
        # Shrink back by margin
        final = current + (margin, margin, -margin, -margin)
        merged.append(final)
    
    return merged


def render_figure_region(doc, page_num, rect, output_path, dpi=200):
    """Render a specific region of a page as an image."""
    page = doc[page_num]
    
    # Add small padding
    padded = rect + (-5, -5, 5, 5)
    
    # Ensure we stay within page bounds
    padded = padded & page.rect
    
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=padded)
    
    pix.save(output_path)
    return pix.width, pix.height, len(pix.tobytes()) / 1024


def extract_images(pdf_path, output_dir, min_size_kb=5, min_dimension=50, 
                   exclude_photos=False, extract_vectors=True, vector_to_png=False,
                   vector_dpi=200, verbose=True):
    """
    Extract images from a PDF file with smart filtering.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save extracted images
        min_size_kb: Minimum image size in KB (default: 5KB - lowered for legends)
        min_dimension: Minimum width OR height in pixels (default: 50)
        exclude_photos: Skip images that appear to be photographs (e.g., author photos)
        extract_vectors: Also extract vector graphics (Form XObjects)
        vector_to_png: Convert extracted vector PDFs to PNG for web use
        vector_dpi: DPI for PNG conversion (default: 200)
        verbose: Print detailed filtering info
    """
    os.makedirs(output_dir, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    img_count = 0
    kept_count = 0
    photo_count = 0
    vector_count = 0
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)
        
        for img_idx, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image['image']
            image_ext = base_image['ext']
            width = base_image.get('width', 0)
            height = base_image.get('height', 0)
            size_kb = len(image_bytes) / 1024
            
            img_count += 1
            
            # Check if stub image using smart heuristics
            is_stub, reason, analysis = is_likely_stub_image(image_bytes, width, height, image_ext)
            
            if is_stub:
                if verbose:
                    print(f'  Filtered: page{page_num+1}_img{img_idx+1} - {reason} ({width}x{height}, {size_kb:.1f}KB)')
                continue
            
            # Check for portrait photos (author photos) if exclude_photos is enabled
            # Only filter if there are actual skin tones detected (real portrait photos)
            is_portrait = analysis.get('is_portrait', False) or analysis.get('skin_tone_ratio', 0) > 0.1
            if exclude_photos and is_portrait:
                photo_count += 1
                if verbose:
                    skin_ratio = analysis.get('skin_tone_ratio', 0)
                    print(f'  Portrait: page{page_num+1}_img{img_idx+1} - author photo detected (skin={skin_ratio:.1%}) ({width}x{height})')
                continue
            
            # Additional size check (but lower threshold)
            if size_kb < min_size_kb:
                if verbose:
                    print(f'  Filtered: page{page_num+1}_img{img_idx+1} - too small ({size_kb:.1f}KB < {min_size_kb}KB)')
                continue
            
            kept_count += 1
            
            # Tag the image with type info if available
            img_type = ""
            if analysis.get('is_portrait'):
                img_type = "_portrait"
            elif analysis.get('is_photo'):
                img_type = "_photo"
            elif analysis.get('is_chart'):
                img_type = "_chart"
            
            img_filename = f'{output_dir}/figure_{kept_count}{img_type}_page{page_num+1}.{image_ext}'
            
            with open(img_filename, 'wb') as f:
                f.write(image_bytes)
            
            # Print with analysis info
            extra_info = ""
            if analysis:
                parts = []
                if analysis.get('is_photo'):
                    parts.append("📷 PHOTO")
                if analysis.get('is_chart'):
                    parts.append("📊 CHART")
                if analysis.get('skin_tone_ratio', 0) > 0.1:
                    parts.append(f"skin={analysis['skin_tone_ratio']:.0%}")
                if parts:
                    extra_info = f" [{', '.join(parts)}]"
            
            print(f'Extracted: {img_filename} ({width}x{height}, {size_kb:.1f}KB){extra_info}')
    
    # Phase 2: Extract vector graphics (Form XObjects) as native format
    if extract_vectors:
        if verbose:
            print(f'\n--- Scanning for vector graphics ---')
        
        for page_num in range(len(doc)):
            vector_figures = find_vector_figures(doc, page_num, min_size=min_dimension, verbose=verbose)
            
            for fig in vector_figures:
                rect = fig['rect']
                xref = fig.get('xref')
                xobj_name = fig.get('name')  # Get the XObject name for pikepdf
                
                if not xref:
                    continue
                
                vector_count += 1
                kept_count += 1
                
                output_base = f'{output_dir}/vector_{vector_count}_page{page_num+1}'
                
                try:
                    success, final_path, fmt, w, h, size_kb = extract_xobject_image(
                        doc, xref, output_base, page_num, rect, verbose=verbose,
                        convert_to_png=vector_to_png, png_dpi=vector_dpi,
                        pdf_path=pdf_path, xobj_name=xobj_name
                    )
                    
                    if success:
                        fmt_icon = "📄" if fmt == 'pdf' else "🖼️"
                        print(f'Extracted: {final_path} ({w}x{h}, {size_kb:.1f}KB) [{fmt_icon} {fmt.upper()}]')
                    else:
                        if verbose:
                            print(f'  Could not extract vector figure from page {page_num+1}')
                        vector_count -= 1
                        kept_count -= 1
                except Exception as e:
                    if verbose:
                        print(f'  Failed to extract vector figure: {e}')
                    vector_count -= 1
                    kept_count -= 1
    
    print(f'\n--- Summary ---')
    print(f'Raster images found: {img_count}')
    print(f'Raster images kept: {kept_count - vector_count}')
    print(f'Raster images filtered: {img_count - (kept_count - vector_count) - photo_count}')
    if exclude_photos:
        print(f'Portraits excluded: {photo_count}')
    if extract_vectors:
        print(f'Vector figures extracted: {vector_count}')
    print(f'Total extracted: {kept_count}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract images from PDF with smart filtering')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('output_dir', help='Directory to save extracted images')
    parser.add_argument('--min-size', type=int, default=5, help='Minimum image size in KB (default: 5)')
    parser.add_argument('--min-dim', type=int, default=50, help='Minimum dimension in pixels (default: 50)')
    parser.add_argument('--no-photos', action='store_true', help='Exclude images that appear to be photographs')
    parser.add_argument('--no-vectors', action='store_true', help='Skip vector graphics extraction')
    parser.add_argument('--vector-to-png', action='store_true', help='Convert vector PDFs to PNG for web use')
    parser.add_argument('--vector-dpi', type=int, default=200, help='DPI for PNG conversion (default: 200)')
    parser.add_argument('-q', '--quiet', action='store_true', help='Suppress filter details')
    
    args = parser.parse_args()
    extract_images(args.pdf_path, args.output_dir, args.min_size, args.min_dim, 
                   exclude_photos=args.no_photos, extract_vectors=not args.no_vectors,
                   vector_to_png=args.vector_to_png, vector_dpi=args.vector_dpi,
                   verbose=not args.quiet)
