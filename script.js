const navbar = document.getElementById('navbar');
const navMenu = document.querySelector('.nav-menu');
const hamburger = document.querySelector('.hamburger');
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const hasFinePointer = window.matchMedia('(pointer: fine)').matches;

// Theme Toggle
const themeToggle = document.getElementById('themeToggle');
const html = document.documentElement;

// Load saved theme or default to dark
const savedTheme = localStorage.getItem('theme') || 'dark';
html.setAttribute('data-theme', savedTheme);

// Theme toggle functionality
if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
    });
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', event => {
        const href = anchor.getAttribute('href');
        if (href && href.startsWith('#')) {
            event.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: prefersReducedMotion ? 'auto' : 'smooth',
                    block: 'start'
                });
            }
            if (navMenu && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                resetHamburger();
            }
        }
    });
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
    if (!navbar) return;
    if (window.pageYOffset > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Mobile menu toggle
if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        animateHamburger();
    });

    document.addEventListener('click', (event) => {
        if (!navMenu.contains(event.target) && !hamburger.contains(event.target)) {
            navMenu.classList.remove('active');
            resetHamburger();
        }
    });
}

function animateHamburger() {
    if (!hamburger || !navMenu) return;
    const spans = hamburger.querySelectorAll('span');
    if (!spans.length) return;
    if (navMenu.classList.contains('active')) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
    } else {
        resetHamburger();
    }
}

function resetHamburger() {
    if (!hamburger) return;
    const spans = hamburger.querySelectorAll('span');
    if (!spans.length) return;
    spans[0].style.transform = 'none';
    spans[1].style.opacity = '1';
    spans[2].style.transform = 'none';
}

// Reveal animations
const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.25,
    rootMargin: '0px 0px -80px 0px'
});

document.querySelectorAll('.reveal').forEach(element => {
    if (prefersReducedMotion) {
        element.classList.add('is-visible');
    } else {
        revealObserver.observe(element);
    }
});

// Metrics counter animation
const counters = document.querySelectorAll('.metric-value[data-target]');
if (counters.length && prefersReducedMotion) {
    counters.forEach(counter => {
        const target = counter.dataset.target;
        const suffix = counter.dataset.suffix || '';
        if (target) {
            counter.textContent = `${target}${suffix}`;
        }
    });
} else if (counters.length) {
    const counterObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                if (!el.dataset.animated) {
                    animateCounter(el);
                    el.dataset.animated = 'true';
                }
                observer.unobserve(el);
            }
        });
    }, { threshold: 0.6 });

    counters.forEach(counter => counterObserver.observe(counter));
}

function animateCounter(element) {
    const target = parseInt(element.dataset.target, 10);
    if (Number.isNaN(target)) return;
    const suffix = element.dataset.suffix || '';
    const duration = 1500;
    const startTime = performance.now();

    const step = (now) => {
        const progress = Math.min((now - startTime) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 4);
        element.textContent = Math.round(target * eased) + suffix;
        if (progress < 1) {
            requestAnimationFrame(step);
        }
    };

    requestAnimationFrame(step);
}

// Skill bar animation
const progressBars = document.querySelectorAll('.skill-progress[data-progress]');
if (progressBars.length && prefersReducedMotion) {
    progressBars.forEach(bar => {
        const span = bar.querySelector('span');
        if (span) {
            span.style.width = `${bar.dataset.progress}%`;
        }
    });
} else if (progressBars.length) {
    const progressObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progress = entry.target.dataset.progress;
                const span = entry.target.querySelector('span');
                if (span) {
                    span.style.width = `${progress}%`;
                }
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    progressBars.forEach(bar => progressObserver.observe(bar));
}

// Active state for nav links
const sections = document.querySelectorAll('.hero, .section');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
    let currentId = '';
    sections.forEach(section => {
        const top = section.offsetTop - 220;
        if (window.pageYOffset >= top) {
            currentId = section.getAttribute('id') || currentId;
        }
    });

    navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === `#${currentId}`);
    });
});

// Hero spotlight interaction
const hero = document.querySelector('.hero');
if (hero && hasFinePointer && !prefersReducedMotion) {
    const resetHeroCursor = () => {
        hero.style.setProperty('--cursor-x', '60%');
        hero.style.setProperty('--cursor-y', '30%');
    };

    resetHeroCursor();

    hero.addEventListener('pointermove', (event) => {
        const rect = hero.getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width) * 100;
        const y = ((event.clientY - rect.top) / rect.height) * 100;
        hero.style.setProperty('--cursor-x', `${x}%`);
        hero.style.setProperty('--cursor-y', `${y}%`);
    });

    hero.addEventListener('pointerleave', resetHeroCursor);
}

// Tilt interaction
if (hasFinePointer && !prefersReducedMotion) {
    const tiltElements = document.querySelectorAll('[data-tilt]');

    tiltElements.forEach(element => {
        element.addEventListener('mouseenter', () => {
            element.classList.add('is-hovering');
        });

        element.addEventListener('mousemove', (event) => {
            const rect = element.getBoundingClientRect();
            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;
            const rotateY = ((x / rect.width) - 0.5) * 14;
            const rotateX = ((y / rect.height) - 0.5) * -12;
            element.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(12px)`;
        });

        element.addEventListener('mouseleave', () => {
            element.classList.remove('is-hovering');
            element.style.transform = '';
        });
    });
}

// Typing effect for hero title
const heroTitle = document.querySelector('.hero-name');
if (heroTitle && !prefersReducedMotion) {
    const text = heroTitle.textContent;
    heroTitle.textContent = '';
    let i = 0;

    const typeWriter = () => {
        if (i < text.length) {
            heroTitle.textContent += text.charAt(i);
            i += 1;
            setTimeout(typeWriter, 80);
        }
    };

    setTimeout(typeWriter, 400);
}

