// The theme scrolls the active sidebar entry into view, which also scrolls the window
// past the (non-sticky) Cyberduck header. Keep the page at the top on load unless
// the URL targets an anchor.
window.addEventListener("load", function () {
  if (!window.location.hash) {
    window.scrollTo(0, 0);
  }
});

// Hamburger menu for the header navigation on small screens
document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector(".cd-toggle");
  var nav = document.getElementById("cd-nav");
  if (!toggle || !nav) {
    return;
  }
  toggle.addEventListener("click", function () {
    var open = nav.classList.toggle("cd-nav-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });
});
