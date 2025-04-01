import { reportHeadingTemplate, projectCardTemplate } from "../templates";
import { templateDiv, parsedProjectsData, orgsData, siteData, findObject, baseurl } from "./data";
import { updateFilters } from "./filters";
import { getPageRange, updateHeadingVisibility } from "./utilities";
import DOMPurify from 'dompurify';

const parsedOrgsData = orgsData

let currentPage = 1
const itemsPerPage = 10;

export function createProjectCards() {
    let filteredProjects = [...parsedProjectsData];
    templateDiv.innerHTML = ''
  
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
    
      const reportHeading = document.createElement('div');
      reportHeading.className = "report_heading";
      reportHeading.innerHTML = DOMPurify.sanitize(orgHeading);
      projectSectionsTemplate.appendChild(reportHeading);
    
      const projectCards = document.createElement('ul');
      projectCards.className = "usa-card-group flex-align-stretch";
    
      projectSectionsTemplate.appendChild(projectCards);
  
      groupedByOrg[org].forEach(repoData => {
        repoData.baseurl = siteData.baseurl;
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

export function renderPaginatedProjects(projects = parsedProjectsData) {
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const paginatedProjects = projects.slice(startIndex, endIndex);

  templateDiv.innerHTML = '';

  const groupedByOrg = paginatedProjects.reduce((acc, curr) => {
    if(!acc[curr.owner]) {
      acc[curr.owner] = []
    }
    acc[curr.owner].push(curr);
    return acc
  }, {});

  for (const org in groupedByOrg) {
    const orgProject = findObject(parsedOrgsData, org);
    const orgHeading = reportHeadingTemplate(orgProject);
    const projectSectionsTemplate = document.createElement('div');
    projectSectionsTemplate.className = 'project_section';
  
    const reportHeading = document.createElement('div');
    reportHeading.className = "report_heading";
    reportHeading.innerHTML = DOMPurify.sanitize(orgHeading);
    projectSectionsTemplate.appendChild(reportHeading);
  
    const projectCards = document.createElement('ul');
    projectCards.className = "usa-card-group flex-align-stretch";

    groupedByOrg[org].forEach(repoData => {
      repoData.baseurl = siteData.baseurl;
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

export function renderPaginationControls(totalProjectsCount) {
  const paginationDiv = document.getElementById('pagination-controls') || document.createElement('div');
  paginationDiv.id = 'pagination-controls';
  paginationDiv.className = 'usa-pagination';
  paginationDiv.innerHTML = '';

  const totalPages = Math.ceil(totalProjectsCount / itemsPerPage);

  const paginationList = document.createElement('ul');
  paginationList.className = 'usa-pagination__list';

  const prevItem = document.createElement('li');
  prevItem.className = 'usa-pagination__item usa-pagination__arrow';
  const prevButton = document.createElement('a');
  prevButton.href = 'javascript:void(0);';
  prevButton.className = 'usa-pagination__link usa-pagination__previous-page';
  prevButton.setAttribute('aria-label', 'Previous page');
  if (currentPage === 1) prevButton.classList.add('usa-pagination__disabled');
  prevButton.innerHTML = `
    <svg class="usa-icon" aria-hidden="true" role="img">
      <use xlink:href="${baseurl}/assets/img/sprite.svg#navigate_before"></use>
    </svg>
    <span class="usa-pagination__link-text">Previous</span>
  `;
  prevButton.addEventListener('click', () => {
    if (currentPage > 1) {
      currentPage--;
      createProjectCards();
    }
  });
  prevItem.appendChild(prevButton);
  paginationList.appendChild(prevItem);

  const pageRange = getPageRange(currentPage, totalPages, 3);
  pageRange.forEach((page, index) => {
    const pageItem = document.createElement('li');
    pageItem.className = 'usa-pagination__item';

    if (page === '...') {
      pageItem.className += ' usa-pagination__overflow';
      pageItem.innerHTML = `<span aria-label="ellipsis indicating non-visible pages">…</span>`;
    } else {
      pageItem.className += ' usa-pagination__page-no';
      const pageButton = document.createElement('a');
      pageButton.href = 'javascript:void(0);';
      pageButton.className = `usa-pagination__button${page === currentPage ? ' usa-current' : ''}`;
      pageButton.textContent = page;
      pageButton.setAttribute('aria-label', `Page ${page}`);
      if (page === currentPage) pageButton.setAttribute('aria-current', 'page');
      pageButton.addEventListener('click', () => {
        currentPage = page;
        createProjectCards();
      });
      pageItem.appendChild(pageButton);
    }
    paginationList.appendChild(pageItem);
  });

  const nextItem = document.createElement('li');
  nextItem.className = 'usa-pagination__item usa-pagination__arrow';
  const nextButton = document.createElement('a');
  nextButton.href = 'javascript:void(0);';
  nextButton.className = 'usa-pagination__link usa-pagination__next-page';
  nextButton.setAttribute('aria-label', 'Next page');
  if (currentPage === totalPages) nextButton.classList.add('usa-pagination__disabled');
  nextButton.innerHTML = `
    <span class="usa-pagination__link-text">Next</span>
    <svg class="usa-icon" aria-hidden="true" role="img">
      <use xlink:href="${baseurl}/assets/img/sprite.svg#navigate_next"></use>
    </svg>
  `;
  nextButton.addEventListener('click', () => {
    if (currentPage < totalPages) {
      currentPage++;
      createProjectCards();
    }
  });
  nextItem.appendChild(nextButton);
  paginationList.appendChild(nextItem);

  paginationDiv.appendChild(paginationList);

  if (!document.body.contains(paginationDiv)) {
    templateDiv.parentElement.appendChild(paginationDiv);
  }
}
