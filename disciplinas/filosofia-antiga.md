---
layout: page
title: Filosofia Antiga
permalink: /disciplinas/filosofia-antiga/
---
Aqui vocÃª encontra todas as postagens sobre **Filosofia Antiga**.

<div class="entries-list">
{% assign search_term = "Filosofia Antiga" | downcase %}
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
  <p><em>Ainda nÃ£o hÃ¡ postagens classificadas exatamente como "Filosofia Antiga". Explore a busca geral do blog!</em></p>
{% endif %}
</div>
