window.showGraph = function (selectedGraphId, className, buttonName) {
  const graphs = document.querySelectorAll("." + className)

  graphs.forEach((graph) => {
    const button = document.querySelector("#" + buttonName + graph.id)

    if (graph.id == selectedGraphId) {
      if (button.classList.contains("usa-button--outline")) {
          // Shows selected graph
          graph.style.display = "block";
          button.classList.remove("usa-button--outline");
      }
    } else {
      // Hides rest of graphs
      graph.style.display = "none";
      button.classList.add("usa-button--outline");
    }
  })
}

// goes inside includes/js for the time being
function toggleDateAge(element) {
  const dateSpan = element.querySelector('.date');
  const ageSpan = element.querySelector('.age');
  
  if (ageSpan.style.display === 'none') {
    dateSpan.style.display = 'none';
    ageSpan.style.display = 'inline';
  } else {
    dateSpan.style.display = 'inline';
    ageSpan.style.display = 'none';
  }
}