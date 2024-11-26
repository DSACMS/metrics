// export function createNavigation() {
//     const toggleButton = document.querySelector(".usa-menu-btn");
//     const menu = document.querySelector(".usa-nav");
//     const menuIcon = document.querySelector(".menu-icon use");

//     toggleButton.addEventListener("click", () => {
//         const isOpen = menu.classList.toggle("is-open");
//         menuIcon.setAttribute(
//             "xlink:href",
//             isOpen ? "/assets/img/sprite.svg#close" : "/assets/img/sprite.svg#menu"
//         );
//     });
// }

// document.addEventListener("DOMContentLoaded", createNavigation);

export function createNavigation() {
    const toggleButton = document.querySelector(".usa-accordion__button");
    const closeButton = document.querySelector(".usa-nav__close");
    const menu = document.querySelector(".usa-nav");
    const menuIcon = document.querySelector(".usa-accordion__button svg use");

    if (toggleButton && closeButton && menu) {

        toggleButton.addEventListener("click", () => {
            const isOpen = menu.classList.toggle("is-visible");

            menuIcon.setAttribute(
                "xlink:href",
                isOpen ? "/assets/img/sprite.svg#close" : "/assets/img/sprite.svg#menu"
            );
        });
    } else {
        console.error("One or more elements is not found")
    }
}

document.addEventListener("DOMContentLoaded", createNavigation)