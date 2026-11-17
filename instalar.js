/*
 * MF Agentes: aviso "Instale o app no celular" para os apps.
 * Uso, no <head> de cada app:
 *   <script src="https://mfagentes.com.br/instalar.js" data-app="Nome do App" defer></script>
 *
 * Regras:
 *  - aparece só no celular, só para quem está logado e fora das telas de login/cadastro;
 *  - não aparece se o app já está instalado (aberto pela tela inicial);
 *  - espera o banner de cookies ser respondido, para não empilhar avisos;
 *  - "Agora não" esconde por 3 dias;
 *  - no Android com suporte, "Instalar" abre a instalação com um toque;
 *    nos demais casos (iPhone, Firefox etc.) abre o tutorial em mfagentes.com.br/instalar.
 * window.mfInstallPrompt() abre o aviso na hora (por exemplo, num item de menu).
 */
(function () {
  'use strict';
  if (window.__mfInstallLoaded) return;
  window.__mfInstallLoaded = true;

  var TUTORIAL = 'https://mfagentes.com.br/instalar/';
  var SNOOZE_KEY = 'mf_install_snooze';
  var DONE_KEY = 'mf_install_done';
  var SNOOZE_DAYS = 3;
  var AUTH_PATHS = /^\/(login|register|cadastro|entrar|signup|sign-in|forgot-password|reset-password|mfa|onboarding|privacidade|termos)(\/|$)/i;

  var script = document.currentScript;
  var appName = (script && script.getAttribute('data-app')) ||
    (document.querySelector('meta[name="application-name"]') || {}).content ||
    (document.title || 'app').split(/\s[—|–-]\s/)[0];
  appName = String(appName).trim().slice(0, 40) || 'app';

  var ua = navigator.userAgent || '';
  var isIOS = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var isAndroid = /Android/.test(ua);
  var isMobile = (isIOS || isAndroid) && window.matchMedia('(pointer: coarse)').matches;

  function store(key, value) {
    try {
      if (value === undefined) return window.localStorage.getItem(key);
      window.localStorage.setItem(key, value);
    } catch (e) { return null; }
  }

  function isStandalone() {
    return window.matchMedia('(display-mode: standalone)').matches ||
      window.matchMedia('(display-mode: fullscreen)').matches ||
      window.navigator.standalone === true;
  }

  function isSnoozed() {
    if (store(DONE_KEY) === '1') return true;
    var until = Number(store(SNOOZE_KEY) || 0);
    return until > Date.now();
  }

  function snooze() { store(SNOOZE_KEY, String(Date.now() + SNOOZE_DAYS * 864e5)); }

  function isLoggedIn() {
    try {
      return !!(localStorage.getItem('base44_access_token') || localStorage.getItem('token'));
    } catch (e) { return false; }
  }

  function track(name, params) {
    if (typeof window.gtag === 'function') {
      window.gtag('event', name, Object.assign({ app_name: appName, page_host: location.hostname }, params || {}));
    }
  }

  // Android: guarda o pedido de instalação para usar no botão.
  var deferredPrompt = null;
  window.addEventListener('beforeinstallprompt', function (e) {
    e.preventDefault();
    deferredPrompt = e;
  });
  window.addEventListener('appinstalled', function () {
    store(DONE_KEY, '1');
    track('app_instalado');
    hide();
  });

  function tutorialUrl() {
    var u = TUTORIAL + '?app=' + encodeURIComponent(appName) + '&volta=' + encodeURIComponent(location.origin + '/');
    return u + (isIOS ? '#iphone' : '#android');
  }

  // Sobe o aviso acima de uma barra de navegação fixa no rodapé do app, se houver.
  function bottomOffset() {
    try {
      var el = document.elementFromPoint(window.innerWidth / 2, window.innerHeight - 4);
      while (el && el !== document.body && el !== document.documentElement) {
        var pos = getComputedStyle(el).position;
        if (pos === 'fixed' || pos === 'sticky') {
          var r = el.getBoundingClientRect();
          if (r.height < window.innerHeight * 0.4) return Math.max(0, window.innerHeight - r.top) + 8;
          break;
        }
        el = el.parentElement;
      }
    } catch (e) {}
    return 12;
  }

  var box = null;

  function hide() {
    if (box) { box.remove(); box = null; }
  }

  function iconUrl() {
    var l = document.querySelector('link[rel="apple-touch-icon"]') || document.querySelector('link[rel~="icon"]');
    return l ? l.href : '';
  }

  function show() {
    if (box) return;
    if (!document.getElementById('mf-install-style')) {
      var css = document.createElement('style');
      css.id = 'mf-install-style';
      css.textContent =
        '#mf-install{position:fixed;left:12px;right:12px;z-index:2147482999;max-width:520px;margin:0 auto;' +
        'background:#1D2721;color:#F3F5F1;border-radius:18px;padding:14px 14px 14px 16px;box-shadow:0 18px 40px -16px rgba(0,0,0,.55);' +
        'font:15px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;display:grid;grid-template-columns:auto 1fr;gap:12px 12px;align-items:center;' +
        'animation:mfInstallIn .25s ease-out}' +
        '#mf-install img{width:44px;height:44px;border-radius:11px;object-fit:cover;background:#2E4236}' +
        '#mf-install strong{display:block;font-size:15.5px;margin-bottom:2px}' +
        '#mf-install span{color:#C9D8C5;font-size:13.5px}' +
        '#mf-install .mf-i-actions{grid-column:1/-1;display:flex;gap:10px}' +
        '#mf-install button{font:inherit;font-weight:600;border-radius:999px;padding:10px 16px;cursor:pointer;border:2px solid #C9D8C5;flex:1}' +
        '#mf-install .mf-i-go{background:#C9D8C5;color:#1D2721}' +
        '#mf-install .mf-i-later{background:transparent;color:#F3F5F1}' +
        '#mf-install button:focus-visible{outline:3px solid #7E9C85;outline-offset:2px}' +
        '@keyframes mfInstallIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}' +
        '@media (prefers-reduced-motion:reduce){#mf-install{animation:none}}';
      document.head.appendChild(css);
    }

    var canPrompt = !!deferredPrompt;
    var sub = isIOS
      ? 'No iPhone, os avisos do app só chegam com ele instalado.'
      : 'Abra direto da tela inicial, em tela cheia, como um aplicativo.';

    box = document.createElement('div');
    box.id = 'mf-install';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', 'Instalar o app no celular');
    box.style.bottom = 'calc(' + bottomOffset() + 'px + env(safe-area-inset-bottom, 0px))';

    var icon = iconUrl();
    box.innerHTML =
      (icon ? '<img alt="" src="' + icon.replace(/"/g, '&quot;') + '">' : '<div></div>') +
      '<div><strong></strong><span></span></div>' +
      '<div class="mf-i-actions"><button type="button" class="mf-i-later">Agora não</button>' +
      '<button type="button" class="mf-i-go"></button></div>';
    box.querySelector('strong').textContent = 'Instale o ' + appName + ' no celular';
    box.querySelector('span').textContent = sub;
    box.querySelector('.mf-i-go').textContent = canPrompt ? 'Instalar' : 'Como instalar';

    box.querySelector('.mf-i-later').addEventListener('click', function () {
      snooze();
      track('instalar_aviso', { acao: 'agora_nao' });
      hide();
    });

    box.querySelector('.mf-i-go').addEventListener('click', function () {
      if (deferredPrompt) {
        var p = deferredPrompt;
        deferredPrompt = null;
        track('instalar_aviso', { acao: 'instalar' });
        p.prompt();
        p.userChoice.then(function (choice) {
          if (choice && choice.outcome === 'accepted') store(DONE_KEY, '1');
          else snooze();
        }).catch(function () { snooze(); });
        hide();
      } else {
        snooze();
        track('instalar_aviso', { acao: 'tutorial' });
        window.open(tutorialUrl(), '_blank', 'noopener');
        hide();
      }
    });

    document.body.appendChild(box);
    track('instalar_aviso', { acao: 'exibido' });
  }

  window.mfInstallPrompt = function () { if (!isStandalone()) show(); };

  if (!isMobile || isStandalone()) return;

  // Confere as condições de tempos em tempos (os apps trocam de tela sem recarregar).
  var readySince = 0;
  var checks = 0;
  var timer = setInterval(function () {
    checks++;
    if (checks > 300 || box) { clearInterval(timer); return; } // até ~10 minutos
    var ok = !isStandalone() && !isSnoozed() && isLoggedIn() &&
      !AUTH_PATHS.test(location.pathname) &&
      !document.getElementById('mf-cookie-banner') &&
      document.visibilityState === 'visible';
    if (!ok) { readySince = 0; return; }
    if (!readySince) readySince = Date.now();
    if (Date.now() - readySince >= 4000) { clearInterval(timer); show(); }
  }, 2000);
})();
