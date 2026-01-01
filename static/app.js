/*HOME PAGE js*/
        let currentSlideIndex = 0;
        let autoSlideInterval;
        let certSlideIndex = 0;
        let certAutoSlideInterval;
        const totalCertSlides = 5; // Only 5 courses to display

        // Testimonial Slider Functions
        function showSlide(index) {
            const slides = document.querySelectorAll('.testimonial-slide');
            const dots = document.querySelectorAll('.dot');

            if (index >= slides.length) currentSlideIndex = 0;
            if (index < 0) currentSlideIndex = slides.length - 1;

            slides.forEach(slide => slide.classList.remove('active'));
            dots.forEach(dot => dot.classList.remove('active'));

            slides[currentSlideIndex].classList.add('active');
            dots[currentSlideIndex].classList.add('active');
        }

        function changeSlide(direction) {
            currentSlideIndex += direction;
            showSlide(currentSlideIndex);
            resetAutoSlide();
        }

        function currentSlide(index) {
            currentSlideIndex = index;
            showSlide(currentSlideIndex);
            resetAutoSlide();
        }

        function autoSlide() {
            currentSlideIndex++;
            showSlide(currentSlideIndex);
        }

        function resetAutoSlide() {
            clearInterval(autoSlideInterval);
            autoSlideInterval = setInterval(autoSlide, 5000);
        }

        // Certification Slider Functions
        function initCertSlider() {
            const certDots = document.getElementById('certDots');
            const isMobile = window.innerWidth <= 768;

            // Mobile: 5 dots, Desktop: 3 dots (since we can only slide to show cards at positions 0, 1, 2)
            const dotsToShow = isMobile ? totalCertSlides : Math.max(1, totalCertSlides - 2);

            certDots.innerHTML = '';
            for (let i = 0; i < dotsToShow; i++) {
                const dot = document.createElement('span');
                dot.className = 'cert-dot';
                if (i === 0) dot.classList.add('active');
                dot.onclick = () => goToCertSlide(i);
                certDots.appendChild(dot);
            }
        }

        function updateCertSlider() {
            const slider = document.getElementById('certSlider');
            const dots = document.querySelectorAll('.cert-dot');
            const isMobile = window.innerWidth <= 768;

            let translateValue;
            if (isMobile) {
                // Mobile: slide one course at a time (100% per slide)
                translateValue = certSlideIndex * 100;
            } else {
                // Desktop: Calculate to always show 3 cards
                // For 5 cards, max we can slide is to show cards 3,4,5 (index 2)
                const maxDesktopSlide = Math.max(0, totalCertSlides - 3);
                const actualSlide = Math.min(certSlideIndex, maxDesktopSlide);
                translateValue = actualSlide * (100 / 3);
            }

            slider.style.transform = `translateX(-${translateValue}%)`;

            dots.forEach((dot, index) => {
                dot.classList.toggle('active', index === certSlideIndex);
            });
        }

        function moveCertSlide(direction) {
            const isMobile = window.innerWidth <= 768;
            const maxSlides = isMobile ? totalCertSlides - 1 : Math.max(0, totalCertSlides - 3);

            certSlideIndex += direction;

            if (certSlideIndex > maxSlides) certSlideIndex = 0;
            if (certSlideIndex < 0) certSlideIndex = maxSlides;

            updateCertSlider();
            resetCertAutoSlide();
        }

        function goToCertSlide(index) {
            certSlideIndex = index;
            updateCertSlider();
            resetCertAutoSlide();
        }

        function autoCertSlide() {
            const isMobile = window.innerWidth <= 768;
            const maxSlides = isMobile ? totalCertSlides - 1 : Math.max(0, totalCertSlides - 3);

            certSlideIndex++;
            if (certSlideIndex > maxSlides) certSlideIndex = 0;
            updateCertSlider();
        }

        function resetCertAutoSlide() {
            clearInterval(certAutoSlideInterval);
            certAutoSlideInterval = setInterval(autoCertSlide, 4000);
        }

        // Reinitialize slider on window resize
        let resizeTimeout;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(() => {
                certSlideIndex = 0;
                initCertSlider();
                updateCertSlider();
            }, 250);
        });

        // Initialize sliders on page load
        window.addEventListener('DOMContentLoaded', () => {
            initCertSlider();
            autoSlideInterval = setInterval(autoSlide, 5000);
            certAutoSlideInterval = setInterval(autoCertSlide, 4000);
        });

        function toggleMenu() {
            const nav = document.querySelector('.main-nav');
            nav.classList.toggle('active');
        }

        function toggleDropdown(event, element) {
            if (window.innerWidth <= 768) {
                event.preventDefault();
                event.stopPropagation();
                const parentLi = element.closest('li');
                parentLi.classList.toggle('open');
            }
        }

        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const href = this.getAttribute('href');
                if (!this.classList.contains('has-dropdown') || window.innerWidth > 768) {
                    e.preventDefault();
                    const target = document.querySelector(href);
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth'
                        });
                        if (window.innerWidth <= 768) {
                            const nav = document.querySelector('.main-nav');
                            nav.classList.remove('active');
                        }
                    }
                }
            });
        });

        document.addEventListener('click', function (event) {
            if (window.innerWidth <= 768) {
                const dropdowns = document.querySelectorAll('.has-mobile-dropdown.open');
                dropdowns.forEach(dropdown => {
                    if (!dropdown.contains(event.target)) {
                        dropdown.classList.remove('open');
                    }
                });
            }
        });

        // Scroll to top functionality
        const scrollTopBtn = document.getElementById("scrollTopBtn");

        window.addEventListener("scroll", () => {
            if (window.scrollY > 300) {
                scrollTopBtn.style.display = "block";
            } else {
                scrollTopBtn.style.display = "none";
            }
        });

        scrollTopBtn.addEventListener("click", () => {
            window.scrollTo({ top: 0, behavior: "smooth" });
        });
   



        /*ABOUT US PAGE js*/