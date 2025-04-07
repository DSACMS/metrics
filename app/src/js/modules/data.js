import DOMPurify from 'dompurify';

export const projectsData = document.getElementById('metrics').textContent;
export const orgsData = JSON.parse(document.getElementById('org-data').textContent);
export const siteData = JSON.parse(document.getElementById('site-data').textContent);
export const parsedProjectsData = JSON.parse(projectsData);
export const filtersContainer = document.querySelector('.filters-container');
export const templateDiv = document.getElementById('content-container');
export const sortDirection = document.getElementById('sort-direction');
export const sortSelection = document.getElementById('sort-selection');
export const baseurl = DOMPurify.sanitize(siteData.baseurl);

export const projects = setProjectsData(parsedProjectsData)

// export let filteredProjects = [...parsedProjectsData];

export function setProjectsData(parsedData) {
    let projects = {};
    const orgCheckboxes = document.getElementById('organization-content').querySelectorAll('.usa-checkbox');
    const organizations = [...orgCheckboxes].map(checkbox => checkbox.textContent.trim());
    
    organizations.forEach(org => {
      projects[org] = getProjectsInOrg(parsedData, org);
    })
    return projects
  }

  export function findObject(array, value) {
    return array.find((item) => item["name"] === value);
  }
  
  export function getProjectsInOrg(array, value) {
    return array.filter((item) => item["owner"] === value);
  }
