import { reportHeadingTemplate, projectCardTemplate } from "./templates";
import DOMPurify from 'dompurify';

// const searchForm = document.getElementById('search-form');
// const searchBox = document.getElementById("search-input");
// const label = document.querySelector('label[for="search-input"]');


const projectsData = document.getElementById('metrics').textContent;
const orgsData = document.getElementById('org-data').textContent;
const parsedOrgsData = JSON.parse(orgsData);
const parsedProjectsData = JSON.parse(projectsData);
const filtersContainer = document.querySelector('.filters-container');
const templateDiv = document.getElementById('content-container');
const projects = setProjectsData(parsedProjectsData)
const sortDirection = document.getElementById('sort-direction');
const sortSelection = document.getElementById('sort-selection');

console.log({projects})


// Hide sort direction when sort is not selected
document.getElementById("sort-direction-form").hidden = true;

// Main Function to create project cards, filter buttons, and hide headings based on filters
createProjectCards();

// Listens for selection to sort by attribute
sortSelection.addEventListener('change', e => {
  sortCards();
  // Unhide sort direction once sort by is selected
  document.getElementById("sort-direction-form").hidden = false;
})

// Listens for sort direction to sort descending/ascending
sortDirection.addEventListener('change', e => {
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

function sortCards(descending=false) {
  const selection = sortSelection.value;

  for (const org in projects) {
    // Selected attribute of type number
    if 
      (
        selection === "maturity_model_tier" || 
        selection === "stargazers_count" || 
        selection === 'forks_count'
      ) {
        sortByNumberAttribute(projects[org], selection, descending);
      } 
    // Selected attribute of type string
    else if
      (
        selection === 'name' || 
        selection === 'project_type' || 
        selection === "fisma_level"
      ) {
        sortByStringAttribute(projects[org], selection, descending);
      }
    createProjectCards();
  }
}

function createProjectCards() {
  templateDiv.innerHTML = ''
  for (const org in projects) {
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
  
    // Create all project cards for each org
    for (const repoIndex in projects[org]) {
      const repoData = projects[org][repoIndex];
      const projectCard = document.createElement('li');
      projectCard.className = 'usa-card project-card tablet:grid-col-12';
      projectCard.id = repoData.name;
      projectCard.setAttribute('org-name', repoData.owner);
      projectCard.innerHTML = DOMPurify.sanitize(projectCardTemplate(repoData));
      projectCards.appendChild(projectCard);
    }
  }
  updateFilters();
  updateHeadingVisibility();
}

// Checks for Checkbox event and updates filters
addGlobalEventListener('change', '.usa-checkbox__input', e => {
  // Can use this e.target.name to update selected filters object
  updateFilters();
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
  const cardName = card.querySelector(".text-no-underline").textContent;
  const currentProject = parsedProjectsData.find((project) => project["name"] === cardName)
  
  const matchesOrganization = selectedFiltersObject.organization.length === 0 || selectedFiltersObject.organization.includes(currentProject.owner);
  const projectMaturityModelTier = "Tier " + currentProject.maturityModelTier;
  const matchesMaturityModelTier = selectedFiltersObject.maturityModelTier.length === 0 || selectedFiltersObject.maturityModelTier.includes(projectMaturityModelTier);
  const matchesFismaLevel = selectedFiltersObject.fismaLevel.length === 0 || selectedFiltersObject.fismaLevel.includes(currentProject.fismaLevel);
  const matchesProjectType = selectedFiltersObject.projectType.length === 0 || selectedFiltersObject.projectType.includes(currentProject.projectType);
  
  // Hide card if project does not match all filter categories
  card.hidden = !(matchesOrganization && matchesMaturityModelTier && matchesFismaLevel && matchesProjectType);

}



// SEARCH BOX FUNCTIONS
// Value needs to match project[org][index].name
// search value needs to disapear when typing starts
// functions needs to return project card matching input value
// should filter as typing begins
// event prevent default from form reload
document.addEventListener("DOMContentLoaded", () => {
  const searchForm = document.getElementById('search-form');
  const searchBox = document.getElementById("search-input");
  const projectList = document.getElementById("content-container");
  const projectCards = projectList.getElementsByClassName("project-card");
  const projectSections = document.querySelectorAll(".project_section");
  // console.log("org name: ", projectSections[0].childNodes[1].childNodes)
  // console.log("org THINGS: ", projectSections[0].attributes)

  searchForm.addEventListener("submit", (e) => {
    e.preventDefault();
  })
  
  searchBox.addEventListener("input", () => {
    const query = searchBox.value.toLowerCase();

    projectSections.forEach((section) => {
      const orgName = section.querySelector(".report_heading h2")
      console.log({orgName})
      console.log(orgName.innerHTML)

      let hasVisableProjects = false;
    

    Array.from(projectCards).forEach((card) => {
      const cardName = card.id.toLowerCase()
      const isVisable = query === "" || cardName.includes(query)
      card.style.display = isVisable ? "" : "none";

      if(isVisable) hasVisableProjects = true
    })


    // orgName.innerHTML = hasVisableProjects ? orgName.innerHTML : "";
    if(hasVisableProjects) {
      console.log({hasVisableProjects})
      orgName.innerHTML.style.display = "";
    } else {
      orgName.innerHTML.style.display = "none";
    }
  })
  })
})


// // Search function
// {projects}
// searchBox.addEventListener("input", () => {
//   const projectSections = document.querySelectorAll(".project_section");
//   console.log("projects inside search: ", projects.DSACMS[3].name)
//   console.log({projectSections})
//   const query = searchBox.value.toLowerCase()



//   // Iterate through each section
//   projectSections.forEach((section) => {
//     var queryMatchCheck = false
//     const projectCards = section.querySelectorAll(".project-card")
//     console.log({projectCards})

//     // Performs query and hides project card accordingly
//     projectCards.forEach((card) => {
//       card.hidden = !(
//         query == "" || card.textContent.toLowerCase().includes(query)
//       )

//       if (!card.hidden) {
//         queryMatchCheck = false
//       }
//     })

//     // Hide heading if all cards under section are hidden
//     const reportHeadings = section.querySelector(".report_heading")
//     reportHeadings.hidden = !queryMatchCheck
//   })
// })