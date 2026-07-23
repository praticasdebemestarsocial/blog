---
layout: search
title: "Pesquisar no Blog"
permalink: /search/
---

<script>
  window.addEventListener('DOMContentLoaded', (event) => {
    // Pega o parametro 'q' da URL
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get('q');
    
    if (query) {
      // Coloca o termo na caixa de busca
      const searchInput = document.getElementById('search');
      if (searchInput) {
        searchInput.value = query;
        // Dispara o evento de 'keyup' e 'input' para forçar o script de busca do tema a rodar
        searchInput.dispatchEvent(new Event('input', { bubbles: true }));
        searchInput.dispatchEvent(new KeyboardEvent('keyup', { bubbles: true }));
      }
    }
  });
</script>
