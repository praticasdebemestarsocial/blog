---
layout: page
title: Fundamentos da Iridologia
permalink: /mapeamento-da-iris/fundamentos/
show_excerpts: true
search_terms:
  - fundamento
  - ciência
  - ciencia
  - base
  - avaliação
---
<p><a href="/mapeamento-da-iris/">← Voltar para Mapeamento da Íris</a></p>

Abaixo você encontra todos os nossos artigos e estudos relacionados a **Fundamentos da Iridologia**.

<div class="entries-list">
{% assign count = 0 %}
{% for post in site.posts %}
  {% assign match = false %}
  {% for term in page.search_terms %}
    {% assign term_down = term | downcase %}
    {% assign title_down = post.title | downcase %}
    {% assign tags_string = post.tags | join: " " | downcase %}
    
    {% if title_down contains term_down or tags_string contains term_down %}
      {% assign match = true %}
    {% endif %}
  {% endfor %}

  {% if match %}
    {% assign count = count | plus: 1 %}
    {% assign entry = post %}
    {% include entry.html %}
  {% endif %}
{% endfor %}
</div>

{% if count == 0 %}
  <p><em>Ainda não publicamos artigos especificamente sobre este tópico, mas novidades chegarão em breve!</em></p>
{% endif %}
