/*
 * MF Agentes: Google Analytics 4 + banner de cookies (LGPD) para o site e os apps.
 * Uso em qualquer página de *.mfagentes.com.br:
 *   <script src="https://mfagentes.com.br/analytics.js" defer></script>
 * A escolha do visitante vale para todo o domínio (cookie em .mfagentes.com.br).
 */
(function () {
  'use strict';

  var GA_ID = 'G-CM4GJS1MWY';
  var COOKIE = 'mf_consent';
  var ROOT = 'mfagentes.com.br';
  var host = location.hostname;
  var onDomain = host === ROOT || host.slice(-(ROOT.length + 1)) === '.' + ROOT;

  if (window.__mfAnalyticsLoaded) return;
  window.__mfAnalyticsLoaded = true;

  function readConsent() {
    var m = document.cookie.match(new RegExp('(?:^|; )' + COOKIE + '=([^;]*)'));
    return m ? decodeURIComponent(m[1]) : null;
  }

  function saveConsent(value) {
    var parts = [COOKIE + '=' + value, 'path=/', 'max-age=' + 60 * 60 * 24 * 365, 'SameSite=Lax'];
    if (onDomain) parts.push('domain=.' + ROOT);
    if (location.protocol === 'https:') parts.push('Secure');
    document.cookie = parts.join('; ');
  }

  // Google tag com modo de consentimento: nada é gravado até o visitante aceitar.
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  var choice = readConsent();
  var granted = choice === 'granted' ? 'granted' : 'denied';
  gtag('consent', 'default', {
    analytics_storage: granted,
    ad_storage: granted,
    ad_user_data: granted,
    ad_personalization: granted,
    wait_for_update: 500
  });
  gtag('js', new Date());
  gtag('config', GA_ID, { cookie_domain: onDomain ? ROOT : 'auto' });

  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
  document.head.appendChild(s);

  function updateConsent(value) {
    saveConsent(value);
    gtag('consent', 'update', {
      analytics_storage: value,
      ad_storage: value,
      ad_user_data: value,
      ad_personalization: value
    });
  }

  // Eventos de conversão: cliques em WhatsApp, piloto e abertura dos apps.
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var label = (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    if (/wa\.me|whatsapp\.com/i.test(href)) {
      var waText = decodeURIComponent(href);
      if (/piloto/i.test(waText)) {
        gtag('event', /estoque/i.test(waText) ? 'piloto_estoque' : 'piloto_carteira', { link_text: label, page_host: host });
      } else {
        gtag('event', 'contato_whatsapp', { link_text: label, page_host: host });
      }
      return;
    }
    if (/^mailto:/i.test(href)) {
      gtag('event', 'contato_email', { link_text: label, page_host: host });
      return;
    }
    var m = href.match(/^https?:\/\/([a-z0-9-]+)\.mfagentes\.com\.br/i);
    if (m && m[1] !== 'www' && m[1] !== host.split('.')[0]) {
      gtag('event', 'abrir_app', { app_name: m[1], link_text: label, page_host: host });
    }
  }, true);

  // Banner de cookies.
  function showBanner() {
    if (document.getElementById('mf-cookie-banner')) return;
    var css = document.createElement('style');
    css.textContent =
      '#mf-cookie-banner{position:fixed;left:16px;right:16px;bottom:16px;z-index:2147483000;max-width:560px;margin:0 auto;' +
      'background:#1D2721;color:#F3F5F1;border-radius:16px;padding:18px 20px;box-shadow:0 20px 50px -20px rgba(0,0,0,.5);' +
      'font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;display:flex;flex-wrap:wrap;gap:14px 18px;align-items:center}' +
      '#mf-cookie-banner p{margin:0;flex:1 1 260px}' +
      '#mf-cookie-banner .mf-cb-actions{display:flex;gap:10px;flex:0 0 auto}' +
      '#mf-cookie-banner button{font:inherit;font-weight:600;border-radius:999px;padding:9px 18px;cursor:pointer;border:2px solid #C9D8C5}' +
      '#mf-cookie-banner .mf-cb-accept{background:#C9D8C5;color:#1D2721}' +
      '#mf-cookie-banner .mf-cb-reject{background:transparent;color:#F3F5F1}' +
      '#mf-cookie-banner button:focus-visible{outline:3px solid #7E9C85;outline-offset:2px}' +
      '@media (max-width:480px){#mf-cookie-banner .mf-cb-actions{width:100%}#mf-cookie-banner button{flex:1}}';
    document.head.appendChild(css);

    var box = document.createElement('div');
    box.id = 'mf-cookie-banner';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-live', 'polite');
    box.setAttribute('aria-label', 'Preferências de cookies');
    box.innerHTML =
      '<p>Usamos cookies para entender como o site e os aplicativos são usados e melhorar nossos serviços. Você pode aceitar ou recusar.</p>' +
      '<div class="mf-cb-actions"><button type="button" class="mf-cb-reject">Recusar</button>' +
      '<button type="button" class="mf-cb-accept">Aceitar</button></div>';
    box.querySelector('.mf-cb-accept').addEventListener('click', function () { updateConsent('granted'); box.remove(); });
    box.querySelector('.mf-cb-reject').addEventListener('click', function () { updateConsent('denied'); box.remove(); });
    document.body.appendChild(box);
  }

  // Permite reabrir o banner, por exemplo num link "Preferências de cookies".
  window.mfCookiePreferences = showBanner;

  if (!choice) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', showBanner);
    } else {
      showBanner();
    }
  }
})();
