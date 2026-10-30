// Choosing and Running Local LLMs with Ollama — static site scripts
// Asdale Dynamics, LLC — MIT License, Copyright (c) 2026 Asdale Dynamics, LLC

document.addEventListener('DOMContentLoaded', function () {
  // Highlight the current nav link
  const current = window.location.pathname.split('/').pop() || 'index.html';
  const links = document.querySelectorAll('.site-nav a');
  links.forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === current || (current === 'index.html' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // Print button for worksheet
  const printBtn = document.getElementById('print-worksheet');
  if (printBtn) {
    printBtn.addEventListener('click', function () {
      window.print();
    });
  }

  // Model chip copy-to-clipboard helper
  document.querySelectorAll('.copy-model').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const code = btn.getAttribute('data-model');
      navigator.clipboard.writeText(code).then(function () {
        const old = btn.textContent;
        btn.textContent = 'Copied!';
        setTimeout(function () { btn.textContent = old; }, 1200);
      });
    });
  });
});
