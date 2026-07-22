---
layout: page
title: Artigos Científicos da Iridologia
permalink: /mapeamento-da-iris/artigos/
search_terms:
  - artigo
  - científico
  - cientifico
  - estudo
  - pesquisa
---
<p><a href="/mapeamento-da-iris/">← Voltar para Mapeamento da Íris</a></p>

Abaixo você encontra todos os nossos artigos e estudos relacionados a **Artigos Científicos da Iridologia**.

<ul class="post-list">
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
    <li style="margin-bottom: 20px;">
      <h3 style="margin-bottom: 5px;"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p style="margin-top: 0;">{{ post.excerpt | strip_html | truncatewords: 25 }}</p>
    </li>
  {% endif %}
{% endfor %}
</ul>

{% if count == 0 %}
  <p><em>Ainda não publicamos artigos especificamente sobre este tópico, mas novidades chegarão em breve!</em></p>
{% endif %}
