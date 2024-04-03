window.showGraph = function(graphId) {
    const graphs = document.querySelectorAll(".graph");
    
    graphs.forEach(graph => {
      const button = document.querySelector("#button-" + graph.id);

      if (graph.id == graphId && button.classList.contains("usa-button--outline")) {
        // Shows selected graph
        graph.style.display = 'block';
        button.classList.remove("usa-button--outline");
      } else {
        // Hides rest of graphs
        graph.style.display = 'none';
        button.classList.add("usa-button--outline");
      }
    });
  };