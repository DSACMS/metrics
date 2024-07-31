const filterBox = document.getElementById("filter-input")
const projectSections = document.querySelectorAll(".project_section")
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

  // Get selected categories
  document.querySelectorAll('input:checked').forEach(function (checkbox) {
      selectedFilters.push(checkbox.value);
      console.log(checkbox.value)
  });

  console.log(selectedFilters)
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
