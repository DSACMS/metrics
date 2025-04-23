import { projects, parsedProjectsData } from "./data";
import { addGlobalEventListener, updateHeadingVisibility } from "./utilities";
import { renderPaginatedProjects, renderPaginationControls } from "./rendering";
import { sortCards } from "./sorting";

let currentPage = 1
const itemsPerPage = 10;
let filteredProjects = [...parsedProjectsData];

export function getFilteredProjects() {
  return filteredProjects;
}

export function setFilteredProjects(projects) {
  filteredProjects = projects;
}

export function updateFilteredProjects() {
  const selectedFiltersObject = {
    organization: [],
    maturityModelTier: [],
    fismaLevel: [],
    projectType: []
  }

  document.querySelectorAll('input[name="org-filter"]:checked').forEach(checkbox => {
    selectedFiltersObject.organization.push(checkbox.value);
  });
  document.querySelectorAll('input[name="tier-filter"]:checked').forEach(checkbox => {
    selectedFiltersObject.maturityModelTier.push(checkbox.value);
  });
  document.querySelectorAll('input[name="fisma-level-filter"]:checked').forEach(checkbox => {
    selectedFiltersObject.fismaLevel.push(checkbox.value);
  });
  document.querySelectorAll('input[name="project-type-filter"]:checked').forEach(checkbox => {
    selectedFiltersObject.projectType.push(checkbox.value);
  });

  const allProjects = Object.keys(projects).flatMap((org) => projects[org].map((project) => ({...project, org})))
  filteredProjects = allProjects.filter((project) => {
    const matchesOrg = selectedFiltersObject.organization.length === 0 || selectedFiltersObject.organization.includes(project.org);
    const matchesTier = selectedFiltersObject.maturityModelTier.length === 0 || selectedFiltersObject.maturityModelTier.includes("Tier" + project.maturityModelTier);
    const matchesFisma = selectedFiltersObject.fismaLevel.length === 0 || selectedFiltersObject.fismaLevel.includes(project.fismaLevel);
    const matchesType = selectedFiltersObject.projectType.length === 0 || selectedFiltersObject.projectType.includes(project.projectType);
    return  matchesOrg && matchesTier && matchesFisma && matchesType;
  });
 
  updatePagination(filteredProjects);
  renderPaginatedProjects(filteredProjects)
  sortCards();
}

export function addFilterButtonGroup(selectedFiltersObject) {
  // Get filter tags div from DOM
  const selectedFiltersContainer = document.getElementById('filter-tags');
  selectedFiltersContainer.innerHTML = '';

  // Manipulate the DOM to create buttons based on the selected filters
  const filtersButtonGroup = document.createElement('div');
  filtersButtonGroup.className = "usa-button-group";
  selectedFiltersContainer.appendChild(filtersButtonGroup);

  for (const filterCategory in selectedFiltersObject) {
    const filtersArray = selectedFiltersObject[filterCategory];
    
    filtersArray.forEach(filter => {
      // TODO: add remove.svg to button
      const filterButton = document.createElement('button');
      filterButton.className = 'usa-button margin-bottom-1';
      filterButton.textContent = filter;
      filtersButtonGroup.appendChild(filterButton);
    })
  }

  addGlobalEventListener("click", "#filter-tags .usa-button", e => {
    const buttonName = e.target.textContent;
    const selectedCheckboxes = document.querySelectorAll("input:checked");

    selectedCheckboxes.forEach(checkbox => {
      if (buttonName == checkbox.value) {
        e.target.remove();
        checkbox.checked = false;
        updateFilters();
      }
    })
    
  }, filtersButtonGroup);
}

export function updateFilters() {
  const selectedFiltersObject = {
    organization: [],
    maturityModelTier: [],
    fismaLevel: [],
    projectType: []
  }

  document.querySelectorAll('input[name="org-filter"]:checked').forEach(checkbox => {
    selectedFiltersObject.organization.push(checkbox.value);
  });
  document.querySelectorAll('input[name="tier-filter"]:checked').forEach(checkbox => {
    selectedFiltersObject.maturityModelTier.push(checkbox.value);
  });
  document.querySelectorAll('input[name="fisma-level-filter"]:checked').forEach(checkbox => {
    selectedFiltersObject.fismaLevel.push(checkbox.value);
  });
  document.querySelectorAll('input[name="project-type-filter"]:checked').forEach(checkbox => {
    selectedFiltersObject.projectType.push(checkbox.value);
  });

  addFilterButtonGroup(selectedFiltersObject)
  const projectSections = document.querySelectorAll(".project_section");

  projectSections.forEach((section) => {
    const projectCards = section.querySelectorAll(".project-card");
    
    projectCards.forEach((card) => {
      checkFilterCriteria(card, selectedFiltersObject);
    })
  })

  addFilterButtonGroup(selectedFiltersObject);
  updateHeadingVisibility();
}

export function checkFilterCriteria(card, selectedFiltersObject) {
  const cardName = card.querySelector(".usa-card__heading").innerText;
  const currentProject = parsedProjectsData.find((project) => project.name === cardName)
  const matchesOrganization = selectedFiltersObject.organization.length === 0 || selectedFiltersObject.organization.includes(currentProject.owner);
  const projectMaturityModelTier = "Tier " + currentProject.maturityModelTier;
  const matchesMaturityModelTier = selectedFiltersObject.maturityModelTier.length === 0 || selectedFiltersObject.maturityModelTier.includes(projectMaturityModelTier);
  const matchesFismaLevel = selectedFiltersObject.fismaLevel.length === 0 || selectedFiltersObject.fismaLevel.includes(currentProject.fismaLevel);
  const matchesProjectType = selectedFiltersObject.projectType.length === 0 || selectedFiltersObject.projectType.includes(currentProject.projectType);
  
  // Hide card if project does not match all filter categories
  card.hidden = !(matchesOrganization && matchesMaturityModelTier && matchesFismaLevel && matchesProjectType);
}

export function updatePagination() {
  const totalProjects = (filteredProjects || parsedProjectsData).length;
  const totalPages = Math.ceil(totalProjects / itemsPerPage);
  currentPage = Math.min(currentPage, totalPages || 1);
  renderPaginationControls(totalPages);
}