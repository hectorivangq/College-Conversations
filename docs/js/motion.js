/* ==========================================================================
   motion.js: dependency-free motion layer for the starter.
   Covers ~90% of what a small-business site needs: scroll reveals with
   stagger, masked headline reveals, image unmasks, count-ups, header state,
   light parallax, SVG line draws, mobile nav. Reach for GSAP + ScrollTrigger
   (pinned exact version) only for pinned/scrubbed sequences or timelines.
   ========================================================================== */
(() => {
  const root = document.documentElement;
  root.classList.add('js');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Split [data-split] headings into masked words. Screen readers get the
     original sentence via aria-label; the word spans are hidden from them. */
  document.querySelectorAll('[data-split]').forEach((el) => {
    const text = el.textContent.trim().replace(/\s+/g, ' ');
    const esc = (t) => t.replace(/&/g, '&amp;').replace(/</g, '&lt;');
    let i = parseInt(el.dataset.splitOffset || '0', 10);
    /* Walk the heading: text becomes masked words, inline elements (a grey
       phrase, an italic accent) keep their tag and class around their words,
       and SVG is kept whole. */
    const render = (node) => {
      if (node.nodeType === 3) {
        return node.textContent.split(/(\s+)/).map((part) => {
          if (!part) return '';
          if (/^\s+$/.test(part)) return ' ';
          return `<span class="w" aria-hidden="true"><span style="--i:${i++}">${esc(part)}</span></span>`;
        }).join('');
      }
      if (node.nodeType !== 1) return '';
      const tag = node.tagName.toLowerCase();
      if (tag === 'svg') return node.outerHTML;
      const cls = node.getAttribute('class');
      return `<${tag}${cls ? ` class="${cls}"` : ''} aria-hidden="true">${[...node.childNodes].map(render).join('')}</${tag}>`;
    };
    const html = [...el.childNodes].map(render).join('');
    /* The sentence stays readable to screen readers as real (visually hidden)
       text; aria-label is unreliable on non-heading elements. */
    el.innerHTML = `<span class="visually-hidden">${esc(text)}</span>${html}`;
    el.setAttribute('data-reveal', '');
  });

  /* Stagger: children of [data-stagger] reveal one after another */
  document.querySelectorAll('[data-stagger]').forEach((group) => {
    [...group.children].forEach((child, i) => {
      child.setAttribute('data-reveal', '');
      child.style.setProperty('--i', i);
    });
  });

  /* SVG line length for draw-on */
  document.querySelectorAll('.draw path').forEach((p) => {
    if (p.getTotalLength) p.closest('.draw').style.setProperty('--len', Math.ceil(p.getTotalLength()));
  });

  /* Count-up numbers: <span data-count="120" data-suffix="+">120+</span>.
     The real number is in the HTML, so no-JS and reduced motion see it. */
  const countUp = (el) => {
    const end = parseFloat(el.dataset.count);
    const decimals = (el.dataset.count.split('.')[1] || '').length;
    const suffix = el.dataset.suffix || '';
    const prefix = el.dataset.prefix || '';
    if (reduce) return;
    const dur = 1600;
    const t0 = performance.now();
    const tick = (now) => {
      const t = Math.min((now - t0) / dur, 1);
      const eased = 1 - Math.pow(1 - t, 4);
      const v = end * eased;
      el.textContent = prefix + (decimals ? v.toFixed(decimals) : Math.round(v).toLocaleString('en-US')) + suffix;
      if (t < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  /* Masked headings drop their word masks once every word has finished
     rising (transitionend, not a timer: a background tab pauses transitions
     but not timers, and an early unmask would let moving words spill out). */
  const markDone = (el) => {
    if (reduce) { el.classList.add('is-done'); return; }
    const spans = [...el.querySelectorAll('.w > span')];
    let left = spans.length;
    const finish = () => el.classList.add('is-done');
    if (!left) return finish();
    spans.forEach((sp) => sp.addEventListener('transitionend', (e) => {
      if (e.propertyName === 'transform' && --left === 0) finish();
    }, { once: false }));
    /* Safety net: if transitions never fire, unmask once nothing is moving */
    const check = () => {
      if (el.classList.contains('is-done')) return;
      if (spans.every((sp) => getComputedStyle(sp).transform === 'none')) finish();
      else setTimeout(check, 1000);
    };
    setTimeout(check, 3000);
  };

  /* One observer for everything that reveals */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      el.classList.add('is-in');
      if (el.hasAttribute('data-split')) markDone(el);
      if (el.dataset.count) countUp(el);
      io.unobserve(el);
    });
  }, { rootMargin: '0px 0px -12% 0px', threshold: 0.15 });

  document.querySelectorAll('[data-reveal], [data-count]').forEach((el) => {
    if (reduce) { el.classList.add('is-in'); if (el.hasAttribute('data-split')) markDone(el); }
    else io.observe(el);
  });

  /* Failsafe: nothing above the fold may stay hidden if the observer is late
     (background tab, slow device). */
  window.addEventListener('load', () => setTimeout(() => {
    document.querySelectorAll('[data-reveal]:not(.is-in)').forEach((el) => {
      if (el.getBoundingClientRect().top < window.innerHeight) { el.classList.add('is-in'); if (el.hasAttribute('data-split')) markDone(el); io.unobserve(el); }
    });
  }, 1200));

  /* Header: compact + hairline once the page scrolls */
  const header = document.querySelector('.site-header');
  const parallax = reduce ? [] : [...document.querySelectorAll('[data-parallax]')];
  let ticking = false;
  const onScroll = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const y = window.scrollY;
      if (header) header.classList.toggle('is-scrolled', y > 8);
      parallax.forEach((el) => {
        const r = el.getBoundingClientRect();
        const speed = parseFloat(el.dataset.parallax) || 0.08;
        const offset = (r.top + r.height / 2 - window.innerHeight / 2) * -speed;
        el.style.transform = `translate3d(0, ${offset.toFixed(1)}px, 0)`;
      });
      ticking = false;
    });
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Mobile nav */
  const toggle = document.querySelector('.nav-toggle');
  const panel = document.getElementById('mobile-nav');
  if (toggle && panel) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      panel.hidden = open;
    });
    panel.addEventListener('click', (e) => {
      if (e.target.closest('a')) { toggle.setAttribute('aria-expanded', 'false'); panel.hidden = true; }
    });
  }
})();
