import { sortDirection, sortSelection, parsedProjectsData } from "./data";
import { updateFilters } from "./filters";
import { sortCards } from "./sorting";
import { createProjectCards } from "./rendering";

let currentPage;
let filteredProjects = [...parsedProjectsData];

export function setupEventListeners() {
  sortSelection.addEventListener('change', () => sortCards());
  sortDirection.addEventListener('change', () => sortCards(sortDirection.value === 'descending'));
}

window.addEventListener('pageshow', (event) => {
  updateFilters();
  sortCards();

  if (event.persisted) {
    // The page was loaded from the bfcache (back-forward cache)
    updateFilters();
    sortCards();
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const searchForm = document.getElementById('search-form');
  const searchBox = document.getElementById("search-input");
  const projectList = document.getElementById("content-container")
  const projectCards = projectList.getElementsByClassName("project-card")

  searchForm.addEventListener("submit", (e) => {
    e.preventDefault();
  })
  
  searchBox.addEventListener("input", () => {
    const query = searchBox.value.toLowerCase();
    filteredProjects = parsedProjectsData.filter((project) => project.name.toLowerCase().includes(query.toLowerCase()));
    currentPage = 1
    createProjectCards()
  })
  createProjectCards()
})