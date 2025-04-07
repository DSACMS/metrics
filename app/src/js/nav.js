export function createNavigation() {
    const menuButton = document.querySelector(".usa-menu-btn");
    const closeButton = document.querySelector(".usa-nav__close");
    const menu = document.querySelector(".usa-nav");

    function toggleMenu() {
        const isOpen = menu.classList.toggle("is-visible");
        menuButton.setAttribute("aria-expanded", isOpen ? "true" : "false");
    }

    function closeMenu() {
        menu.classList.remove("is-visible");
        menuButton.setAttribute("aria-expanded", "false");
    }

    if(menuButton && closeButton && menu) {
        menuButton.addEventListener("click", toggleMenu);
        closeButton.addEventListener("click", closeMenu);
    }
}

document.addEventListener("DOMContentLoaded", createNavigation)