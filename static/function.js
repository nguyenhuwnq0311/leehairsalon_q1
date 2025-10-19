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
    window.addEventListener('scroll', handleScroll);
    window.dispatchEvent(new Event('scroll')); // Kích hoạt lần đầu khi tải trang
});

// ==== Language-based image handling ==== //
window.getImage = function (link) {
  const base = window.STATIC_BASE || '/static/';
  const lang = localStorage.getItem('lang') || 'vi';

  // Nếu là tiếng ES thì chuyển ảnh sang thư mục price_en/
  if (lang === 'es') {
    link = link.replace('price_list/', 'price_list/price_en/');
  }

  // Nếu link đã được Flask render (bắt đầu bằng /static/...), chỉ cần trả về
  if (link.startsWith('/static/')) return link;

  return base + 'images/' + link;
};

