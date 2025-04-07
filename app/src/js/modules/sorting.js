import { sortSelection, parsedProjectsData, filtersContainer } from "./data";
import { addGlobalEventListener } from "./utilities";
import { updateFilters, updateFilteredProjects, updatePagination } from "./filters";
import { renderPaginatedProjects } from "./rendering";

let filteredProjects = [...parsedProjectsData]

export function sortCards(isDescending = false) {
  const selection = sortSelection.value;

  let targetProjects = filteredProjects || parsedOrgsData

  if(["maturity_model_tier", "stargazers_count", "forks_count"].includes(selection)) {
    sortByNumberAttribute(targetProjects, selection, isDescending);
  } else { 
    sortByStringAttribute(targetProjects, selection, isDescending);
  }

  updatePagination();
  renderPaginatedProjects(filteredProjects);
}

export function sortByNumberAttribute(data, attribute, isDescending) {
  data.sort((a, b) => {
    const attributeA = a[attribute] !== undefined ? Number(a[attribute]) : Infinity;
    const attributeB = b[attribute] !== undefined ? Number(b[attribute]) : Infinity;
    return isDescending ? attributeB - attributeA : attributeA - attributeB;
  });
}

export function sortByStringAttribute(data, attribute, isDescending) {
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

addGlobalEventListener('change', '.usa-checkbox__input', e => {
    // Can use this e.target.name to update selected filters object
    updateFilters();
    updateFilteredProjects()
  }, filtersContainer)