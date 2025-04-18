import { reportHeadingTemplate, projectCardTemplate } from "../templates";
import { templateDiv, parsedProjectsData, orgsData, siteData, findObject, baseurl } from "./data";
import { getFilteredProjects, updateFilters } from "./filters";
import { getPageRange, updateHeadingVisibility } from "./utilities";
import DOMPurify from 'dompurify';

const parsedOrgsData = orgsData
let currentPage = 1
const itemsPerPage = 10;

function renderProjectGroups(projects, groupByKey = 'org') {
  const groupedByOrg = projects.reduce((acc, curr) => {
    const groupKey = curr[groupByKey];
    if(!acc[groupKey]) {
      acc[groupKey] = [];
    }
    acc[groupKey].push(curr);
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
        });
  }
}

export function createProjectCards(projects = getFilteredProjects()) {
  templateDiv.innerHTML = ''
  
  const allProjects = (projects || parsedProjectsData).map((project) => ({
    ...project,
    org: project.owner
  }));
  
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const paginatedProjects = allProjects.slice(startIndex, endIndex);

  renderProjectGroups(paginatedProjects);
  updateFilters();
  updateHeadingVisibility();
  renderPaginationControls(allProjects.length);
}

export const renderPaginatedProjects = createProjectCards;

export function renderPaginationControls(totalProjectsCount) {
  const paginationDiv = document.getElementById('pagination-controls') || document.createElement('div');
  paginationDiv.id = 'pagination-controls';
  paginationDiv.className = 'usa-pagination';
  paginationDiv.innerHTML = '';
  
  const totalPages = Math.ceil(totalProjectsCount / itemsPerPage);
  currentPage = Math.max(1, Math.min(currentPage, totalPages || 1));
  
  const paginationList = document.createElement('ul');
  paginationList.className = 'usa-pagination__list';

  const prevItem = createPaginationButton({
    className: 'usa-pagination__previous-page',
    label: 'Previous page',
    disabled: currentPage === 1,
    icon: 'navigate_before',
    text: 'Previous',
    onclick: () => navigateToPage(currentPage - 1)
  });
  paginationList.appendChild(prevItem);

  const pageRange = getPageRange(currentPage, totalPages, 3);
  pageRange.forEach((page) => {
    const isEllipsis = page === '...';
    const pageItem = document.createElement('li');
    pageItem.className = `usa-pagination__item ${isEllipsis ? 'usa-pagination__overflow' :
      'usa-pagination__page-no'}`;

    if (isEllipsis) {
      pageItem.innerHTML = `<span aria-label="ellipsis indicating non-visible pages">…</span>`;
    } else {
      const isCurrent = page === currentPage;
      const pageButton = document.createElement('a');
      pageButton.href = 'javascript:void(0);';
      pageButton.className = `usa-pagination__button${isCurrent ? ' usa-current' : ''}`;
      pageButton.textContent = page;
      pageButton.setAttribute('aria-label', `Page ${page}`);

      if (isCurrent) pageButton.setAttribute('aria-current', 'page');
        pageButton.addEventListener('click', () => navigateToPage(page));
        pageItem.appendChild(pageButton);
    }
    paginationList.appendChild(pageItem);
  });

  const nextItem = createPaginationButton({
    className: 'usa-pagination__next-page',
    label: 'Next page',
    disabled: currentPage === totalPages,
    icon: 'navigate_next',
    text: 'Next',
    onclick: () => navigateToPage(currentPage + 1)
  });
  paginationList.appendChild(nextItem);

  paginationDiv.appendChild(paginationList);

  if (!document.body.contains(paginationDiv)) {
    templateDiv.parentElement.appendChild(paginationDiv);
  }
}

function navigateToPage(page) {
  if(page >= 1 && page <= Math.ceil(getFilteredProjects().length / itemsPerPage)) {
    currentPage = page;
    createProjectCards();
  }
}

function createPaginationButton({
  className,
  label,
  disabled,
  icon,
  text,
  iconPosition = 'before',
  onclick
}) {
  const item = document.createElement('li');
  item.className = 'usa-pagination__item usa-pagination__arrow';

  const button = document.createElement('a');
  button.href = 'javascript:void(0);';
  button.className = `usa-pagination__link ${className}`;
  button.setAttribute('aria-label', label);
  if(disabled) button.classList.add('usa-pagination__disabled');

  const iconHtml = `
    <svg class="usa-icon" aria-hidden="true" role="img">
      <use xlink:href="${baseurl}/assets/img/sprite.svg#${icon}"></use>
    </svg>
  `;

  button.innerHTML = iconPosition === 'before'
    ? `${iconHtml}<span class="usa-pagination__link-text">${text}</span>`
    : `<span class="usa-pagination__link-text">${text}</span>${iconHtml}`;

  if(!disabled) {
    button.addEventListener('click', onclick);
  }

  item.appendChild(button);
  return item;
}
