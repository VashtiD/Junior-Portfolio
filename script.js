// script.js

// Smooth scrolling for navigation links
document.querySelectorAll('nav ul li a').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetID = this.getAttribute('href').substring(1);
        const targetSection = document.getElementById(targetID);
        window.scrollTo({
            top: targetSection.offsetTop - 60, // offset for fixed header if any
            behavior: 'smooth'
        });
    });
});

// Highlight active nav link based on scroll position
const sections = document.querySelectorAll('section');
const navLinks = document.querySelectorAll('nav ul li a');

window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop - 70; // offset for header
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop && pageYOffset < sectionTop + sectionHeight) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Optional: Animate headings on load for a subtle entrance effect
window.addEventListener('load', () => {
    document.querySelectorAll('.section-heading').forEach(heading => {
        heading.style.opacity = 0;
        heading.style.transform = 'translateY(20px)';
        setTimeout(() => {
            heading.style.transition = 'opacity 1s, transform 1s';
            heading.style.opacity = 1;
            heading.style.transform = 'translateY(0)';
        }, 300);
    });
});
