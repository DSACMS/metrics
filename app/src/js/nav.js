export function createNavigation() {
    const toggleButton = document.querySelector(".usa-accordion__button");
    const closeButton = document.querySelector(".usa-nav__close");
    const menu = document.querySelector(".usa-nav");
    const menuIcon = document.querySelector(".usa-accordion__button svg use");

    function toggleMenu(e) {
        e.preventDefault();
        const isOpen = menu.classList.toggle("is-visible");

        toggleButton.setAttribute("aria-expanded", isOpen ? "true" : "false");
        menuIcon.setAttribute(
            "href",
            isOpen ? "/assets/img/sprite.svg#close" : "/assets/img/sprite.svg#menu"
        );
    }

    function closeMenu() {
        if(menu.classList.contains("is-visible")) {
            menu.classList.remove("is-visible");
            toggleButton.setAttribute("aria-expanded", "false");
            menuIcon.setAttribute("href", "/assets/img/sprite.svg#menu");
        }
    }

    if(toggleButton && closeButton && menu) {
        toggleButton.addEventListener("click", toggleMenu);

        closeButton.addEventListener("click", (e) => {
            e.preventDefault();
            closeMenu();
        })

        document.addEventListener("click", (e) => {
            if(!menu.contains(e.target) && !toggleButton.contains(e.target)) {
                closeMenu();
            }
        });
    } else {
        console.error("Some elements are not found");
    }
}

document.addEventListener("DOMContentLoaded", createNavigation)