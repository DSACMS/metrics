import { createProjectCards } from "./modules/rendering";
import { updateFilteredProjects } from "./modules/filters";
import { setupEventListeners } from './modules/events';
import { setupFilterMenuListeners } from "./modules/ui";

document.addEventListener("DOMContentLoaded", () => {
  setTimeout(async () => {
    await createProjectCards();
    updateFilteredProjects();
    setupEventListeners();
  }, 50);

  setupFilterMenuListeners();
});
