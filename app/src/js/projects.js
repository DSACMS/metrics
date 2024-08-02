const filterBox = document.getElementById("filter-input");
const projectSections = document.querySelectorAll(".project_section");
const checkboxes = document.querySelectorAll('input[type="checkbox"]');

// Add event listener to each checkbox
checkboxes.forEach(function (checkbox) {
  checkbox.addEventListener('change', function () {
    updateFilters();
  });
});

// Function to update filters
function updateFilters() {
  const selectedFilters = []

  // const repoData = document.getElementById('dedupliFHIR-data').textContent;
  // const parsedData = JSON.parse(repoData);
  // console.log(parsedData)


  const siteDataScript = document.getElementById('dedupliFHIR-data');
  console.log(siteDataScript)

  // Get selected categories
  document.querySelectorAll('input:checked').forEach(function (checkbox) {
      selectedFilters.push(checkbox.value);
  });

  console.log(selectedFilters)
  
  // Get filter tags div from DOM
  const selectedFiltersContainer = document.getElementById('filter-tags');
  selectedFiltersContainer.innerHTML = '';

  // Manipulate the DOM to create buttons based on the selected filters
  const filtersButtonGroup = document.createElement('div');
  filtersButtonGroup.className = "usa-button-group";
  selectedFiltersContainer.appendChild(filtersButtonGroup);

  selectedFilters.forEach(filter => {
    const filterButton = document.createElement('button');
    filterButton.className = 'usa-button margin-bottom-1';
    filterButton.textContent = filter;
    filtersButtonGroup.appendChild(filterButton);
  });
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
