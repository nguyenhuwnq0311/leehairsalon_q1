document.addEventListener('DOMContentLoaded', function() {
    console.log('Website has loaded.');

    window.addEventListener('scroll', function() {
        let elements = document.querySelectorAll('img, video, p, h3, h5, h6');
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        elements.forEach(function(element) {
            if (element.getBoundingClientRect().top < window.innerHeight) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            } else {
                element.style.opacity = '0';
                element.style.transform = 'translateY(20px)';
            }
        });
    });

    window.dispatchEvent(new Event('scroll'));
});
