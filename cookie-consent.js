(function () {
  'use strict';
  // Renew consent: the choice now explicitly includes the optional visitor counter.
  var STORAGE_KEY = 'tdl-cookie-consent-v2';
  var GA_ID = 'G-77H5RENPZ3';
  var accepted = false;
  var counterStarted = false;
  var counterRequest;
  var banner, settings, returnFocus;
  function stored() {
    try { return localStorage.getItem(STORAGE_KEY); } catch (_) { return null; }
  }
  function save(value) {
    try { localStorage.setItem(STORAGE_KEY, value); return true; } catch (_) { return false; }
  }
  function clearAnalyticsCookies() {
    var domains = ['', location.hostname, '.' + location.hostname];
    var parts = location.hostname.split('.');
    if (parts.length > 2) domains.push('.' + parts.slice(-2).join('.'));
    var paths = ['/'];
    var segments = location.pathname.split('/').filter(Boolean);
    segments.forEach(function (_, i) { paths.push('/' + segments.slice(0, i + 1).join('/')); });
    document.cookie.split(';').forEach(function (entry) {
      var name = entry.split('=')[0].trim();
      if (!/^(_ga($|_)|_gid$|_gat($|_))/.test(name)) return;
      domains.forEach(function (domain) { paths.forEach(function (path) {
        document.cookie = name + '=; Max-Age=0; path=' + path + (domain ? '; domain=' + domain : '') + '; SameSite=Lax';
      }); });
    });
  }
  function counterLabel(text, label) {
    var el = document.getElementById('visitor-count');
    if (!el) return;
    el.textContent = text; el.setAttribute('aria-label', label); el.title = label;
  }
  function enable() {
    accepted = true;
    window['ga-disable-' + GA_ID] = false;
    if (!document.getElementById('google-analytics')) {
      window.dataLayer = window.dataLayer || [];
      window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
      window.gtag('js', new Date());
      window.gtag('config', GA_ID, { allow_google_signals: false, allow_ad_personalization_signals: false });
      var script = document.createElement('script');
      script.async = true; script.id = 'google-analytics';
      script.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
      document.head.appendChild(script);
    }
    if (document.getElementById('visitor-count') && !counterStarted) {
      counterStarted = true;
      counterRequest = new AbortController();
      fetch('https://api.counterapi.dev/v1/tripperdeelabs-com/homepage/up?cacheBust=' + Date.now(), {
        cache: 'no-store', credentials: 'omit', referrerPolicy: 'no-referrer', signal: counterRequest.signal
      }).then(function (response) {
        if (!response.ok) throw new Error('Counter unavailable');
        return response.json();
      }).then(function (result) {
        if (accepted && Number.isFinite(result.count)) counterLabel(Number(result.count).toLocaleString(), result.count + ' homepage visits counted with consent');
      }).catch(function () {
        if (accepted) counterLabel('—', 'Visitor counter temporarily unavailable');
      });
    }
  }
  function disable() {
    accepted = false;
    window['ga-disable-' + GA_ID] = true;
    if (counterRequest) counterRequest.abort();
    var script = document.getElementById('google-analytics');
    if (script) script.remove();
    clearAnalyticsCookies();
    counterLabel('—', 'Visitor counter off until you accept optional analytics');
  }
  function openBanner() {
    returnFocus = document.activeElement;
    banner.hidden = false; settings.hidden = true;
    banner.querySelector('.cookie-decline').focus();
  }
  function closeBanner() {
    banner.hidden = true; settings.hidden = false;
    if (returnFocus && returnFocus !== document.body && returnFocus.isConnected) returnFocus.focus();
    else settings.focus();
  }
  function choose(value) {
    var wasAccepted = accepted;
    if (value !== 'accepted') disable();
    var persisted = save(value);
    if (value === 'accepted') enable();
    closeBanner();
    // Remove already-loaded analytics code and listeners after withdrawal.
    // If storage is unavailable, the disable flag still blocks further GA measurement.
    if (wasAccepted && value !== 'accepted' && persisted) location.reload();
  }
  function build() {
    banner = document.createElement('section');
    banner.className = 'cookie-banner'; banner.hidden = true;
    banner.setAttribute('role', 'region'); banner.setAttribute('aria-labelledby', 'cookie-title');
    banner.innerHTML = '<div class="cookie-copy"><h2 id="cookie-title">Your privacy, your choice</h2>' +
      '<p>With your permission, Google Analytics and our visitor counter help us understand site visits. Declining keeps both off. <a href="/privacy/">Website privacy details</a>.</p></div>' +
      '<div class="cookie-actions"><button class="cookie-button cookie-decline" type="button">Decline</button>' +
      '<button class="cookie-button cookie-accept" type="button">Accept analytics</button></div>';
    settings = document.createElement('button'); settings.className = 'cookie-settings';
    settings.type = 'button'; settings.textContent = 'Cookie settings'; settings.hidden = true;
    banner.querySelector('.cookie-accept').addEventListener('click', function () { choose('accepted'); });
    banner.querySelector('.cookie-decline').addEventListener('click', function () { choose('declined'); });
    settings.addEventListener('click', openBanner);
    document.body.appendChild(banner); document.body.appendChild(settings);
    var value = stored();
    if (value === 'accepted') enable(); else disable();
    if (value === 'accepted' || value === 'declined') settings.hidden = false;
    else banner.hidden = false;
    window.addEventListener('storage', function (event) {
      if (event.key !== STORAGE_KEY && event.key !== null) return;
      if (stored() === 'accepted') { enable(); banner.hidden = true; settings.hidden = false; }
      else {
        var wasAccepted = accepted; disable();
        if (wasAccepted) location.reload();
        else { banner.hidden = stored() === 'declined'; settings.hidden = !banner.hidden; }
      }
    });
  }
  window['ga-disable-' + GA_ID] = true;
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', build);
  else build();
})();
