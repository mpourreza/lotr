(function () {
  "use strict";

  var REDUCE = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var html = document.documentElement;
  var canvas = document.getElementById("chronicle-veil");
  var progress = document.querySelector(".chronicle-progress");
  var hero = document.querySelector(".page__hero--overlay, .page__hero");
  var ticking = false;
  var particles = [];
  var ctx = null;
  var width = 0;
  var height = 0;
  var dpr = 1;
  var lastRealm = "";
  var time = 0;

  var REALMS = {
    origin: { a: "#1c3a2c", b: "#3a0f12", accent: "#c9a227", fog: "rgba(11,9,7,0.12)", kind: "ember", count: 46 },
    shire: { a: "#1e3d28", b: "#3a2a0c", accent: "#c9a227", fog: "rgba(28,58,44,0.18)", kind: "firefly", count: 56 },
    hobbits: { a: "#1e3d28", b: "#3a2a0c", accent: "#c9a227", fog: "rgba(28,58,44,0.18)", kind: "firefly", count: 56 },
    elves: { a: "#0c2430", b: "#1a2a3a", accent: "#b7d4d0", fog: "rgba(12,36,48,0.22)", kind: "star", count: 70 },
    men: { a: "#3a2410", b: "#1a120c", accent: "#d4a054", fog: "rgba(58,36,16,0.2)", kind: "dust", count: 48 },
    dwarves: { a: "#3a220c", b: "#1c1008", accent: "#d4923a", fog: "rgba(58,34,12,0.22)", kind: "spark", count: 52 },
    ents: { a: "#142414", b: "#0c1a0c", accent: "#7aa05a", fog: "rgba(20,36,20,0.22)", kind: "spore", count: 50 },
    maiar: { a: "#1a2238", b: "#2a2010", accent: "#e8e0c8", fog: "rgba(26,34,56,0.2)", kind: "mote", count: 60 },
    orcs: { a: "#2a0c0c", b: "#140808", accent: "#c45c3a", fog: "rgba(42,12,12,0.28)", kind: "ash", count: 64 },
    nazgul: { a: "#101018", b: "#08080c", accent: "#8a8696", fog: "rgba(8,8,12,0.35)", kind: "mist", count: 40 },
    beasts: { a: "#241428", b: "#120c18", accent: "#9a7ab8", fog: "rgba(36,20,40,0.22)", kind: "mote", count: 44 },
    enigmas: { a: "#1a2e28", b: "#2a2410", accent: "#d4c48a", fog: "rgba(26,46,40,0.2)", kind: "pollen", count: 48 },
    unmaking: { a: "#2a1c08", b: "#0b0907", accent: "#c9a227", fog: "rgba(11,9,7,0.16)", kind: "ember", count: 54 },
    other: { a: "#1c1814", b: "#0b0907", accent: "#c9a227", fog: "rgba(11,9,7,0.16)", kind: "dust", count: 36 }
  };

  function scenes() {
    return Array.prototype.slice.call(
      document.querySelectorAll(".page__hero--overlay[data-scene], .page__hero[data-scene], .journey-scene[data-scene], .kindred-chapter[data-scene], .kindred-intro[data-scene]")
    );
  }

  function applyRealm(id) {
    if (!id || id === lastRealm) return;
    lastRealm = id;
    html.setAttribute("data-realm", id);
    var spec = REALMS[id] || REALMS.origin;
    html.style.setProperty("--realm-a", spec.a);
    html.style.setProperty("--realm-b", spec.b);
    html.style.setProperty("--realm-accent", spec.accent);
    html.style.setProperty("--realm-fog", spec.fog);

    scenes().forEach(function (node) {
      var on = node.getAttribute("data-scene") === id;
      node.classList.toggle("is-active", on);
      if (on) node.classList.add("has-been-active");
    });

    document.querySelectorAll(".kindred-jump__link").forEach(function (link) {
      var href = link.getAttribute("href") || "";
      var hash = href.split("#")[1] || "";
      var on = hash === id;
      link.classList.toggle("is-current", on);
    });

    if (progress) {
      progress.querySelectorAll("a").forEach(function (link) {
        var on = link.getAttribute("data-scene") === id;
        link.classList.toggle("is-current", on);
        if (on) link.setAttribute("aria-current", "true");
        else link.removeAttribute("aria-current");
      });
    }

    if (!REDUCE && particles.length) restyleParticles(spec);
  }

  function restyleParticles(spec) {
    particles.forEach(function (p, i) {
      if (i % 3 === 0) {
        p.kind = spec.kind;
        p.life = 0;
      }
    });
  }

  function pickScene() {
    var nodes = scenes();
    if (!nodes.length) return;
    var marker = window.innerHeight * 0.38;
    var best = nodes[0];
    var bestDist = Infinity;
    nodes.forEach(function (node) {
      var rect = node.getBoundingClientRect();
      if (rect.bottom < 64 || rect.top > window.innerHeight) return;
      var focus = rect.top + Math.min(rect.height * 0.22, 140);
      var dist = Math.abs(focus - marker);
      if (dist < bestDist) {
        bestDist = dist;
        best = node;
      }
    });
    applyRealm(best.getAttribute("data-scene"));
  }

  function buildProgress() {
    if (!progress) return;
    var seen = {};
    var items = [];
    scenes().forEach(function (node) {
      var id = node.getAttribute("data-scene");
      if (!id || seen[id]) return;
      seen[id] = true;
      var label = (node.querySelector("h1, h2") || {}).textContent || id;
      items.push({ id: id, label: label.replace(/\s+/g, " ").trim() });
    });
    if (items.length < 2) return;
    progress.hidden = false;
    progress.innerHTML = items.map(function (item) {
      var href = nodeHref(item.id);
      return '<a href="' + href + '" data-scene="' + item.id + '" title="' + escapeHtml(item.label) + '"><span class="visually-hidden">' + escapeHtml(item.label) + "</span></a>";
    }).join("");
  }

  function nodeHref(id) {
    var el = document.getElementById(id) || document.getElementById("scene-" + id);
    if (el && el.id) return "#" + el.id;
    return "#" + id;
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, function (ch) {
      return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[ch];
    });
  }

  function onScroll() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      pickScene();
      ticking = false;
    });
  }

  function resizeCanvas() {
    if (!canvas || !ctx) return;
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = Math.floor(width * dpr);
    canvas.height = Math.floor(height * dpr);
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function hexToRgb(hex) {
    var h = hex.replace("#", "");
    return [
      parseInt(h.slice(0, 2), 16),
      parseInt(h.slice(2, 4), 16),
      parseInt(h.slice(4, 6), 16)
    ];
  }

  function makeParticle(kind) {
    return {
      x: Math.random() * width,
      y: Math.random() * height,
      r: 0.6 + Math.random() * 2.4,
      vx: (Math.random() - 0.5) * 0.35,
      vy: (Math.random() - 0.5) * 0.35,
      o: 0.15 + Math.random() * 0.55,
      phase: Math.random() * Math.PI * 2,
      life: Math.random(),
      kind: kind
    };
  }

  function seedParticles(spec) {
    particles = [];
    var n = spec.count;
    for (var i = 0; i < n; i += 1) particles.push(makeParticle(spec.kind));
  }

  function wrap(p) {
    if (p.x < -12) p.x = width + 12;
    if (p.x > width + 12) p.x = -12;
    if (p.y < -12) p.y = height + 12;
    if (p.y > height + 12) p.y = -12;
  }

  function stepParticle(p, spec) {
    p.phase += 0.012;
    p.life += 0.002;
    switch (p.kind) {
      case "firefly":
        p.x += Math.sin(p.phase) * 0.28 + p.vx;
        p.y += Math.cos(p.phase * 0.8) * 0.22 + p.vy * 0.3;
        p.o = 0.2 + Math.abs(Math.sin(p.phase * 2)) * 0.7;
        break;
      case "star":
        p.x += p.vx * 0.15;
        p.y += p.vy * 0.15;
        p.o = 0.12 + Math.abs(Math.sin(p.phase * 3)) * 0.8;
        break;
      case "ember":
        p.y -= 0.35 + p.r * 0.12;
        p.x += Math.sin(p.phase) * 0.2;
        p.o = 0.15 + (1 - (p.life % 1)) * 0.55;
        break;
      case "ash":
        p.y += 0.45 + p.r * 0.08;
        p.x += Math.sin(p.phase * 0.7) * 0.35;
        p.o = 0.12 + (1 - (p.life % 1)) * 0.4;
        break;
      case "spark":
        p.y -= 0.7 + p.r * 0.2;
        p.x += p.vx * 0.8;
        p.o = Math.max(0, 0.8 - (p.life % 1));
        break;
      case "spore":
        p.x += Math.sin(p.phase) * 0.18;
        p.y -= 0.12;
        p.o = 0.18 + Math.abs(Math.sin(p.phase)) * 0.4;
        break;
      case "mist":
        p.x += p.vx * 0.4;
        p.y += p.vy * 0.2;
        p.r = 6 + Math.sin(p.phase) * 3;
        p.o = 0.04 + Math.abs(Math.sin(p.phase)) * 0.08;
        break;
      case "pollen":
        p.x += Math.sin(p.phase) * 0.25 + 0.08;
        p.y += Math.cos(p.phase * 0.6) * 0.18;
        p.o = 0.2 + Math.abs(Math.sin(p.phase * 1.4)) * 0.45;
        break;
      case "mote":
        p.x += p.vx * 0.45;
        p.y += p.vy * 0.45;
        p.o = 0.16 + Math.abs(Math.sin(p.phase * 1.6)) * 0.5;
        break;
      default:
        p.x += p.vx * 0.3;
        p.y += p.vy * 0.2;
        p.o = 0.18 + Math.abs(Math.sin(p.phase)) * 0.3;
    }
    wrap(p);
  }

  function draw() {
    if (!ctx) return;
    time += 1;
    ctx.clearRect(0, 0, width, height);
    var spec = REALMS[lastRealm] || REALMS.origin;
    var rgb = hexToRgb(spec.accent);
    particles.forEach(function (p) {
      stepParticle(p, spec);
      ctx.beginPath();
      ctx.fillStyle = "rgba(" + rgb[0] + "," + rgb[1] + "," + rgb[2] + "," + p.o + ")";
      if (p.kind === "mist") {
        ctx.arc(p.x, p.y, p.r * 4, 0, Math.PI * 2);
      } else if (p.kind === "star") {
        ctx.arc(p.x, p.y, p.r * 0.7, 0, Math.PI * 2);
      } else {
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      }
      ctx.fill();
    });
    window.requestAnimationFrame(draw);
  }

  function initCanvas() {
    if (REDUCE || !canvas || !canvas.getContext) return;
    ctx = canvas.getContext("2d");
    resizeCanvas();
    seedParticles(REALMS.origin);
    window.addEventListener("resize", function () {
      resizeCanvas();
    }, { passive: true });
    window.requestAnimationFrame(draw);
  }

  if (!document.querySelector(".chronicle-atmosphere")) return;

  if (hero && !hero.getAttribute("data-scene")) {
    hero.setAttribute("data-scene", "origin");
    if (!hero.id) hero.id = "scene-origin";
  }

  html.classList.add("has-chronicle-scroll");
  buildProgress();
  initCanvas();
  pickScene();
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
})();
