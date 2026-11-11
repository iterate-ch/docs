// The theme scrolls the active sidebar entry into view, which also scrolls the window
// past the (non-sticky) Cyberduck header. Keep the page at the top on load unless
// the URL targets an anchor.
window.addEventListener("load", function () {
  if (!window.location.hash) {
    window.scrollTo(0, 0);
  }
});
