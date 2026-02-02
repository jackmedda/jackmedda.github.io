/* ==========================================================================
   Academic Project Page JavaScript
   Based on Academic Project Page Template by Eliahu Horwitz
   Adapted for Jekyll by GitHub Copilot
   ========================================================================== */

// Carousel functionality
let currentSlide = 0;

function moveCarousel(direction) {
  const slides = document.querySelectorAll('.carousel-slide');
  const dots = document.querySelectorAll('.dot');
  
  if (slides.length === 0) return;
  
  slides[currentSlide].classList.remove('active');
  dots[currentSlide].classList.remove('active');
  
  currentSlide += direction;
  
  if (currentSlide >= slides.length) {
    currentSlide = 0;
  } else if (currentSlide < 0) {
    currentSlide = slides.length - 1;
  }
  
  slides[currentSlide].classList.add('active');
  dots[currentSlide].classList.add('active');
}

function goToSlide(index) {
  const slides = document.querySelectorAll('.carousel-slide');
  const dots = document.querySelectorAll('.dot');
  
  if (slides.length === 0) return;
  
  slides[currentSlide].classList.remove('active');
  dots[currentSlide].classList.remove('active');
  
  currentSlide = index;
  
  slides[currentSlide].classList.add('active');
  dots[currentSlide].classList.add('active');
}

// Auto-advance carousel every 5 seconds
let carouselInterval;

function startCarouselAutoplay() {
  const slides = document.querySelectorAll('.carousel-slide');
  if (slides.length > 1) {
    carouselInterval = setInterval(() => moveCarousel(1), 5000);
  }
}

function stopCarouselAutoplay() {
  if (carouselInterval) {
    clearInterval(carouselInterval);
  }
}

// Copy BibTeX functionality
function copyBibTeX() {
  const bibtexCode = document.getElementById('bibtex-code');
  const copyBtn = document.querySelector('.copy-bibtex-btn');
  const copyText = copyBtn.querySelector('.copy-text');
  
  if (!bibtexCode) return;
  
  const text = bibtexCode.textContent || bibtexCode.innerText;
  
  navigator.clipboard.writeText(text).then(() => {
    // Show success state
    copyBtn.classList.add('copied');
    copyText.textContent = 'Copied!';
    
    // Reset after 2 seconds
    setTimeout(() => {
      copyBtn.classList.remove('copied');
      copyText.textContent = 'Copy';
    }, 2000);
  }).catch(err => {
    console.error('Failed to copy BibTeX:', err);
    // Fallback for older browsers
    fallbackCopyText(text);
  });
}

function fallbackCopyText(text) {
  const textArea = document.createElement('textarea');
  textArea.value = text;
  textArea.style.position = 'fixed';
  textArea.style.left = '-999999px';
  textArea.style.top = '-999999px';
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();
  
  try {
    document.execCommand('copy');
    const copyBtn = document.querySelector('.copy-bibtex-btn');
    const copyText = copyBtn.querySelector('.copy-text');
    copyBtn.classList.add('copied');
    copyText.textContent = 'Copied!';
    
    setTimeout(() => {
      copyBtn.classList.remove('copied');
      copyText.textContent = 'Copy';
    }, 2000);
  } catch (err) {
    console.error('Fallback: Could not copy text:', err);
  }
  
  document.body.removeChild(textArea);
}

// Scroll to top functionality
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

// Lazy loading for images
function initLazyLoading() {
  const images = document.querySelectorAll('img[loading="lazy"]');
  
  if ('loading' in HTMLImageElement.prototype) {
    // Browser supports native lazy loading
    return;
  }
  
  // Fallback for older browsers
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.classList.remove('lazy');
        imageObserver.unobserve(img);
      }
    });
  });
  
  images.forEach(img => imageObserver.observe(img));
}

// Smooth scroll for anchor links
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', function() {
  initLazyLoading();
  initSmoothScroll();
  startCarouselAutoplay();
  
  // Pause carousel on hover
  const carousel = document.querySelector('.carousel-wrapper');
  if (carousel) {
    carousel.addEventListener('mouseenter', stopCarouselAutoplay);
    carousel.addEventListener('mouseleave', startCarouselAutoplay);
  }
});

// Keyboard navigation for carousel
document.addEventListener('keydown', function(e) {
  const carousel = document.querySelector('.carousel-wrapper');
  if (!carousel) return;
  
  if (e.key === 'ArrowLeft') {
    moveCarousel(-1);
  } else if (e.key === 'ArrowRight') {
    moveCarousel(1);
  }
});
