export const reportHeadingTemplate = function(data) {  
    return `
          <h2>
            ${ data.name }
            <img
              src="${data.avatar_url}"
              alt="Organization Avatar"
              width="20"
            >
          </h2>
    `
}

export function projectCardTemplate(data) {  
    const baseUrl = window.location.hostname === "dsacms.github.io" ? '/metrics' : ""
    const description = data.description !== null ? data.description : ""
    return `
        <div class="usa-card-outer outer-project-template">
            <div class="usa-card-middle">
                <a href="${ baseUrl }/${ data.owner }/${ data.name }/" class="href-home">
                    <div class="usa-card__container container-project-template">
                        <div class="text-container-project-template">
                            <div class="usa-card__header header-project-template">
                                <h2 class="usa-card__heading">${ data.name }</h2>
                            </div>
                            <div class="body-project-template">
                                <div>${ description }</div>
                            </div>
                            <div class="usa-card__footer footer-project-template">
                                <span class="star-count" style="margin-right: 15px;">
                                    <svg class="usa-icon" aria-labelledby="star-count-${data.name}-title" role="img">
                                    title id="github-${data.name}-title"> Star Count</title>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-star"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                                    </svg>

                                    <span> ${ data.stargazers_count } </span>
                                </span>
                                <span class="fork-count" style="margin-right: 15px;">
                                    <svg class="usa-icon" aria-labelledby="fork-count-${data.name}-title" role="img">
                                    <title id="github-${data.name}-title"> Fork Count</title>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-git-fork"><circle cx="12" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><circle cx="18" cy="6" r="3"/><path d="M18 9v2c0 .6-.4 1-1 1H7c-.6 0-1-.4-1-1V9"/><path d="M12 12v3"/></svg>
                                    </svg>
                                    <span> ${ data.forks_count } </span>
                                </span>
                                <span class="issue-count" style="margin-right: 15px;">
                                    <svg class="usa-icon" aria-labelledby="issue-count-${ data.name }-title" role="img">
                                    <title id="github-{{data.name}}-title"> Issue Count</title>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-circle-dot"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="1"/></svg>
                                    </svg>
                                    <span> ${ data.issues_count } </span>
                                </span>
                                <span class="pull-request-count" style="margin-right: 15px;">
                                    <svg class="usa-icon" aria-labelledby="pull-request-count-${data.name}-title" role="img">
                                    <title id="github-${data.name}-title"> Pull Request Count</title>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-git-pull-request"><circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M13 6h3a2 2 0 0 1 2 2v7"/><line x1="6" x2="6" y1="9" y2="21"/></svg>
                                    </svg>
                                    <span> ${ data.pull_requests_count } </span>
                                </span>
                                <span class="watchers-count">
                                    <svg class="usa-icon" aria-labelledby="watchers-count-${data.name}-title" role="img">
                                    <title id="github-${data.name}-title"> Watchers Count</title>
                                    <svg xmlns="http://www.w3.org/2000/svg" width="17" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-eye"><path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/></svg>                </svg>
                                    <span> ${ data.watchers_count } </span>
                                </span>
                            </div>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    `;
}

// const itemsPerPage = 10;

// export function renderProjectCards(page, data) {
//     console.log({data})
//     const projectCardList = document.querySelector('.project-card-list');
//     projectCardList.innerHTML = '';

//     const startIndex = (page - 1) * itemsPerPage;
//     const endIndex = startIndex + itemsPerPage;
   
//     const paginatedProjects = projects.slice(startIndex, endIndex);

//     paginatedProjects.forEach(project => {
//         projectCardList.innerHTML += projectCardTemplate(project); 
//     });
   
//     updatePaginationControls(page, projects);
// }

// export function updatePaginationControls(currentPage, projects) {
//     const totalPages = Math.ceil(projects.length / itemsPerPage);
//     const paginationContainer = document.querySelector('.usa-pagination__list');
//     paginationContainer.innerHTML = ''; 

//     const prevButton = document.createElement('li');
//     prevButton.className = 'usa-pagination__item usa-pagination__arrow';
//     prevButton.innerHTML = `
//         <a href="#" class="usa-pagination__link usa-pagination__previous-page" aria-label="Previous page" onclick="handlePageChange(${currentPage - 1})">
//             <span class="usa-pagination__link-text">Previous</span>
//         </a>
//     `;
//     if (currentPage === 1) prevButton.classList.add('disabled'); 
//     prevButton.addEventListener('click', (e) => {
//         e.preventDefault();
//         if(currentPage > 1) handlePageChange(currentPage - 1)
//     })
//     paginationContainer.appendChild(prevButton);

//     for (let i = 1; i <= totalPages; i++) {
//         const pageButton = document.createElement('li');
//         pageButton.className = 'usa-pagination__item usa-pagination__page-no';
//         pageButton.innerHTML = `
//             <a href="#" class="usa-pagination__button ${i === currentPage ? 'active' : ''}" aria-label="Page ${i}" onclick="handlePageChange(${i})">
//                 ${i}
//             </a>
//         `;
//         pageButton.addEventListener('click', (e) => {
//             e.preventDefault();
//             handlePageChange(i)
//         })
//         paginationContainer.appendChild(pageButton);
//     }

//     const nextButton = document.createElement('li');
//     nextButton.className = 'usa-pagination__item usa-pagination__arrow';
//     nextButton.innerHTML = `
//         <a href="#" class="usa-pagination__link usa-pagination__next-page" aria-label="Next page" onclick="handlePageChange(${currentPage + 1})">
//             <span class="usa-pagination__link-text">Next</span>
//         </a>
//     `;
//     if (currentPage === totalPages) nextButton.classList.add('disabled'); 
//     nextButton.addEventListener('click', (e) => {
//         e.preventDefault();
//         if(currentPage > 1) handlePageChange(currentPage + 1)
//     })
//     paginationContainer.appendChild(nextButton);
// }

// export function handlePageChange(page) {
//     const totalPages = Math.ceil(projects.length / itemsPerPage);
//     if (page < 1 || page > totalPages) {
//         console.error('Invalid page number', page)
//         return; 
//     }
//     renderProjectCards(page, projects);
// }

// renderProjectCards(1, projects);

  