document.addEventListener('DOMContentLoaded', () => {
    // ==========================================
    // 1. HEADER SCROLL & MOBILE MENU
    // ==========================================
    const header = document.querySelector('.site-header');
    const hamburger = document.querySelector('.hamburger');
    const mainNav = document.querySelector('.main-nav');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 40) {
            header?.classList.add('scrolled');
        } else {
            header?.classList.remove('scrolled');
        }
    });

    if (hamburger && mainNav) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            mainNav.classList.toggle('open');
            document.body.classList.toggle('no-scroll');
        });
    }

    // ==========================================
    // 2. HERO SLIDER & TRANSITIONS
    // ==========================================
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.hero-dots button');
    let currentSlide = 0;
    let slideInterval;

    function goToSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });
        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });
        currentSlide = index;
    }

    function startHeroAutoplay() {
        if (slides.length <= 1) return;
        slideInterval = setInterval(() => {
            const next = (currentSlide + 1) % slides.length;
            goToSlide(next);
        }, 6000);
    }

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            clearInterval(slideInterval);
            goToSlide(index);
            startHeroAutoplay();
        });
    });

    startHeroAutoplay();

    // ==========================================
    // 3. STAGGERED SCROLL REVEALS
    // ==========================================
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });

    // Auto-assign reveal and staggered delay classes to grid cards
    const gridContainers = document.querySelectorAll('.events-grid, .ministries-grid, .leadership-grid');
    gridContainers.forEach(container => {
        Array.from(container.children).forEach((child, idx) => {
            child.classList.add('reveal', `delay-${(idx % 4) + 1}`);
        });
    });

    // Observe all reveal elements
    document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

    // ==========================================
    // 4. GIVING WIDGET SELECTION
    // ==========================================
    const amtBtns = document.querySelectorAll('.amt-btn');
    const amtInput = document.querySelector('.amt-input');

    amtBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            amtBtns.forEach(b => b.classList.remove('active'));
            e.currentTarget.classList.add('active');
            if (amtInput) {
                amtInput.value = e.currentTarget.dataset.amount || '';
            }
        });
    });
});