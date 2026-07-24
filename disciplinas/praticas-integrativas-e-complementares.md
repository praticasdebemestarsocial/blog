---
layout: page
title: Práticas Integrativas e Complementares
permalink: /disciplinas/praticas-integrativas-e-complementares/
---

Aqui você encontra todas as postagens sobre **Práticas Integrativas e Complementares**.

<div class="entries-list">
{% assign search_term = "Práticas Integrativas e Complementares" | downcase %}
{% assign posts = "" | split: "" %}

{% for post in site.posts %}
  {% assign post_tags = post.tags | join: " " | downcase %}
  {% assign post_categories = post.categories | join: " " | downcase %}
  {% if post_tags contains search_term or post_categories contains search_term %}
    {% assign posts = posts | push: post %}
  {% endif %}
{% endfor %}

{% if posts.size > 0 %}
  {% for post in posts %}
    {% include entry.html %}
  {% endfor %}
{% else %}
  <p><em>Ainda não há postagens classificadas exatamente como "Práticas Integrativas e Complementares". Explore a busca geral do blog!</em></p>
{% endif %}
</div>
