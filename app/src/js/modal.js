export function operateModal() {
    const modalOpenButtons = document.querySelectorAll("[data-open-modal]");
    const modalCloseButtons = document.querySelectorAll("[data-close-modal]");

    const openModal = (id) => {
        const modal = document.getElementById(id);
        if(modal) {
            modal.classList.add("usa-modal--active");
            modal.setAttribute("aria-hidden", "false");
            console.log("Modal is open")
        }
    };

    const closeModal = (modal) => {
        if(modal) {
            modal.classList.remove("usa-modal--active");
            modal.setAttribute("aria-hidden", "true");
            console.log("modal is closed")
        }
    };

    modalOpenButtons.forEach((button) => {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation();
            const id = button.getAttribute("aria-controls");
            openModal(id);
        });
    });

    modalCloseButtons.forEach((button) => {
        button.addEventListener("click", (e) => {
            e.stopPropagation();
            const modal = button.closest(".usa-modal");
            closeModal(modal);
        });
    });

    document.addEventListener("click", (e) => {
        const activeModal = document.querySelector(".usa-modal.usa-modal--active");
        if(activeModal && !activeModal.contains(e.target)) {
            closeModal(activeModal);
        }
    });

    document.addEventListener("keydown", (e) => {
        if(e.key === "Escape") {
            const activeModal = document.querySelector(".usa-modal.usa-modal--active");
            closeModal(activeModal)
        }
    });
}

document.addEventListener("DOMContentLoaded", operateModal)