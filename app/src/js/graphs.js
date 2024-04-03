window.showGraph = function (selectedGraphId, className, buttonName) {
  const graphs = document.querySelectorAll("." + className)

  graphs.forEach((graph) => {
    const button = document.querySelector("#" + buttonName + graph.id)

    if (
      graph.id == selectedGraphId &&
      button.classList.contains("usa-button--outline")
    ) {
      // Shows selected graph
      graph.style.display = "block"
      button.classList.remove("usa-button--outline")
    } else {
      // Hides rest of graphs
      graph.style.display = "none"
      button.classList.add("usa-button--outline")
    }
  })
}
