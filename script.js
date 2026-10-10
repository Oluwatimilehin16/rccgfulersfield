// RCCG Fuller's Field: shared site script
(function () {
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---------- Header: transparent over the hero, white once scrolled ----------
  var header = document.getElementById("siteHeader");
  var fab = document.querySelector(".fab-give");
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("scrolled", y > 40);
    if (fab) fab.classList.toggle("is-visible", y > 320);
  }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  // ---------- Mobile menu ----------
  var burger = document.getElementById("hamburgerBtn");
  var nav = document.getElementById("mainNav");
  if (burger && nav) {
    var setMenu = function (open) {
      nav.classList.toggle("mobile-open", open);
      burger.classList.toggle("active", open);
      document.body.classList.toggle("menu-open", open);
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    };
    burger.addEventListener("click", function () { setMenu(!nav.classList.contains("mobile-open")); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && nav.classList.contains("mobile-open")) setMenu(false); });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function (e) {
        var li = a.parentElement;
        if (li && li.classList.contains("has-mega") && window.innerWidth <= 900) {
          e.preventDefault();
          a.setAttribute("aria-expanded", li.classList.toggle("mega-open") ? "true" : "false");
          return;
        }
        setMenu(false);
      });
    });
  }

  // ---------- Hero slideshow ----------
  var slides = document.querySelectorAll(".hero-slide");
  var dots = document.querySelectorAll("#heroDots button");
  if (slides.length > 1) {
    var cur = 0, timer;
    var show = function (i) {
      slides[cur].classList.remove("active"); if (dots[cur]) dots[cur].classList.remove("active");
      cur = i;
      slides[cur].classList.add("active"); if (dots[cur]) dots[cur].classList.add("active");
    };
    var start = function () { clearInterval(timer); if (!reduce) timer = setInterval(function () { show((cur + 1) % slides.length); }, 7000); };
    dots.forEach(function (d) { d.addEventListener("click", function () { show(+d.dataset.i); start(); }); });
    start();
  }

  // ---------- Countdown to the next gathering ----------
  var cd = document.querySelector("[data-countdown]");
  if (cd) {
    var gatherings = [
      { day: 0, h: 7,  m: 30, len: 120, name: "Sunday · First Service" },
      { day: 0, h: 9,  m: 30, len: 90,  name: "Sunday School & Hope of Nations" },
      { day: 0, h: 10, m: 30, len: 90,  name: "Sunday · Second Service" },
      { day: 2, h: 18, m: 30, len: 75,  name: "Tuesday · Digging Deep" },
      { day: 4, h: 18, m: 30, len: 75,  name: "Thursday · Faith Clinic" }
    ];
    var pad = function (n) { return (n < 10 ? "0" : "") + n; };
    var q = function (s) { return cd.querySelector(s); };
    var tick = function () {
      var now = new Date(), next = null, live = null;
      gatherings.forEach(function (g) {
        var d = new Date(now);
        d.setDate(now.getDate() + ((g.day - now.getDay() + 7) % 7));
        d.setHours(g.h, g.m, 0, 0);
        var end = new Date(d.getTime() + g.len * 60000);
        if (d <= now && now < end && !live) live = g.name;
        if (d <= now) d.setDate(d.getDate() + 7);
        if (!next || d < next.d) next = { d: d, name: g.name };
      });
      cd.classList.toggle("is-live", !!live);
      q(".cd-name").textContent = live || next.name;
      q(".cd-eyebrow").textContent = live ? "Happening now" : "Next gathering";
      var diff = Math.max(0, next.d - now);
      q("[data-u=d]").textContent = pad(Math.floor(diff / 864e5));
      q("[data-u=h]").textContent = pad(Math.floor(diff / 36e5) % 24);
      q("[data-u=m]").textContent = pad(Math.floor(diff / 6e4) % 60);
      q("[data-u=s]").textContent = pad(Math.floor(diff / 1e3) % 60);
    };
    tick(); setInterval(tick, 1000);
  }

  // ---------- Recurring events: work out the next date ----------
  var MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  var DAYS = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
  function nthWeekday(y, m, wd, n) { var f = new Date(y, m, 1); return new Date(y, m, 1 + ((wd - f.getDay() + 7) % 7) + (n - 1) * 7); }
  function nextOcc(rule, h, mi) {
    var now = new Date(), cut = now.getTime() - 3 * 3600000;
    for (var i = 0; i < 24; i++) {
      var d;
      if (rule[0] === "nth") { var t = now.getMonth() + i; d = nthWeekday(now.getFullYear() + Math.floor(t / 12), t % 12, +rule[2], +rule[1]); }
      else d = new Date(now.getFullYear() + i, +rule[1], +rule[2]);
      d.setHours(h, mi, 0, 0);
      if (d.getTime() > cut) return d;
    }
    return null;
  }
  document.querySelectorAll(".ev-list").forEach(function (list) {
    var dated = [];
    list.querySelectorAll(".ev-row[data-rule]").forEach(function (ev) {
      var hm = ev.dataset.time.split(":");
      var d = nextOcc(ev.dataset.rule.split(","), +hm[0], +hm[1]);
      if (!d) return;
      dated.push({ el: ev, d: d });
      var dd = ev.querySelector(".event-date .d"), mm = ev.querySelector(".event-date .m"), full = ev.querySelector(".next-full");
      if (dd) dd.textContent = d.getDate();
      if (mm) mm.textContent = MONTHS[d.getMonth()].slice(0, 3) + " " + d.getFullYear();
      if (full) full.textContent = DAYS[d.getDay()] + " " + d.getDate() + " " + MONTHS[d.getMonth()];
    });
    dated.sort(function (x, y) { return x.d - y.d; }).forEach(function (x) { list.appendChild(x.el); });
    list.querySelectorAll(".ev-row:not([data-rule])").forEach(function (el) { list.appendChild(el); });
    var limit = +list.dataset.limit || 0;
    if (limit) Array.prototype.slice.call(list.children).forEach(function (el, i) { if (i >= limit) el.remove(); });
  });

  // ---------- Event flyer dialog ----------
  var dlg = document.getElementById("evDialog");
  if (dlg && typeof dlg.showModal === "function") {
    var dImg = dlg.querySelector(".flyer img"), dT = dlg.querySelector("h3"), dW = dlg.querySelector(".when"), dD = dlg.querySelector(".desc");
    var open = function (ev) {
      var img = ev.querySelector("img");
      dImg.src = ev.dataset.flyer || (img ? img.getAttribute("src") : "");
      dImg.alt = img ? img.alt : "";
      dT.textContent = ev.querySelector("h3").textContent;
      var w = ev.querySelector(".ev-when"); dW.textContent = w ? w.textContent : "";
      var lead = ev.querySelector(".ev-lead"), more = ev.querySelector(".ev-more");
      dD.innerHTML = (lead ? "<p>" + lead.innerHTML + "</p>" : "") + (more ? more.innerHTML : "");
      dlg.showModal(); document.body.style.overflow = "hidden";
    };
    document.querySelectorAll(".ev-row").forEach(function (ev) {
      ev.addEventListener("click", function () { open(ev); });
      ev.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(ev); } });
    });
    dlg.querySelector(".ev-close").addEventListener("click", function () { dlg.close(); });
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
    dlg.addEventListener("close", function () { document.body.style.overflow = ""; });
  }

  // ---------- Photo viewer ----------
  var pv = document.getElementById("photoDialog");
  if (pv && typeof pv.showModal === "function") {
    var pImg = pv.querySelector("img");
    document.querySelectorAll(".photo-grid button").forEach(function (b) {
      b.addEventListener("click", function () { var im = b.querySelector("img"); pImg.src = im.getAttribute("src"); pImg.alt = im.alt; pv.showModal(); document.body.style.overflow = "hidden"; });
    });
    pv.querySelector(".ev-close").addEventListener("click", function () { pv.close(); });
    pv.addEventListener("click", function (e) { if (e.target === pv) pv.close(); });
    pv.addEventListener("close", function () { document.body.style.overflow = ""; });
  }

  // ---------- Gallery marquee: duplicate once for a seamless loop ----------
  var mq = document.getElementById("marquee");
  if (mq) Array.prototype.slice.call(mq.children).forEach(function (n) { var c = n.cloneNode(true); c.setAttribute("aria-hidden", "true"); var i = c.querySelector("img"); if (i) i.alt = ""; mq.appendChild(c); });

  // ---------- Reveal on scroll ----------
  var rev = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in-view"); io.unobserve(e.target); } }); }, { threshold: 0.06, rootMargin: "0px 0px -40px 0px" });
    rev.forEach(function (el) { io.observe(el); });
  } else rev.forEach(function (el) { el.classList.add("in-view"); });

  // ---------- Copy buttons ----------
  function copyText(t) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(t);
    return new Promise(function (res, rej) {
      var a = document.createElement("textarea"); a.value = t; a.style.position = "fixed"; a.style.opacity = "0";
      document.body.appendChild(a); a.select();
      try { document.execCommand("copy") ? res() : rej(); } catch (e) { rej(e); }
      document.body.removeChild(a);
    });
  }
  document.querySelectorAll(".copy-btn[data-copy]").forEach(function (b) {
    var l = b.querySelector(".lbl"), o = l ? l.textContent : "";
    b.addEventListener("click", function () {
      copyText(b.dataset.copy).then(function () { b.classList.add("copied"); if (l) l.textContent = "Copied"; setTimeout(function () { b.classList.remove("copied"); if (l) l.textContent = o; }, 2000); },
        function () { if (l) l.textContent = "Press and hold to copy"; });
    });
  });

  // ---------- Footer year ----------
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
