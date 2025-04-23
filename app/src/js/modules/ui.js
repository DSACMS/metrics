import { baseurl } from "./data";

export function updateFilterMenuState() {
    const filterButtons = document.querySelectorAll(".usa-accordion__button");
    const isMobile = window.innerWidth < 768;

    filterButtons.forEach((button) => {
      const contentId = button.getAttribute("aria-controls");
      const content = document.getElementById(contentId);
      const icon = button.querySelector("svg use");

      if(isMobile) {
        button.setAttribute("aria-expanded", "false");
        content.setAttribute("hidden", "true");
        icon.setAttribute("href", `${baseurl}/assets/img/sprite.svg#expand_more`);
      } else {
        button.setAttribute("aria-expanded", "true");
        content.removeAttribute("hidden");
        icon.setAttribute("href", `${baseurl}/assets/img/sprite.svg#expand_less`);
      }
    });
  }

//   updateFilterMenuState()

//   window.addEventListener("resize", updateFilterMenuState)

//   document.querySelectorAll(".usa-accordion__button").forEach((button) => {
//     button.addEventListener("click", () => {
//       const expanded = button.getAttribute("aria-expanded");
//       const content = document.getElementById(button.getAttribute("id"));
//       const icon = button.querySelector("svg use");
      
//       if(expanded === 'false') {
//         content.removeAttribute("hidden");
//         icon.setAttribute("href", `${baseurl}/assets/img/sprite.svg#expand_less`);
//       } else {
//         content.setAttribute("hidden", "true");
//         icon.setAttribute("href", `${baseurl}/assets/img/sprite.svg#expand_more`);
//       }
//     });
//   });

export function setupFilterMenuListeners() {
    updateFilterMenuState()
    window.addEventListener("resize", updateFilterMenuState)

    document.querySelectorAll(".usa-accordion__button").forEach((button) => {
        button.addEventListener("click", () => {
            const expanded = button.getAttribute("aria-expanded");
            const content = document.getElementById(button.getAttribute("id"));
            const icon = button.querySelector("svg use");
      
            if(expanded === 'false') {
                content.removeAttribute("hidden");
                icon.setAttribute("href", `${baseurl}/assets/img/sprite.svg#expand_less`);
            } else {
                content.setAttribute("hidden", "true");
                icon.setAttribute("href", `${baseurl}/assets/img/sprite.svg#expand_more`);
            }
        });
    });
}