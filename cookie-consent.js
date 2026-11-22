(function () {
  'use strict';
  // Keep this URL for existing pages; it now loads analytics without a consent UI.
  var GA_ID = 'G-77H5RENPZ3';
  function start() {
    if (document.getElementById('google-analytics')) return;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_ID, { allow_google_signals: false, allow_ad_personalization_signals: false });
    var script = document.createElement('script');
    script.async = true; script.id = 'google-analytics';
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(script);
    var counter = document.getElementById('visitor-count');
    if (!counter) return;
    fetch('https://api.counterapi.dev/v1/tripperdeelabs-com/homepage/up?cacheBust=' + Date.now(), {
      cache: 'no-store', credentials: 'omit', referrerPolicy: 'no-referrer'
    }).then(function (response) {
      if (!response.ok) throw new Error('Counter unavailable');
      return response.json();
    }).then(function (result) {
      if (!Number.isFinite(result.count)) throw new Error('Invalid counter');
      counter.textContent = Number(result.count).toLocaleString();
      counter.setAttribute('aria-label', result.count + ' homepage visits');
      counter.title = result.count + ' homepage visits';
    }).catch(function () {
      counter.textContent = '—';
      counter.setAttribute('aria-label', 'Visitor counter temporarily unavailable');
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
