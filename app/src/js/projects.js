import { reportHeadingTemplate, projectCardTemplate } from "./templates";
const filterBox = document.getElementById("filter-input");
var projectSections = document.querySelectorAll(".project_section");
const projectsData = document.getElementById('metrics').textContent;
const orgsData = document.getElementById('org-data').textContent;
const parsedOrgsData = JSON.parse(orgsData);
const parsedProjectsData = JSON.parse(projectsData);
const filtersContainer = document.querySelector('.filters-container');
const templateDiv = document.getElementById('content-container');
var projects = setProjectsData(parsedProjectsData)
const sortDirection = document.getElementById('sort-direction')
const sortSelection = document.getElementById('sort-selection')
var isSorted = false;


document.getElementById("sort-direction-form").hidden = !isSorted;

function sortByNumberAttribute(data, attribute) {
  // console.log(data)
  // console.log(attribute)
  data.sort((a, b) => {
    // console.log(a[attribute])
    // console.log(b[attribute])
    const tierA = a[attribute] !== undefined ? Number(a[attribute]) : Infinity;
    const tierB = b[attribute] !== undefined ? Number(b[attribute]) : Infinity;
    return tierA - tierB;
  });
  // data.sort((a, b) => Number(a.maturity_model_tier) - Number(b.maturity_model_tier));
}

function sortByStringAttribute(data, attribute) {
  data.sort((a, b) => {
    const hasAttributeA = typeof a[attribute] === 'string';
    const hasAttributeB = typeof b[attribute] === 'string';
  
    // If both objects have the attribute, sort by name
    if (hasAttributeA && hasAttributeB) {
      return a[attribute].localeCompare(b[attribute]);
    }
  
    // If only one object has the attribute, it should come first
    if (hasAttributeA) return -1;
    if (hasAttributeB) return 1;
  
    // If neither object has the attribute, sort by name
    return a.name.localeCompare(b.name);
  });
}



function setProjectsData(parsedData) {
  let projects = {};
  const orgCheckboxes = document.getElementById('organization-content').querySelectorAll('.usa-checkbox')
  const organizations = [...orgCheckboxes].map(checkbox => checkbox.textContent.trim());
  
  organizations.forEach(org => {
    projects[org] = getProjectsInOrg(parsedData, org);
  })
  return projects
}

function findObject(array, value) {
  return array.find((item) => item["name"] === value)
}

function getProjectsInOrg(array, value) {
  return array.filter((item) => item["owner"] === value)
}

sortSelection.addEventListener('change', e => {
  sortCards();
})

function sortCards() {
  const selection = sortSelection.value;

  for (const org in projects) {
    if (
        selection === "maturity_model_tier" || 
        selection === "stargazers_count" || 
        selection === 'forks_count'
      ) {
      sortByNumberAttribute(projects[org], selection)
    } 
    else if (selection === 'name') {
      projects[org].sort((a, b) => {
        return a.name.localeCompare(b.name);
      });
    }
    else if (selection === 'project_type' || selection === "project_fisma_level") {
      sortByStringAttribute(projects[org], selection)
    }
    createProjectCards()
  }
}

function createProjectCards() {
  templateDiv.innerHTML = ''
  for (const org in projects) {
    const orgProject = findObject(parsedOrgsData, org);
    const heading = reportHeadingTemplate(orgProject);
    const projectSectionsTemplate = document.createElement('div');
    projectSectionsTemplate.className = 'project_section'
    templateDiv.append(projectSectionsTemplate)
  
    const reportHeading = document.createElement('div');
    reportHeading.className = "report_heading"
    reportHeading.innerHTML = heading;
    projectSectionsTemplate.appendChild(reportHeading)
  
    const projectCards = document.createElement('ul');
    projectCards.className = "usa-card-group flex-align-stretch"
  
    projectSectionsTemplate.appendChild(projectCards)
  
  
    for (const repoIndex in projects[org]) {
      const repoData = projects[org][repoIndex]
      const projectCard = document.createElement('li');
      projectCard.className = 'usa-card project-card tablet:grid-col-12'
      projectCard.id = repoData.name
      projectCard.setAttribute('org-name', repoData.owner)
      projectCard.innerHTML = projectCardTemplate(repoData)
      projectCards.appendChild(projectCard);
    }
  }
  updateFilters()
  updateHeadingVisibility();
}

createProjectCards()

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
  const projectMaturityModelTier = "Tier " + currentProject.maturity_model_tier;
  const matchesMaturityModelTier = selectedFiltersObject.maturityModelTier.length === 0 || selectedFiltersObject.maturityModelTier.includes(projectMaturityModelTier);
  const matchesFismaLevel = selectedFiltersObject.fismaLevel.length === 0 || selectedFiltersObject.fismaLevel.includes(currentProject.project_fisma_level);
  const matchesProjectType = selectedFiltersObject.projectType.length === 0 || selectedFiltersObject.projectType.includes(currentProject.project_type);
  
  // Hide card if project does not match all filter categories
  card.hidden = !(matchesOrganization && matchesMaturityModelTier && matchesFismaLevel && matchesProjectType);

}

filterBox.addEventListener("input", () => {
  const query = filterBox.value.toLowerCase()

  // Iterate through each section
  projectSections.forEach((section) => {
    var queryMatchCheck = false
    const projectCards = section.querySelectorAll(".project-card")

    // Performs query and hides project card accordingly
    projectCards.forEach((card) => {
      card.hidden = !(
        query == "" || card.textContent.toLowerCase().includes(query)
      )

      if (!card.hidden) {
        queryMatchCheck = true
      }
    })

    // Hide heading if all cards under section are hidden
    const reportHeadings = section.querySelector(".report_heading")
    reportHeadings.hidden = !queryMatchCheck
  })
})