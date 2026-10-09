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
      var end = new Date(d.getTime() + 90 * 60000);
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
