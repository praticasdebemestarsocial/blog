# Práticas de Bem-Estar Social

Este é um blog construído com [Jekyll](https://jekyllrb.com/) utilizando uma estrutura baseada no tema [So Simple Theme](https://github.com/mmistakes/so-simple-theme). Ele foi migrado a partir do Blogger e otimizado para melhor performance e SEO.

## 🚀 Como rodar localmente

Este projeto utiliza Ruby e Bundler para gerenciar as dependências do Jekyll. Não é necessário Docker.

1. Instale o [Ruby](https://rubyinstaller.org/) (se estiver no Windows, use o RubyInstaller).
2. Instale o Bundler executando:
   ```bash
   gem install bundler
   ```
3. Instale as dependências do projeto:
   ```bash
   bundle install
   ```
4. Inicie o servidor local do Jekyll:
   ```bash
   bundle exec jekyll serve
   ```
5. Acesse no navegador: `http://localhost:4000/blog/`

## 🛠️ Modificações e Ferramentas de Migração

- **Migração do Blogger:** 842 posts foram convertidos de XML/HTML para Markdown.
- **Limpeza de Links:** URLs quebradas, imagens duplicadas e erros de parsing (ex: `.gif).gif)`) foram corrigidos em lote com scripts Python.
- **Hospedagem de Imagens:** As imagens originais do Blogger foram migradas em parte para o **ImgBB** via API, e o restante foi baixado e hospedado localmente na pasta `assets/img/posts/`.
- **Correção da Home:** A renderização da página inicial e tags foi otimizada para evitar a duplicação de imagens representativas e prevenir vazamentos de links, desabilitando globalmente os excertos automáticos.

## 📂 Estrutura de Diretórios

- `_posts/` - Contém todos os posts em Markdown.
- `_includes/` - Componentes de layout (ex: `entry.html`).
- `assets/` - Imagens hospedadas localmente, CSS e JavaScript.
- `*.py` - Scripts utilitários de limpeza e migração do conteúdo antigo.
- `.planning/` - Logs gerados por agentes de automação do projeto.
