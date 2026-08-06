(function () {
  'use strict';

  var localPart = String.fromCharCode(102, 101, 101, 100, 98, 97, 99, 107);
  var domain = String.fromCharCode(116, 114, 105, 112, 112, 101, 114, 100, 101, 101, 108, 97, 98, 115, 46, 99, 111, 109);
  var address = localPart + '@' + domain;

  document.querySelectorAll('a[href^="/contact-email"]').forEach(function (link) {
    link.addEventListener('click', function (event) {
      event.preventDefault();
      var query = link.getAttribute('href').slice('/contact-email'.length);
      window.location.href = 'mailto:' + address + query;
    });
  });
})();
