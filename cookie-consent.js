(function () {
  'use strict';

  var STORAGE_KEY = 'tdl-cookie-consent';
  var GTM_ID = 'GTM-KTV46GP6';

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

  function loadTagManager() {
    if (document.getElementById('google-tag-manager')) return;

    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });

    var script = document.createElement('script');
    script.async = true;
    script.id = 'google-tag-manager';
    script.src = 'https://www.googletagmanager.com/gtm.js?id=' + GTM_ID;
    document.head.appendChild(script);
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
      loadTagManager();
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

  if (getConsent() === 'accepted') loadTagManager();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildInterface);
  } else {
    buildInterface();
  }
})();
