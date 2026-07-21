# Blog - Práticas de Bem-Estar Social

Este repositório contém o código-fonte do blog estático, migrado do Blogger para o **Jekyll**.

## Estrutura do Projeto

- `_posts/`: Contém todos os artigos do blog em formato Markdown.
- `assets/`: Arquivos estáticos (CSS, imagens, JavaScript).
- `_layouts/` e `_includes/`: Estrutura HTML e templates do tema.
- `migrar_posts.py`: Script em Python utilizado para converter o XML do Blogger e fazer o upload das imagens.

## Como Rodar Localmente

Para testar o site na sua máquina e visualizar as alterações antes da publicação:

### Pré-requisitos
- **Ruby** (versão 2.7 ou superior)
- **Bundler** (`gem install bundler`)

### Instalação

1. Clone o repositório e acesse a pasta:
   ```bash
   git clone https://github.com/praticasdebemestarsocial/blog.git
   cd blog
   ```
2. Instale as dependências listadas no `Gemfile`:
   ```bash
   bundle install
   ```

### Iniciando o Servidor

Execute o comando abaixo para iniciar o Jekyll:
```bash
bundle exec jekyll serve
```
O blog ficará disponível em **http://localhost:4000**. As atualizações serão feitas automaticamente (live reload) sempre que você salvar um arquivo.

## Como Criar Novos Posts

Os posts devem ser salvos na pasta `_posts/` seguindo o formato de nomeclatura `ANO-MES-DIA-titulo-do-post.md` (ex: `2024-05-10-dicas-de-saude.md`).

Todo post deve começar com um **Frontmatter** em YAML. Exemplo:

```yaml
---
layout: post
title: "Título do seu Post"
date: 2024-05-10 14:00:00 -0300
categories: ["Bem Estar", "Saúde"]
image: "https://i.ibb.co/url-da-imagem.jpg"
---
```

Logo abaixo dos três traços (`---`), você pode escrever o conteúdo do seu post em Markdown.

## Publicação e Deploy

O blog utiliza o **GitHub Pages** (ou GitHub Actions). Sempre que um novo commit for feito no branch de produção, o Jekyll será compilado automaticamente e o site será atualizado.

---
*Nota: Este projeto é baseado no tema [So Simple Jekyll Theme](https://mmistakes.github.io/so-simple-theme/). A documentação original do tema pode ser consultada na web caso precise de detalhes avançados sobre sua estilização.*
