document.addEventListener("DOMContentLoaded", function () {
    // Disable scroll preservation for the sidebar
    var nav = document.querySelector(".wy-side-nav-search");
    if (nav) {
        nav.style.scrollBehavior = "auto";
    }
});