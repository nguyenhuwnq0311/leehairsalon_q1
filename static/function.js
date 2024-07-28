document.addEventListener('DOMContentLoaded', function() {
    console.log('Website has loaded.');

    function handleScroll() {
        let elements = document.querySelectorAll('img, video, p, h3, h4, h5, h6');
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
    }

    window.addEventListener('scroll', handleScroll);
    window.dispatchEvent(new Event('scroll'));
});
