// RCCG Fuller's Field — shared site script
(function () {
  "use strict";

  // ---------- Mobile menu ----------
  var toggle = document.querySelector(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("menu-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
    document.querySelectorAll(".main-nav a").forEach(function (a) {
      a.addEventListener("click", function () {
        document.body.classList.remove("menu-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.setAttribute("aria-label", "Open menu");
      });
    });
  }

  // ---------- Hero photo slideshow ----------
  var show = document.querySelector("[data-slideshow]");
  if (show) {
    var pics = show.querySelectorAll("img");
    var dotsWrap = show.querySelector(".hero-dots");
    var cap = show.querySelector("figcaption");
    var idx = 0, timer;
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var dots = [];
    pics.forEach(function (img, i) {
      if (!dotsWrap) return;
      var b = document.createElement("button");
      b.type = "button";
      b.setAttribute("aria-label", "Show photo " + (i + 1));
      if (i === 0) b.className = "is-active";
      b.addEventListener("click", function () { go(i); restart(); });
      dotsWrap.appendChild(b); dots.push(b);
    });
    function go(i) {
      pics[idx].classList.remove("is-active"); if (dots[idx]) dots[idx].classList.remove("is-active");
      idx = i;
      pics[idx].classList.add("is-active"); if (dots[idx]) dots[idx].classList.add("is-active");
      if (cap && pics[idx].dataset.caption) cap.textContent = pics[idx].dataset.caption;
    }
    function restart() { clearInterval(timer); if (!reduce) timer = setInterval(function () { go((idx + 1) % pics.length); }, 6000); }
    restart();
  }

  // ---------- Countdown to the next gathering ----------
  var cd = document.querySelector(".countdown[data-countdown]");
  if (cd) {
    var gatherings = [
      { day: 0, h: 7,  m: 30, len: 120, name: "Sunday first service" },
      { day: 0, h: 9,  m: 30, len: 60,  name: "Sunday school" },
      { day: 0, h: 9,  m: 30, len: 90,  name: "Hope of Nations youth service" },
      { day: 0, h: 10, m: 30, len: 90,  name: "Sunday second service" },
      { day: 2, h: 18, m: 30, len: 75,  name: "Digging Deep Bible study" },
      { day: 4, h: 18, m: 30, len: 75,  name: "Faith Clinic prayer meeting" }
    ];
    var q = function (sel) { return cd.querySelector(sel); };
    var pad = function (n) { return (n < 10 ? "0" : "") + n; };
    var tick = function () {
      var now = new Date(), live = [], next = null;
      gatherings.forEach(function (g) {
        var d = new Date(now);
        d.setDate(now.getDate() + ((g.day - now.getDay() + 7) % 7));
        d.setHours(g.h, g.m, 0, 0);
        var end = new Date(d.getTime() + g.len * 60000);
        if (d <= now && now < end) live.push(g.name);
        if (d <= now) d.setDate(d.getDate() + 7);
        if (!next || d < next.d) next = { d: d, name: g.name };
      });
      // Same start time: name both (Sunday school and Hope of Nations)
      var sameTime = gatherings.filter(function (g) {
        var d = new Date(next.d); return g.day === d.getDay() && g.h === d.getHours() && g.m === d.getMinutes();
      }).map(function (g) { return g.name; });
      cd.classList.toggle("is-live", live.length > 0);
      q(".cd-name").textContent = live.length ? live.join(" and ") : sameTime.join(" and ");
      q(".cd-when").textContent = live.length ? "Happening now" : "Next gathering";
      var diff = Math.max(0, next.d - now);
      q("[data-u=d]").textContent = pad(Math.floor(diff / 864e5));
      q("[data-u=h]").textContent = pad(Math.floor(diff / 36e5) % 24);
      q("[data-u=m]").textContent = pad(Math.floor(diff / 6e4) % 60);
      q("[data-u=s]").textContent = pad(Math.floor(diff / 1e3) % 60);
    };
    tick(); setInterval(tick, 1000);
  }

  // ---------- Footer year ----------
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  var MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  var MON = MONTHS.map(function (m) { return m.slice(0, 3); });
  var DAYS = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];

  // ---------- "This week": mark the next gathering ----------
  var rows = document.querySelectorAll(".timetable li[data-day]");
  if (rows.length) {
    var now = new Date();
    var best = null;
    rows.forEach(function (row) {
      var day = +row.dataset.day;
      var hm = row.dataset.time.split(":");
      var d = new Date(now);
      d.setDate(now.getDate() + ((day - now.getDay() + 7) % 7));
      d.setHours(+hm[0], +hm[1], 0, 0);
      // Treat a gathering as "on now" for 90 minutes after it starts
      var end = new Date(d.getTime() + (+(row.dataset.len || 90)) * 60000);
      if (end <= now) d.setDate(d.getDate() + 7);
      var live = d <= now && now < end;
      if (!best || d < best.date) best = { row: row, date: d, live: live };
    });
    if (best) {
      best.row.classList.add("is-next");
      var flag = best.row.querySelector(".tt-flag");
      if (flag) {
        if (best.live) {
          flag.textContent = "Happening now";
        } else {
          var startOfToday = new Date(now); startOfToday.setHours(0, 0, 0, 0);
          var daysAway = Math.round((new Date(best.date).setHours(0, 0, 0, 0) - startOfToday) / 86400000);
          flag.textContent = daysAway === 0 ? "Next: today" : daysAway === 1 ? "Next: tomorrow" : "Next: in " + daysAway + " days";
        }
      }
    }
  }

  // ---------- Recurring monthly events ----------
  // nth weekday of a month (n = 1..5)
  function nthWeekday(year, month, weekday, n) {
    var first = new Date(year, month, 1);
    var offset = (weekday - first.getDay() + 7) % 7;
    return new Date(year, month, 1 + offset + (n - 1) * 7);
  }
  function nextOccurrence(rule, hour, min) {
    var now = new Date();
    // An event still counts as "next" until 3 hours after it starts
    var cutoff = now.getTime() - 3 * 3600000;
    for (var i = 0; i < 24; i++) {
      var d;
      if (rule.type === "nth") {
        var y = now.getFullYear() + Math.floor((now.getMonth() + i) / 12);
        var m = (now.getMonth() + i) % 12;
        d = nthWeekday(y, m, rule.weekday, rule.n);
      } else {
        d = new Date(now.getFullYear() + i, rule.month, rule.day);
      }
      d.setHours(hour, min, 0, 0);
      if (d.getTime() > cutoff) return d;
    }
    return null;
  }
  var list = document.querySelector(".event-list");
  var dated = [];
  document.querySelectorAll(".event[data-rule]").forEach(function (ev) {
    var r = ev.dataset.rule.split(",");
    var rule = r[0] === "nth"
      ? { type: "nth", n: +r[1], weekday: +r[2] }
      : { type: "date", month: +r[1], day: +r[2] };
    var hm = ev.dataset.time.split(":");
    var d = nextOccurrence(rule, +hm[0], +hm[1]);
    if (!d) return;
    dated.push({ el: ev, date: d });
    var dd = ev.querySelector(".event-date .d");
    var mm = ev.querySelector(".event-date .m");
    var full = ev.querySelector(".next-full");
    if (dd) dd.textContent = d.getDate();
    if (mm) mm.textContent = MON[d.getMonth()] + " " + d.getFullYear();
    if (full) full.textContent = DAYS[d.getDay()] + " " + d.getDate() + " " + MONTHS[d.getMonth()];
  });
  // Show the soonest event first
  if (list && dated.length) {
    dated.sort(function (a, b) { return a.date - b.date; })
      .forEach(function (x) { list.appendChild(x.el); });
    list.querySelectorAll(".event:not([data-rule])").forEach(function (el) { list.appendChild(el); });
  }

  // ---------- Floating Give button ----------
  var fab = document.querySelector(".fab-give");
  if (fab) {
    var onScroll = function () { fab.classList.toggle("is-visible", window.scrollY > 280); };
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  }

  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---------- Photo mosaic: tiles change picture one at a time ----------
  var tiles = Array.prototype.slice.call(document.querySelectorAll(".tile"));
  tiles.forEach(function (t) { var f = t.querySelector("img"); if (f) f.classList.add("is-on"); });
  if (tiles.length && !reduceMotion) {
    var last = -1;
    setInterval(function () {
      var i; do { i = Math.floor(Math.random() * tiles.length); } while (tiles.length > 1 && i === last);
      last = i;
      var imgs = tiles[i].querySelectorAll("img");
      if (imgs.length < 2) return;
      var cur = 0;
      imgs.forEach(function (im, k) { if (im.classList.contains("is-on")) cur = k; });
      var nxt = (cur + 1) % imgs.length;
      if (imgs[nxt].loading === "lazy") imgs[nxt].loading = "eager";
      imgs[cur].classList.remove("is-on"); imgs[nxt].classList.add("is-on");
    }, 2200);
  }
  // Moving strip: duplicate once for a seamless loop
  document.querySelectorAll(".strip-track").forEach(function (track) {
    Array.prototype.slice.call(track.children).forEach(function (img) {
      var c = img.cloneNode(true); c.alt = ""; c.setAttribute("aria-hidden", "true"); track.appendChild(c);
    });
  });

  // ---------- Event flyer + details dialog ----------
  var dlg = document.getElementById("evDialog");
  if (dlg && typeof dlg.showModal === "function") {
    var dImg = dlg.querySelector(".flyer img"), dTitle = dlg.querySelector("h3"),
        dWhen = dlg.querySelector(".when"), dDesc = dlg.querySelector(".desc");
    var openEvent = function (ev) {
      var img = ev.querySelector("img");
      dImg.src = img ? img.getAttribute("src") : "";
      dImg.alt = img ? img.alt : "";
      dTitle.textContent = ev.querySelector("h3").textContent;
      var w = ev.querySelector(".when");
      dWhen.textContent = w ? w.textContent : "";
      var more = ev.querySelector(".ev-more");
      var lead = ev.querySelector(".ev-lead");
      dDesc.innerHTML = (lead ? "<p>" + lead.innerHTML + "</p>" : "") + (more ? more.innerHTML : "");
      dlg.showModal();
      document.body.style.overflow = "hidden";
    };
    document.querySelectorAll(".event").forEach(function (ev) {
      ev.addEventListener("click", function (e) {
        if (e.target.closest("a")) return;
        openEvent(ev);
      });
      ev.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openEvent(ev); }
      });
    });
    var closeDlg = function () { dlg.close(); };
    dlg.querySelector(".ev-close").addEventListener("click", closeDlg);
    dlg.addEventListener("click", function (e) { if (e.target === dlg) closeDlg(); });
    dlg.addEventListener("close", function () { document.body.style.overflow = ""; });
  }

  // ---------- Photo viewer for ministry galleries ----------
  var pv = document.getElementById("photoDialog");
  if (pv && typeof pv.showModal === "function") {
    var pvImg = pv.querySelector("img");
    document.querySelectorAll(".gallery-grid button").forEach(function (b) {
      b.addEventListener("click", function () {
        var im = b.querySelector("img"); pvImg.src = im.getAttribute("src"); pvImg.alt = im.alt;
        pv.showModal(); document.body.style.overflow = "hidden";
      });
    });
    pv.querySelector(".ev-close").addEventListener("click", function () { pv.close(); });
    pv.addEventListener("click", function (e) { if (e.target === pv) pv.close(); });
    pv.addEventListener("close", function () { document.body.style.overflow = ""; });
  }

  // ---------- Copy account numbers ----------
  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function (resolve, reject) {
      var t = document.createElement("textarea");
      t.value = text; t.setAttribute("readonly", ""); t.style.position = "fixed"; t.style.opacity = "0";
      document.body.appendChild(t); t.select();
      try { document.execCommand("copy") ? resolve() : reject(); } catch (e) { reject(e); }
      document.body.removeChild(t);
    });
  }
  document.querySelectorAll(".copy-btn[data-copy]").forEach(function (btn) {
    var label = btn.querySelector(".lbl");
    var original = label ? label.textContent : "";
    btn.addEventListener("click", function () {
      copyText(btn.dataset.copy).then(function () {
        btn.classList.add("copied");
        if (label) label.textContent = "Copied";
        setTimeout(function () { btn.classList.remove("copied"); if (label) label.textContent = original; }, 2000);
      }, function () {
        if (label) label.textContent = "Press and hold to copy";
      });
    });
  });
})();
