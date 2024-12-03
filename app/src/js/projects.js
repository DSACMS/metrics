import { reportHeadingTemplate, projectCardTemplate, renderProjectCards } from "./templates";
import DOMPurify from 'dompurify';

const projectsData = document.getElementById('metrics').textContent;
const orgsData = document.getElementById('org-data').textContent;
const parsedOrgsData = JSON.parse(orgsData);
const parsedProjectsData = JSON.parse(projectsData);
const filtersContainer = document.querySelector('.filters-container');
const templateDiv = document.getElementById('content-container');
const projects = setProjectsData(parsedProjectsData)
const sortDirection = document.getElementById('sort-direction');
const sortSelection = document.getElementById('sort-selection');

let currentPage = 1;
const itemsPerPage = 10;
let filteredProjects = [];

document.addEventListener('DOMContentLoaded', () => {
  if(parsedProjectsData && parsedProjectsData.length > 0) {
    filteredProjects = [...parsedProjectsData];
    renderPaginatedProjects();
  } else {
    console.error('Parsed projects empty')
  }
})


// Hide sort direction when sort is not selected
document.getElementById("sort-direction-form").hidden = true;

// Main Function to create project cards, filter buttons, and hide headings based on filters
createProjectCards();

// Listens for selection to sort by attribute
sortSelection.addEventListener('change', () => {
  // Unhide sort direction once sort by is selected
  document.getElementById("sort-direction-form").hidden = false;
  sortCards();
})

// Listens for sort direction to sort descending/ascending
sortDirection.addEventListener('change', () => {
  const isDescending = sortDirection.value === 'descending' ? true : false; 
  sortCards(isDescending);
})

// Keep filters after navigating back
window.addEventListener('pageshow', (event) => {
  updateFilters();
  sortCards();

  if (event.persisted) {
    // The page was loaded from the bfcache (back-forward cache)
    updateFilters();
    sortCards();
  }
});

// Sorting cards function for numberic attributes
function sortByNumberAttribute(data, attribute, isDescending) {
  data.sort((a, b) => {
    const attributeA = a[attribute] !== undefined ? Number(a[attribute]) : Infinity;
    const attributeB = b[attribute] !== undefined ? Number(b[attribute]) : Infinity;
    return isDescending ? attributeB - attributeA : attributeA - attributeB;
  });
}

// Sort cards function for string type attributes
function sortByStringAttribute(data, attribute, isDescending) {
  data.sort((a, b) => {
    const hasAttributeA = typeof a[attribute] === 'string';
    const hasAttributeB = typeof b[attribute] === 'string';
  
    // If both objects have the attribute, sort by name
    if (hasAttributeA && hasAttributeB) {
      return isDescending ? b[attribute].localeCompare(a[attribute]) : a[attribute].localeCompare(b[attribute]);
    }
  
  // If only one object has the attribute, determine order based on `isDescending`
  if (hasAttributeA) return isDescending ? 1 : -1;
  if (hasAttributeB) return isDescending ? -1 : 1;
  
    // If neither object has the attribute, sort by name
    return isDescending ? b.name.localeCompare(a.name) : a.name.localeCompare(b.name);
  });
}
// Function to map organizations with their projects
function setProjectsData(parsedData) {
  let projects = {};
  const orgCheckboxes = document.getElementById('organization-content').querySelectorAll('.usa-checkbox');
  const organizations = [...orgCheckboxes].map(checkbox => checkbox.textContent.trim());
  
  organizations.forEach(org => {
    projects[org] = getProjectsInOrg(parsedData, org);
  })
  return projects
}

function findObject(array, value) {
  return array.find((item) => item["name"] === value);
}

function getProjectsInOrg(array, value) {
  return array.filter((item) => item["owner"] === value);
}

function sortCards(isDescending = false) {
  const selection = sortSelection.value;

  let targetProjects = filteredProjects || parsedOrgsData

  if(["maturity_model_tier", "stargazers_count", "forks_count"].includes(selection)) {
    sortByNumberAttribute(targetProjects, selection, isDescending);
  } else { 
    sortByStringAttribute(targetProjects, selection, isDescending);
  }

  updatePagination()
  renderPaginatedProjects()

  // for (const org in projects) {
  //   // Selected attribute of type number
  //   if 
  //     (
  //       selection === "maturity_model_tier" || 
  //       selection === "stargazers_count" || 
  //       selection === 'forks_count'
  //     ) {
  //       sortByNumberAttribute(projects[org], selection, descending);
  //     } 
  //   // Selected attribute of type string
  //   else if
  //     (
  //       selection === 'name' || 
  //       selection === 'project_type' || 
  //       selection === "fisma_level"
  //     ) {
  //       sortByStringAttribute(projects[org], selection, descending);
  //     }
  //   createProjectCards();
  // }
}

function createProjectCards(filteredProjects) {
  templateDiv.innerHTML = ''

  // const allProjects = Object.keys(projects).flatMap(org => projects[org].map(project => ({ ...project, org })));

  const allProjects = (filteredProjects || parsedProjectsData).map((project) => ({
    ...project,
    org: project.owner
  }));
  
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const paginatedProjects = allProjects.slice(startIndex, endIndex);

  const groupedByOrg = paginatedProjects.reduce((acc, curr) => {
    if(!acc[curr.org]) {
      acc[curr.org] = []
    }
    acc[curr.org].push(curr);
    return acc
  }, {});

  for (const org in groupedByOrg) {
    const orgProject = findObject(parsedOrgsData, org);
    const orgHeading = reportHeadingTemplate(orgProject);
    const projectSectionsTemplate = document.createElement('div');
    projectSectionsTemplate.className = 'project_section';
    templateDiv.append(projectSectionsTemplate);
  
    // Add report heading for each org
    const reportHeading = document.createElement('div');
    reportHeading.className = "report_heading";
    reportHeading.innerHTML = DOMPurify.sanitize(orgHeading);
    projectSectionsTemplate.appendChild(reportHeading);
  
    const projectCards = document.createElement('ul');
    projectCards.className = "usa-card-group flex-align-stretch";
  
    projectSectionsTemplate.appendChild(projectCards);

    groupedByOrg[org].forEach(repoData => {
      const projectCard = document.createElement('li');
      projectCard.className = 'usa-card project-card tablet:grid-col-12';
      projectCard.id = repoData.name;
      projectCard.setAttribute('org-name', repoData.owner);
      projectCard.innerHTML = DOMPurify.sanitize(projectCardTemplate(repoData));
      projectCards.appendChild(projectCard);
    })
  }
  updateFilters();
  updateHeadingVisibility();
  renderPaginationControls(allProjects.length)
}

function renderPaginationControls(totalProjectsCount) {
  const paginationDiv = document.getElementById('pagination-controls') || document.createElement('div');
  paginationDiv.id = 'pagination-controls';
  paginationDiv.innerHTML = ''; 

  // Determine the total number of pages
  // const totalProjects = Object.values(projects).flat().length; 
  const totalPages = Math.ceil(totalProjectsCount / itemsPerPage);

  // Create Previous Button
  const prevButton = document.createElement('button');
  prevButton.textContent = 'Previous';
  prevButton.disabled = currentPage === 1;
  prevButton.addEventListener('click', () => {
    if (currentPage > 1) {
      currentPage--;
      createProjectCards(); 
    }
  });
  paginationDiv.appendChild(prevButton);

  // Create Page Number Indicators
  for (let i = 1; i <= totalPages; i++) {
    const pageButton = document.createElement('button');
    pageButton.textContent = i;
    pageButton.disabled = i === currentPage; 
    pageButton.addEventListener('click', () => {
      currentPage = i;
      createProjectCards(); 
    });
    paginationDiv.appendChild(pageButton);
  }

  // Create Next Button
  const nextButton = document.createElement('button');
  nextButton.textContent = 'Next';
  nextButton.disabled = currentPage === totalPages;
  nextButton.addEventListener('click', () => {
    if (currentPage < totalPages) {
      currentPage++;
      createProjectCards(); // Re-render cards
    }
  });
  paginationDiv.appendChild(nextButton);

  // Append pagination controls to the DOM
  if (!document.body.contains(paginationDiv)) {
    templateDiv.parentElement.appendChild(paginationDiv);
  }
}

// Checks for Checkbox event and updates filters
addGlobalEventListener('change', '.usa-checkbox__input', e => {
  // Can use this e.target.name to update selected filters object
  updateFilters();
  updateFilteredProjects()
}, filtersContainer)

// Function to update filters
function updateFilters() {

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

  updateHeadingVisibility();
}

function updateFilteredProjects() {

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
 
  console.log({filteredProjects})
  updatePagination(filteredProjects);
  renderPaginatedProjects(filteredProjects)
  sortCards();
}

function updatePagination(filteredProjects) {
  const totalProjects = (filteredProjects || parsedProjectsData).length;
  const totalPages = Math.ceil(totalProjects / itemsPerPage);

  currentPage = Math.min(currentPage, totalPages || 1);
  renderPaginationControls(totalPages);
}

function renderPaginatedProjects(filteredProjects) {
  console.log("IN RENDERPAGINATED: ", filteredProjects)
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const paginatedProjects = filteredProjects.slice(startIndex, endIndex);

  templateDiv.innerHTML = '';

  const groupedByOrg = paginatedProjects.reduce((acc, curr) => {
    if(!acc[curr.org]) {
      acc[curr.org] = []
    }
    acc[curr.org].push(curr);
    return acc
  }, {});

  for (const org in groupedByOrg) {
    const orgProject = findObject(parsedOrgsData, org);
    const orgHeading = reportHeadingTemplate(orgProject);
    const projectSectionsTemplate = document.createElement('div');
    projectSectionsTemplate.className = 'project_section';
    // templateDiv.append(projectSectionsTemplate);
  
    // Add report heading for each org
    const reportHeading = document.createElement('div');
    reportHeading.className = "report_heading";
    reportHeading.innerHTML = DOMPurify.sanitize(orgHeading);
    projectSectionsTemplate.appendChild(reportHeading);
  
    const projectCards = document.createElement('ul');
    projectCards.className = "usa-card-group flex-align-stretch";
  
    // projectSectionsTemplate.appendChild(projectCards);

    groupedByOrg[org].forEach(repoData => {
      const projectCard = document.createElement('li');
      projectCard.className = 'usa-card project-card tablet:grid-col-12';
      projectCard.id = repoData.name;
      projectCard.setAttribute('org-name', repoData.owner);
      projectCard.innerHTML = DOMPurify.sanitize(projectCardTemplate(repoData));
      projectCards.appendChild(projectCard);
    });

    projectSectionsTemplate.appendChild(projectCards);
    templateDiv.append(projectSectionsTemplate);

  }

  updateHeadingVisibility();
}

// Function to add filters buttons
function addFilterButtonGroup(selectedFiltersObject) {
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

// Function for adding a dynamic global event listener
// Parameters:
// - type: The type of event to listen for (e.g., 'click', 'mouseover')
// - selector: The CSS selector to match the target elements (e.g., '.class-name')
// - callback: The callback function to execute when the event is triggered on a matching element
// - parent: The element to attach the event listener to; defaults to 'document' for global listening
function addGlobalEventListener(type, selector, callback, parent = document) {
  parent.addEventListener(type, e => {
    if (e.target.matches(selector)) {
      callback(e);
    }
  });
}

// Function to update heading visibility
function updateHeadingVisibility() {
  const projectSections = document.querySelectorAll(".project_section");
  projectSections.forEach(section => {
    let hasVisibleCard = false;
    // Select the report heading within the current section
    let reportHeading = section.querySelector('.report_heading');
    
    // Select all project cards within the current section
    let projectCards = section.querySelectorAll('.project-card');
    
    // Flag visible card if any card is not hidden
    projectCards.forEach((card) => {
      if (!card.hidden) {
        hasVisibleCard = true;
      }
    })
    
  // Hide heading if all cards under section are hidden
  reportHeading.hidden = !hasVisibleCard;
  });
}

// Function to return whether all filter criteria were met
function checkFilterCriteria(card, selectedFiltersObject) {
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

    filteredProjects = parsedProjectsData.filter((project) => project.name.toLowerCase().includes(query));

    currentPage = 1
    createProjectCards()

  })


})

