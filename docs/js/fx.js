/* ==========================================================================
   fx.js: the signature motion layer (GSAP 3.13 + ScrollTrigger + Flip,
   Lenis 1.3.4, all self-hosted and pinned). Everything here is optional:
   the page works fully without it, and reduced-motion visitors get the
   settled layout with no pinning, spinning or smoothing.
   ========================================================================== */
(() => {
  if (!window.gsap) return;
  const { gsap } = window;
  gsap.registerPlugin(window.ScrollTrigger, window.Flip);
  const ST = window.ScrollTrigger;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const rnd = (i, k) => { const x = Math.sin(i * 12.9898 + k * 78.233) * 43758.5453; return x - Math.floor(x); };

  /* ---------- Smooth scrolling (desktop pointers only) ---------- */
  let lenis = null;
  if (!reduce && fine && window.Lenis) {
    lenis = new window.Lenis({ lerp: 0.11, smoothWheel: true, anchors: { offset: -84 } });
    lenis.on('scroll', ST.update);
    gsap.ticker.add((t) => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
    window.__lenis = lenis;
    document.addEventListener('toggle', () => lenis.resize(), true);
  }

  /* ---------- The arc of instruction cards ---------- */
  const arc = $('.arc');
  if (arc && !reduce) {
    const ring = $('.arc__ring', arc);
    const items = $$('.arc__item', arc);
    const n = items.length;
    const step = 360 / n;
    let r = 0;
    let angle = 0;
    let vel = 0;
    let auto = -6; // degrees per second
    let hover = false;
    let dragging = false;
    let moved = 0;
    let lastX = 0;
    let visible = true;
    arc.classList.add('is-3d');
    const layout = () => {
      const w = items[0].firstElementChild.offsetWidth;
      r = (w + 26) / (2 * Math.tan(Math.PI / n));
      items.forEach((it, i) => { it.style.transform = `rotateY(${i * step}deg) translateZ(${r}px)`; });
    };
    const render = () => {
      ring.style.transform = `translateZ(${-r}px) rotateX(-7deg) rotateY(${angle}deg)`;
      items.forEach((it, i) => {
        let a = ((i * step + angle) % 360 + 540) % 360 - 180; // -180..180, 0 = facing us
        const f = Math.cos((a * Math.PI) / 180);
        it.style.opacity = f > 0 ? (0.25 + 0.75 * f * f).toFixed(3) : '0';
        it.style.pointerEvents = f > 0.55 ? 'auto' : 'none';
        it.firstElementChild.tabIndex = f > 0.55 ? 0 : -1;
      });
    };
    layout();
    render();
    addEventListener('resize', () => { layout(); render(); });
    new IntersectionObserver(([en]) => { visible = en.isIntersecting; }).observe(arc);
    gsap.ticker.add((t, dt) => {
      if (!visible) return;
      const s = dt / 1000;
      if (!dragging) {
        vel *= Math.pow(0.04, s); // inertia decay
        const target = hover ? 0 : auto;
        angle += (vel + target) * s;
      }
      render();
    });
    arc.addEventListener('pointerenter', () => { hover = true; });
    arc.addEventListener('pointerleave', () => { hover = false; });
    arc.addEventListener('pointerdown', (e) => {
      dragging = true; moved = 0; lastX = e.clientX; vel = 0;
      arc.classList.add('is-dragging');
      arc.setPointerCapture(e.pointerId);
    });
    arc.addEventListener('pointermove', (e) => {
      if (!dragging) return;
      const dx = e.clientX - lastX;
      lastX = e.clientX;
      moved += Math.abs(dx);
      angle += dx * 0.22;
      vel = dx * 0.22 * 60;
    });
    const end = (e) => {
      if (!dragging) return;
      dragging = false;
      arc.classList.remove('is-dragging');
      if (arc.hasPointerCapture && arc.hasPointerCapture(e.pointerId)) arc.releasePointerCapture(e.pointerId);
      if (moved < 6) {
        /* a tap, not a drag: open the card under the pointer */
        const el = document.elementFromPoint(e.clientX, e.clientY);
        const card = el && el.closest('.arc__card');
        if (card) card.click();
      }
    };
    arc.addEventListener('pointerup', end);
    arc.addEventListener('pointercancel', end);
    /* Pointer taps are handled above; stop the browser's own click from
       firing a second search */
    arc.addEventListener('click', (e) => { if (e.isTrusted && e.detail > 0) e.stopPropagation(); }, true);
    /* Keyboard: bring the focused card to the front */
    items.forEach((it, i) => it.firstElementChild.addEventListener('focus', () => {
      const target = -i * step;
      const d = ((target - angle) % 360 + 540) % 360 - 180;
      gsap.to({ v: angle }, { v: angle + d, duration: 0.6, ease: 'power3.out', onUpdate() { angle = this.targets()[0].v; } });
    }));
  }

  /* ---------- Scroll-linked pieces ---------- */
  const mm = gsap.matchMedia();

  /* The rulebook: scattered jargon lines up into a numbered list */
  mm.add('(min-width: 60rem) and (prefers-reduced-motion: no-preference)', () => {
    const pin = $('.rulebook__pin');
    const rules = $$('.rule');
    if (!pin || !rules.length) return;
    const tl = gsap.timeline({
      scrollTrigger: { trigger: pin, start: 'top top', end: '+=120%', scrub: 0.9, pin: true, anticipatePin: 1, invalidateOnRefresh: true },
    });
    rules.forEach((el, i) => {
      tl.from(el, {
        x: () => {
          const b = el.getBoundingClientRect();
          const cx = b.left + b.width / 2;
          return (rnd(i, 1) * 0.9 + 0.05) * innerWidth - cx;
        },
        y: () => (rnd(i, 2) - 0.5) * innerHeight * 0.85,
        rotation: (rnd(i, 3) - 0.5) * 56,
        scale: 1.25 + rnd(i, 4) * 0.7,
        opacity: 0.75,
        borderBottomColor: 'rgba(0,0,0,0)',
        duration: 1,
        ease: 'power3.out',
      }, rnd(i, 5) * 0.35);
    });
    tl.from('.rulebook__intro', { opacity: 0, x: -60, duration: 0.6, ease: 'power2.out' }, 0.55);
    tl.to({}, { duration: 0.25 });
  });

  /* The roadmap: a big stage numeral that rolls to the stage in view */
  const now = $('.now');
  if (now && !reduce) {
    const stages = $$('.stage');
    const num = $('.now__n', now);
    const title = $('.now__t', now);
    let cur = -1;
    const show = (i) => {
      if (i === cur || i < 0) return;
      const dir = i > cur ? 1 : -1;
      cur = i;
      const s = stages[i];
      gsap.timeline()
        .to([num, title], { yPercent: -60 * dir, opacity: 0, duration: 0.22, ease: 'power2.in' })
        .add(() => { num.textContent = s.querySelector('.stage__node span').textContent; title.textContent = s.querySelector('.stage__title').textContent; })
        .fromTo([num, title], { yPercent: 60 * dir, opacity: 0 }, { yPercent: 0, opacity: 1, duration: 0.45, ease: 'power3.out', stagger: 0.05 });
    };
    stages.forEach((s, i) => ST.create({ trigger: s, start: 'top 55%', end: 'bottom 55%', onToggle: (self) => self.isActive && show(i) }));
  }
  /* Stage cards swing in as they arrive */
  mm.add('(min-width: 60rem) and (prefers-reduced-motion: no-preference)', () => {
    $$('.stage__card').forEach((c) => {
      gsap.fromTo(c, { x: 70, rotate: 1.5, opacity: 0 }, { x: 0, rotate: 0, opacity: 1, ease: 'power3.out', duration: 1, scrollTrigger: { trigger: c, start: 'top 88%', once: true } });
    });
  });

  /* Featured video opens up as it scrolls in */
  mm.add('(min-width: 56rem) and (prefers-reduced-motion: no-preference)', () => {
    gsap.fromTo('.vcard--feature .vcard__thumb', { scale: 0.78, rotate: -2 }, {
      scale: 1, rotate: 0, ease: 'none',
      scrollTrigger: { trigger: '.feature', start: 'top 90%', end: 'center 55%', scrub: 0.6 },
    });
    /* Catalog cards drift at slightly different speeds */
    $$('.catalog li').forEach((li, i) => {
      gsap.fromTo(li, { y: 30 + i * 22 }, { y: -10 - i * 8, ease: 'none', scrollTrigger: { trigger: '.proof-sec', start: 'top bottom', end: 'bottom top', scrub: true } });
    });
  });

  /* ---------- Draggable video strips ---------- */
  if (fine) {
    $$('.vgrid').forEach((g) => {
      let down = false; let x0 = 0; let s0 = 0; let movedX = 0;
      g.addEventListener('pointerdown', (e) => { if (e.pointerType !== 'mouse') return; down = true; x0 = e.clientX; s0 = g.scrollLeft; movedX = 0; });
      addEventListener('pointermove', (e) => {
        if (!down) return;
        movedX = e.clientX - x0;
        if (Math.abs(movedX) > 4) g.classList.add('is-dragging');
        g.scrollLeft = s0 - movedX;
      });
      addEventListener('pointerup', () => { if (!down) return; down = false; setTimeout(() => g.classList.remove('is-dragging'), 0); });
      g.addEventListener('click', (e) => { if (Math.abs(movedX) > 4) { e.preventDefault(); e.stopPropagation(); } }, true);
    });
  }

  /* ---------- Magnetic buttons + cursor label ---------- */
  if (fine && !reduce) {
    $$('[data-magnetic]').forEach((el) => {
      el.addEventListener('pointermove', (e) => {
        const b = el.getBoundingClientRect();
        gsap.to(el, { x: (e.clientX - b.left - b.width / 2) * 0.28, y: (e.clientY - b.top - b.height / 2) * 0.35, duration: 0.4, ease: 'power3.out' });
      });
      el.addEventListener('pointerleave', () => gsap.to(el, { x: 0, y: 0, duration: 0.7, ease: 'elastic.out(1, 0.4)' }));
    });
  }

  /* ---------- Pointer tilt ---------- */
  if (fine && !reduce) {
    $$('[data-tilt]').forEach((el) => {
      el.addEventListener('pointermove', (e) => {
        const b = el.getBoundingClientRect();
        const px = (e.clientX - b.left) / b.width - 0.5;
        const py = (e.clientY - b.top) / b.height - 0.5;
        gsap.to(el, { rotateY: px * 9, rotateX: -py * 9, transformPerspective: 900, duration: 0.5, ease: 'power3.out' });
      });
      el.addEventListener('pointerleave', () => gsap.to(el, { rotateY: 0, rotateX: 0, duration: 0.8, ease: 'elastic.out(1, 0.5)' }));
    });
    /* Hero glow drifts toward the pointer */
    const glow = $('.hero__glow');
    const hero = $('.hero');
    if (glow && hero) {
      const gx = gsap.quickTo(glow, 'x', { duration: 1.2, ease: 'power3.out' });
      hero.addEventListener('pointermove', (e) => gx((e.clientX / innerWidth - 0.5) * 160));
    }
  }

  /* Re-measure once fonts and images have settled */
  document.fonts && document.fonts.ready.then(() => ST.refresh());
  addEventListener('load', () => ST.refresh());
})();
