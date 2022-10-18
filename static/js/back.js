history.pushState(null, null, location.href);
window.addEventListener("popstate", (e) => {
  history.go(1);
});
