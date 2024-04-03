window.showGraph = function(graphId) {
    const graphs = document.querySelectorAll('.graph');
    graphs.forEach(graph => {
      if (graph.id == graphId) {
        graph.style.display = 'block';
      } else {
        graph.style.display = 'none';
      }
    });
  };