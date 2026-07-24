---
layout: page
title: Psicodélicos
permalink: /disciplinas/psicodelicos/
---

Aqui você encontra todas as postagens sobre **Psicodélicos**.

<div class="entries-list">
{% assign search_term = "Psicodélicos" | downcase %}
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
  <p><em>Ainda não há postagens classificadas exatamente como "Psicodélicos". Explore a busca geral do blog!</em></p>
{% endif %}
</div>
