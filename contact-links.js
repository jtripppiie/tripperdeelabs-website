(function () {
  'use strict';

  var localPart = String.fromCharCode(84, 114, 105, 112, 112, 101, 114, 68, 101, 101, 76, 97, 98, 115);
  var domain = String.fromCharCode(103, 109, 97, 105, 108, 46, 99, 111, 109);
  var address = localPart + '@' + domain;

  document.querySelectorAll('a[href^="/contact-email"]').forEach(function (link) {
    link.addEventListener('click', function (event) {
      event.preventDefault();
      var query = link.getAttribute('href').slice('/contact-email'.length);
      window.location.href = 'mailto:' + address + query;
    });
  });
})();
