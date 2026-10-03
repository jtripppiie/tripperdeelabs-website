(function () {
  'use strict';

  var STORAGE_KEY = 'tdl-cookie-consent';
  var GTM_ID = 'GTM-KTV46GP6';
  var GA_MEASUREMENT_ID = 'G-77H5RENPZ3';

  function getConsent() {
    try {
      return window.localStorage.getItem(STORAGE_KEY);
    } catch (error) {
      return null;
    }
  }

  function saveConsent(value) {
    try {
      window.localStorage.setItem(STORAGE_KEY, value);
    } catch (error) {
      // The choice still applies for this page view when storage is unavailable.
    }
  }

  function gtag() {
    window.dataLayer.push(arguments);
  }

  function initDataLayer() {
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || gtag;
  }

  function insertScript(id, src) {
    if (document.getElementById(id)) return;

    var script = document.createElement('script');
    script.async = true;
    script.id = id;
    script.src = src;
    var first = document.getElementsByTagName('script')[0];
    if (first && first.parentNode) first.parentNode.insertBefore(script, first);
    else document.head.appendChild(script);
  }

  function loadTagManager() {
    if (document.getElementById('google-tag-manager')) return;

    initDataLayer();
    window.dataLayer.push({ 'gtm.start': new Date().getTime(), event: 'gtm.js' });
    insertScript('google-tag-manager', 'https://www.googletagmanager.com/gtm.js?id=' + GTM_ID);
  }

  function loadGoogleAnalytics() {
    if (document.getElementById('google-analytics')) return;

    initDataLayer();
    window.gtag('js', new Date());
    window.gtag('config', GA_MEASUREMENT_ID);
    insertScript('google-analytics', 'https://www.googletagmanager.com/gtag/js?id=' + GA_MEASUREMENT_ID);
  }

  function enableAnalytics() {
    loadTagManager();
    // GTM-KTV46GP6 is published with no tags, so GA4 still needs a direct
    // config after consent. Remove this call if GA4 is added inside GTM.
    loadGoogleAnalytics();
  }

  function buildInterface() {
    var banner = document.createElement('section');
    banner.className = 'cookie-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-modal', 'true');
    banner.setAttribute('aria-labelledby', 'cookie-title');
    banner.hidden = true;
    banner.innerHTML =
      '<div class="cookie-copy">' +
        '<h2 id="cookie-title">Your privacy, your choice</h2>' +
        '<p>We use optional analytics cookies only to understand how this site is used. TripperDeeLabs does not sell your personal data, and declining will not affect how the site works.</p>' +
      '</div>' +
      '<div class="cookie-actions">' +
        '<button class="cookie-button cookie-decline" type="button">Decline</button>' +
        '<button class="cookie-button cookie-accept" type="button">Accept analytics</button>' +
      '</div>';

    var settings = document.createElement('button');
    settings.className = 'cookie-settings';
    settings.type = 'button';
    settings.textContent = 'Cookie settings';
    settings.hidden = true;

    function openBanner() {
      banner.hidden = false;
      settings.hidden = true;
      banner.querySelector('.cookie-accept').focus();
    }

    function closeBanner() {
      banner.hidden = true;
      settings.hidden = false;
    }

    banner.querySelector('.cookie-accept').addEventListener('click', function () {
      saveConsent('accepted');
      enableAnalytics();
      closeBanner();
    });

    banner.querySelector('.cookie-decline').addEventListener('click', function () {
      saveConsent('declined');
      closeBanner();
    });

    settings.addEventListener('click', openBanner);

    document.body.appendChild(banner);
    document.body.appendChild(settings);

    if (getConsent()) {
      settings.hidden = false;
    } else {
      openBanner();
    }
  }

  if (getConsent() === 'accepted') enableAnalytics();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildInterface);
  } else {
    buildInterface();
  }
})();
