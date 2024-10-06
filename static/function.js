document.addEventListener('DOMContentLoaded', function() {
    console.log('Website has loaded.');

    function handleScroll() {
        let elements = document.querySelectorAll('img, video, p, h3, h4, h5, h6');
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        elements.forEach(function(element) {
            if (element.getBoundingClientRect().top < window.innerHeight) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
                element.classList.add('show');
            } else {
                element.style.opacity = '0';
                element.style.transform = 'translateY(20px)';
                element.classList.remove('show');
            }
        });
    }
    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Tạo hiệu ứng cuộn mượt mà
        });
    }

    window.addEventListener('scroll', handleScroll);
    window.dispatchEvent(new Event('scroll')); // Kích hoạt lần đầu khi tải trang
});
