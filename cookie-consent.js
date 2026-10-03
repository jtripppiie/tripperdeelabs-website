(function () {
  'use strict';

  var STORAGE_KEY = 'tdl-cookie-consent';
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

  function loadGoogleAnalytics() {
    if (document.getElementById('google-analytics')) return;

    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () {
      window.dataLayer.push(arguments);
    };
    window.gtag('js', new Date());
    window.gtag('config', GA_MEASUREMENT_ID);

    var script = document.createElement('script');
    script.async = true;
    script.id = 'google-analytics';
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_MEASUREMENT_ID;
    var first = document.getElementsByTagName('script')[0];
    if (first && first.parentNode) first.parentNode.insertBefore(script, first);
    else document.head.appendChild(script);
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
      loadGoogleAnalytics();
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

  if (getConsent() === 'accepted') loadGoogleAnalytics();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildInterface);
  } else {
    buildInterface();
  }
})();
