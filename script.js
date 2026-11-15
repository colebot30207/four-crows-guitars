// The Four Crows Guitars — small enhancements, no dependencies.
(function () {
  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // Mobile menu
  var toggle = document.getElementById('menu-toggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && nav.classList.contains('open')) toggle.click();
    });
  }

  // Placeholder tiles: if a photo file is missing, mark its container so CSS shows a fallback.
  // Drop the real file into assets/photos/ and the tile just works — no code change needed.
  function markMissing(img) {
    var box = img.closest('figure, .hero-media');
    if (box) box.classList.add('is-fallback');
  }
  document.querySelectorAll('.card img, .hero-photo').forEach(function (img) {
    if (img.complete && img.naturalWidth === 0) markMissing(img);
    img.addEventListener('error', function () { markMissing(img); });
  });
})();
