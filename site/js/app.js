/* ==========================================================================
   College Conversations resource library: page behaviour.
   Everything here enhances HTML that already works without JavaScript.
   ========================================================================== */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const store = {
    get(k, d) { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* private mode: keep going */ } },
  };
  const scrollToEl = (el) => el && el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });

  /* ---------- Year ---------- */
  $$('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

  /* ---------- Scroll progress, roadmap rail ---------- */
  const bar = $('.progress');
  const stagesEl = $('.stages');
  const stageEls = $$('.stage');
  let ticking = false;
  const onScroll = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const h = document.documentElement;
      const p = h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight);
      if (bar) bar.style.setProperty('--p', p.toFixed(4));
      if (stagesEl) {
        const r = stagesEl.getBoundingClientRect();
        const mid = innerHeight * 0.55;
        const t = Math.min(1, Math.max(0, (mid - r.top) / r.height));
        stagesEl.style.setProperty('--rail', t.toFixed(4));
        stageEls.forEach((s) => {
          const n = s.querySelector('.stage__node').getBoundingClientRect();
          s.classList.toggle('is-reached', n.top < mid);
        });
      }
      ticking = false;
    });
  };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);
  onScroll();

  /* ---------- Nav: highlight the section in view ---------- */
  const navLinks = $$('.nav a');
  const navTargets = navLinks.map((a) => $(a.getAttribute('href'))).filter(Boolean);
  const navIO = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (!en.isIntersecting) return;
      navLinks.forEach((a) => a.classList.toggle('is-current', a.getAttribute('href') === '#' + en.target.id));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  navTargets.forEach((t) => navIO.observe(t));

  /* ---------- Ticker pause (WCAG 2.2.2) ---------- */
  const ticker = $('.ticker');
  const pauseBtn = $('.ticker__pause');
  if (ticker && pauseBtn) {
    pauseBtn.addEventListener('click', () => {
      const on = pauseBtn.getAttribute('aria-pressed') !== 'true';
      pauseBtn.setAttribute('aria-pressed', String(on));
      pauseBtn.setAttribute('aria-label', on ? 'Play the moving topics' : 'Pause the moving topics');
      ticker.classList.toggle('is-paused', on);
    });
  }

  /* ---------- Library ---------- */
  const libQ = $('#lib-q');
  const cards = $$('.res');
  const norm0 = (t) => t.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[\u2018\u2019]/g, "'").replace(/\s+/g, ' ');
  /* Search text is built from what the card shows, plus its category name */
  cards.forEach((c) => { c.dataset.search = norm0(c.textContent + ' ' + (c.closest('.cat')?.querySelector('.cat__title')?.textContent || '')); });
  $$('.term').forEach((t) => { t.dataset.search = norm0(t.textContent); });
  const cats = $$('.cat');
  const countEl = $('[data-lib-count]');
  const empty = $('.library .empty');
  const segBtns = $$('[data-filter-stage]');
  let stage = 'all';
  let collapsiblesReady = false;
  const norm = (s) => s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[\u2018\u2019]/g, "'").trim();
  const SYN = { money: 'aid', loans: 'loan', jobs: 'job', job: 'career', tests: 'test', textbooks: 'textbook', scholarship: 'scholarship', crisis: 'crisis', therapy: 'mental', anxiety: 'mental', depression: 'mental', suicide: '988', food: 'food', housing: 'housing', essays: 'writing', citation: 'citation', gpa: 'grade' };
  const filterLibrary = () => {
    const words = norm(libQ ? libQ.value : '').split(/\s+/).filter(Boolean).map((w) => SYN[w] || w.replace(/s$/, ''));
    let shown = 0;
    cards.forEach((c) => {
      const okStage = stage === 'all' || c.dataset.stages.split(' ').includes(stage);
      const hay = c.dataset.search;
      const okText = words.every((w) => hay.includes(w));
      const ok = okStage && okText;
      c.hidden = !ok;
      if (ok) shown++;
    });
    cats.forEach((cat) => {
      const n = cat.querySelectorAll('.res:not([hidden])').length;
      cat.hidden = n === 0;
      const idx = $(`[data-index-count="${cat.dataset.cat}"]`);
      if (idx) { idx.textContent = n; idx.closest('a').classList.toggle('is-empty', n === 0); }
    });
    if (countEl) countEl.textContent = shown;
    if (empty) empty.hidden = shown !== 0;
    if (collapsiblesReady) syncCollapsibles();
  };
  const setStage = (s) => {
    stage = s;
    segBtns.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.filterStage === s)));
    filterLibrary();
  };
  if (libQ) {
    libQ.addEventListener('input', filterLibrary);
    segBtns.forEach((b) => b.addEventListener('click', () => setStage(b.dataset.filterStage)));
    $$('.linkish[data-q]').forEach((b) => b.addEventListener('click', () => { libQ.value = b.dataset.q; filterLibrary(); libQ.focus(); }));
  }
  const runSearch = (q) => {
    if (!libQ) return;
    libQ.value = q;
    setStage('all');
    scrollToEl($('#library'));
  };
  const heroForm = $('.finder');
  if (heroForm) {
    heroForm.addEventListener('submit', (ev) => { ev.preventDefault(); runSearch($('#hero-q').value); });
  }
  $$('.qchip').forEach((a) => a.addEventListener('click', (ev) => { ev.preventDefault(); runSearch(a.dataset.q); }));
  $$('.path[data-stage]').forEach((a) => a.addEventListener('click', () => setStage(a.dataset.stage)));

  /* Library index: mark the category in view */
  const idxLinks = $$('[data-index]');
  if (idxLinks.length) {
    const catIO = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        idxLinks.forEach((a) => a.classList.toggle('is-current', a.dataset.index === en.target.dataset.cat));
      });
    }, { rootMargin: '-35% 0px -55% 0px' });
    cats.forEach((c) => catIO.observe(c));
  }

  /* ---------- Collapsible category lists ---------- */
  const collapsibles = [];
  $$('.more').forEach((btn) => {
    const list = document.getElementById(btn.getAttribute('aria-controls'));
    const box = list.closest('.cat') || list;
    const limit = () => (matchMedia('(min-width: 40rem)').matches ? (box === list ? 12 : 6) : (box === list ? 8 : 3));
    const label = btn.textContent;
    const state = { open: false };
    const sync = (searching) => {
      const items = [...list.children].filter((c) => !c.hidden);
      const needs = !searching && !state.open && items.length > limit();
      box.classList.toggle('is-collapsed', needs);
      btn.hidden = searching || list.children.length <= limit();
      btn.setAttribute('aria-expanded', String(state.open));
      btn.textContent = state.open ? 'Show fewer' : label;
    };
    btn.addEventListener('click', () => {
      state.open = !state.open;
      sync(false);
      if (!state.open) box.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    });
    collapsibles.push({ list, sync });
    sync(false);
  });
  const syncCollapsibles = () => {
    const searching = !!(libQ && libQ.value.trim()) || stage !== 'all';
    const tq = $('#term-q');
    collapsibles.forEach((c) => c.sync(c.list.id === 'terms-grid' ? !!(tq && tq.value.trim()) : searching));
  };
  addEventListener('resize', syncCollapsibles);
  collapsiblesReady = true;

  /* ---------- Decoder search ---------- */
  const termQ = $('#term-q');
  if (termQ) {
    const terms = $$('.term');
    const termEmpty = $('.terms-empty');
    termQ.addEventListener('input', () => {
      const words = norm(termQ.value).split(/\s+/).filter(Boolean);
      let n = 0;
      terms.forEach((t) => { const ok = words.every((w) => t.dataset.search.includes(w)); t.hidden = !ok; if (ok) n++; });
      termEmpty.hidden = n !== 0;
      syncCollapsibles();
    });
  }

  /* ---------- Roadmap checklist ---------- */
  const KEY = 'cc-roadmap-v1';
  const done = store.get(KEY, {});
  const boxes = $$('[data-task]');
  const total = boxes.length;
  const meterFill = $('.meter');
  const doneEl = $('[data-done]');
  const live = $('[data-meter-live]');
  const renderMeter = (announce) => {
    const n = boxes.filter((b) => b.checked).length;
    if (doneEl) doneEl.textContent = n;
    if (meterFill) meterFill.style.setProperty('--done', (n / total).toFixed(4));
    stageEls.forEach((s) => {
      const bs = $$('[data-task]', s);
      const k = bs.filter((b) => b.checked).length;
      const c = $(`[data-stage-count="${s.dataset.stageId}"] span`);
      if (c) c.textContent = k;
      s.classList.toggle('is-complete', k === bs.length);
    });
    if (announce && live) live.textContent = `${n} of ${total} done`;
  };
  boxes.forEach((b) => {
    b.checked = !!done[b.dataset.task];
    b.addEventListener('change', () => {
      if (b.checked) done[b.dataset.task] = 1; else delete done[b.dataset.task];
      store.set(KEY, done);
      renderMeter(true);
    });
  });
  const resetBtn = $('[data-reset]');
  if (resetBtn) resetBtn.addEventListener('click', () => {
    boxes.forEach((b) => { b.checked = false; });
    Object.keys(done).forEach((k) => delete done[k]);
    store.set(KEY, done);
    renderMeter(true);
  });
  renderMeter(false);

  /* ---------- Tabs (tools + video shelf), with arrow-key support ---------- */
  const wireTabs = (list) => {
    const tabs = $$('[role="tab"]', list);
    const select = (tab, focus) => {
      tabs.forEach((t) => {
        const on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        const panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
      if (focus) tab.focus();
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => select(t, false));
      t.addEventListener('keydown', (ev) => {
        const d = { ArrowRight: 1, ArrowLeft: -1, Home: -i, End: tabs.length - 1 - i }[ev.key];
        if (d === undefined) return;
        ev.preventDefault();
        select(tabs[(i + d + tabs.length) % tabs.length], true);
      });
    });
  };
  $$('[role="tablist"]').forEach(wireTabs);

  /* ---------- Credit hour calculator ---------- */
  const credits = $('#credits');
  if (credits) {
    const out = $('#credits-out');
    const degree = $('#degree');
    const earned = $('#earned');
    const status = $('[data-status]');
    const classes = $('[data-classes]');
    const finish = $('[data-finish]');
    const MAX = 21 * 3;
    const setBar = (k, v) => { $(`[data-bar="${k}"]`).style.setProperty('--w', (v / MAX).toFixed(4)); $(`[data-val="${k}"]`).textContent = `${v} hrs`; };
    const fmtYears = (sem) => { if (sem === 1) return 'half a year'; const y = sem / 2; return Number.isInteger(y) ? `${y} year${y === 1 ? '' : 's'}` : `${y.toFixed(1)} years`; };
    const calc = () => {
      const c = +credits.value;
      out.value = c; out.textContent = c;
      credits.style.setProperty('--fill', `${((c - 1) / 20) * 100}%`);
      setBar('class', c); setBar('out', c * 2); setBar('total', c * 3);
      let label = 'Full-time', level = 'full';
      if (c > 18) { label = 'Full-time, heavy load'; level = 'heavy'; }
      else if (c < 6) { label = 'Less than half-time'; level = 'less'; }
      else if (c < 12) { label = 'Half-time'; level = 'half'; }
      status.textContent = label; status.dataset.level = level;
      const k = Math.max(1, Math.round(c / 3));
      classes.textContent = c < 3 ? 'one short course' : `about ${k} class${k === 1 ? '' : 'es'}`;
      const need = Math.max(0, +degree.value - Math.max(0, +earned.value || 0));
      if (need === 0) {
        finish.innerHTML = 'You have enough credits for this degree on paper. <strong>Run your degree audit</strong> to confirm every requirement is met.';
      } else {
        const sem = Math.ceil(need / c);
        finish.innerHTML = `At ${c} credit${c === 1 ? '' : 's'} a term, your remaining ${need} credits take <strong>${sem} semester${sem === 1 ? '' : 's'}</strong>, about <strong>${fmtYears(sem)}</strong> of fall and spring terms.`;
      }
    };
    [credits, degree, earned].forEach((el) => el.addEventListener('input', calc));
    calc();
  }

  /* ---------- GPA calculator ---------- */
  const rowsEl = $('[data-gpa-rows]');
  const tpl = $('#gpa-row');
  if (rowsEl && tpl) {
    const gpaEl = $('[data-gpa]');
    const dial = $('[data-gpa-dial]');
    const meta = $('[data-gpa-meta]');
    const cum = $('[data-gpa-cum]');
    const pg = $('#prior-gpa');
    const pc = $('#prior-cr');
    const calc = () => {
      let cr = 0, qp = 0;
      $$('.gpa__row', rowsEl).forEach((r) => {
        const g = $('.gpa__gr', r).value;
        if (g === '') return;
        const c = +$('.gpa__cr', r).value;
        cr += c; qp += c * +g;
      });
      const gpa = cr ? qp / cr : 0;
      gpaEl.textContent = gpa.toFixed(2);
      dial.parentElement.style.setProperty('--g', 0);
      dial.style.setProperty('--g', (gpa / 4).toFixed(4));
      meta.textContent = cr ? `${cr} credit${cr === 1 ? '' : 's'} counted, ${qp.toFixed(1)} grade points` : 'Choose a grade for each course to see your GPA.';
      const p = parseFloat(pg.value), pcr = parseFloat(pc.value);
      if (!isNaN(p) && !isNaN(pcr) && pcr > 0 && p >= 0 && p <= 4.3) {
        const all = (p * pcr + qp) / (pcr + cr);
        cum.hidden = false;
        cum.innerHTML = `New cumulative GPA: <strong>${all.toFixed(2)}</strong> over ${pcr + cr} credits`;
      } else cum.hidden = true;
    };
    const addRow = (focus) => {
      const row = tpl.content.firstElementChild.cloneNode(true);
      $('.gpa__del', row).addEventListener('click', () => {
        const next = row.nextElementSibling || row.previousElementSibling;
        row.remove(); calc();
        if (next) $('.gpa__name', next).focus(); else $('[data-gpa-add]').focus();
      });
      rowsEl.appendChild(row);
      if (focus) $('.gpa__name', row).focus();
    };
    for (let i = 0; i < 4; i++) addRow(false);
    $('[data-gpa-add]').addEventListener('click', () => { addRow(true); calc(); });
    rowsEl.addEventListener('input', calc);
    rowsEl.addEventListener('change', calc);
    [pg, pc].forEach((el) => el.addEventListener('input', calc));
    calc();
  }

  /* ---------- Video player (youtube-nocookie, loads only on click) ---------- */
  const dlg = $('.player');
  if (dlg && typeof dlg.showModal === 'function') {
    const frame = $('[data-player-frame]');
    const title = $('[data-player-title]');
    let opener = null;
    const close = () => dlg.close();
    dlg.addEventListener('close', () => { frame.innerHTML = ''; if (opener) opener.focus(); });
    dlg.addEventListener('click', (ev) => { if (ev.target === dlg) close(); });
    $('.player__close').addEventListener('click', close);
    document.addEventListener('click', (ev) => {
      const a = ev.target.closest('[data-video]');
      if (!a || ev.button !== 0 || ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey) return;
      ev.preventDefault();
      opener = a;
      const id = a.dataset.video;
      title.textContent = a.dataset.title || 'Video';
      const f = document.createElement('iframe');
      f.src = `https://www.youtube-nocookie.com/embed/${encodeURIComponent(id)}?autoplay=1&rel=0&modestbranding=1`;
      f.title = a.dataset.title || 'YouTube video';
      f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      f.allowFullscreen = true;
      f.referrerPolicy = 'strict-origin-when-cross-origin';
      frame.replaceChildren(f);
      dlg.showModal();
    });
  }
  /* ---------- Deep link: ?q=fafsa pre-fills the library search ---------- */
  const initialQ = new URLSearchParams(location.search).get('q');
  if (initialQ && libQ) { libQ.value = initialQ; filterLibrary(); }
})();
