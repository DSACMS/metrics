const filterBox = document.getElementById("filter-input")
const projectSections = document.querySelectorAll(".project_section")

filterBox.addEventListener("input", () => {
  const query = filterBox.value.toLowerCase()

  // Iterate through each section
  projectSections.forEach(section => {
    var queryMatchCheck = false
    const projectCards = section.querySelectorAll(".project-card")

    // Performs query and hides project card accordingly
    projectCards.forEach((card) => {
      card.hidden = !(
        query == "" || card.textContent.toLowerCase().includes(query)
      )

      if(!card.hidden) {
        queryMatchCheck = true
      }
    })

    // Hide heading if all cards under section are hidden
    const reportHeadings = section.querySelector(".report_heading")
    reportHeadings.hidden = !queryMatchCheck
  })
})