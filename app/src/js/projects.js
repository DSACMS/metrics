const filterBox = document.getElementById("filter-input")
const reportHeadings = document.querySelectorAll(".report_heading")
const projectCards = document.querySelectorAll(".project-card")

filterBox.addEventListener("input", () => {
  const query = filterBox.value.toLowerCase()

  // Initiaize dictionary that tracks count of displayed cards under org
  const orgDict = {}
  reportHeadings.forEach(org => {
    const name = org.innerText.trim()
    orgDict[name] = 0;
  })

  // Performs query and hides project card accordingly.
  projectCards.forEach((card) => {
    card.hidden = !(
      query == "" || card.textContent.toLowerCase().includes(query)
    )

    // Updates count
    const org = card.getAttribute("org-name");
    if (!card.hidden) {
      orgDict[org] += 1
    }
  })

  // Displays org heading accordingly
  reportHeadings.forEach(org => {
    const name = org.innerText.trim()
    org.hidden = !orgDict[name];
  })
  
})