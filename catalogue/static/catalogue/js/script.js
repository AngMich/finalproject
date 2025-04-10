setTimeout(function() {
    const container = document.getElementById('message-container');
    if (container) {
      container.style.transition = "opacity 0.1s";
      container.style.opacity = 0;
      setTimeout(() => container.remove(), 500);
    }
  }, 3000);
  