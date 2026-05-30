document.addEventListener("DOMContentLoaded", () => {
  // Intersection Observer for scroll reveals
  const revealElements = document.querySelectorAll('.reveal-on-scroll');
  
  const revealOptions = {
    root: null,
    rootMargin: '0px 0px -10% 0px',
    threshold: 0.1
  };
  
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        // observer.unobserve(entry.target); // keep it to animate multiple times or uncomment to do it once
      }
    });
  }, revealOptions);
  
  revealElements.forEach(el => revealObserver.observe(el));
  
  // Subtle parallax effect for large images
  const parallaxImages = document.querySelectorAll('.parallax-image');
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    parallaxImages.forEach(img => {
      const speed = img.dataset.speed || 0.05;
      img.style.transform = `translateY(${scrollY * speed}px)`;
    });
  });
});
