import os

# Create directory
os.makedirs('mapeamento-da-iris', exist_ok=True)

# Main Hub Page
hub_content = '''---
layout: page
title: Mapeamento da Íris
permalink: /mapeamento-da-iris/
---

Aqui você encontra tudo sobre o fascinante mundo do Mapeamento da Íris e da Iridologia, organizado por tópicos para facilitar o seu estudo.

### Navegue pelos assuntos:

* [Escolas de Iridologia](/mapeamento-da-iris/escolas/)
* [Autores da Iridologia](/mapeamento-da-iris/autores/)
* [História da Iridologia](/mapeamento-da-iris/historia/)
* [Fundamentos da Iridologia](/mapeamento-da-iris/fundamentos/)
* [Livros de Iridologia](/mapeamento-da-iris/livros/)
* [Artigos Científicos da Iridologia](/mapeamento-da-iris/artigos/)

---
*Escolha um dos tópicos acima para ver todos os artigos publicados sobre o tema.*
'''
with open('mapeamento-da-iris.md', 'w', encoding='utf-8') as f:
    f.write(hub_content)


def create_subpage(slug, title, search_terms):
    content = f'''---
layout: page
title: {title}
permalink: /mapeamento-da-iris/{slug}/
---

<p><a href="/mapeamento-da-iris/">← Voltar para Mapeamento da Íris</a></p>

Abaixo você encontra todos os nossos artigos relacionados a **{title}**.

<div class="entries-list">
{{% for post in site.posts %}}
  {{% assign match = false %}}
  {{% for term in page.search_terms %}}
    {{% assign term_down = term | downcase %}}
    {{% assign title_down = post.title | downcase %}}
    {{% assign tags_string = post.tags | join: " " | downcase %}}
    
    {{% if title_down contains term_down or tags_string contains term_down %}}
      {{% assign match = true %}}
    {{% endif %}}
  {{% endfor %}}

  {{% if match %}}
    <article class="entry">
      <header class="entry-header">
        <h3 class="entry-title">
          <a href="{{{{ post.url | relative_url }}}}">{{{{ post.title }}}}</a>
        </h3>
      </header>
      {{% if site.show_excerpts %}}
        <div class="entry-excerpt">
          <p>{{{{ post.excerpt | strip_html | truncatewords: 30 }}}}</p>
        </div>
      {{% endif %}}
    </article>
  {{% endif %}}
{{% endfor %}}
</div>
'''
    # We will pass the search terms in the front matter so Liquid can use it easily
    # Actually, liquid array in front matter:
    terms_yaml = "\n".join([f"  - {t}" for t in search_terms])
    
    final_content = f'''---
layout: page
title: {title}
permalink: /mapeamento-da-iris/{slug}/
search_terms:
{terms_yaml}
---
<p><a href="/mapeamento-da-iris/">← Voltar para Mapeamento da Íris</a></p>

Abaixo você encontra todos os nossos artigos e estudos relacionados a **{title}**.

<ul class="post-list">
{{% assign count = 0 %}}
{{% for post in site.posts %}}
  {{% assign match = false %}}
  {{% for term in page.search_terms %}}
    {{% assign term_down = term | downcase %}}
    {{% assign title_down = post.title | downcase %}}
    {{% assign tags_string = post.tags | join: " " | downcase %}}
    
    {{% if title_down contains term_down or tags_string contains term_down %}}
      {{% assign match = true %}}
    {{% endif %}}
  {{% endfor %}}

  {{% if match %}}
    {{% assign count = count | plus: 1 %}}
    <li>
      <h3><a href="{{{{ post.url | relative_url }}}}">{{{{ post.title }}}}</a></h3>
      <p>{{{{ post.excerpt | strip_html | truncatewords: 25 }}}}</p>
    </li>
  {{% endif %}}
{{% endfor %}}
</ul>

{{% if count == 0 %}}
  <p><em>Ainda não publicamos artigos especificamente sobre este tópico, mas novidades chegarão em breve!</em></p>
{{% endif %}}
'''
    with open(f'mapeamento-da-iris/{slug}.md', 'w', encoding='utf-8') as f:
        f.write(final_content)

create_subpage('escolas', 'Escolas de Iridologia', ['escolas', 'escola '])
create_subpage('autores', 'Autores da Iridologia', ['autor', 'autores', 'pioneiro', 'quem foi'])
create_subpage('historia', 'História da Iridologia', ['história', 'historia', 'origem'])
create_subpage('fundamentos', 'Fundamentos da Iridologia', ['fundamento', 'ciência', 'ciencia', 'base', 'avaliação'])
create_subpage('livros', 'Livros de Iridologia', ['livro', 'obra', 'publicação'])
create_subpage('artigos', 'Artigos Científicos da Iridologia', ['artigo', 'científico', 'cientifico', 'estudo', 'pesquisa'])

print("Pages created successfully!")
