const filterBox = document.getElementById("filter-input")
filterBox.addEventListener("input", () => {
  const query = filterBox.value.toLowerCase()
  document.querySelectorAll(".project-card").forEach((card) => {
    card.hidden = !(
      query == "" || card.textContent.toLowerCase().includes(query)
    )
  })
})