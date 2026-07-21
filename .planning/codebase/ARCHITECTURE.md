# Architecture

O projeto segue a arquitetura padrão de geradores de sites estáticos.

1. **Entrada (Source):** Arquivos Markdown armazenados na pasta `_posts/` com YAML Frontmatter definindo os metadados (título, data, categorias, imagem de destaque).
2. **Processamento (Build):** O Jekyll lê o `_config.yml`, compila o Markdown em HTML, aplica os templates (`_layouts`, `_includes`) e os arquivos CSS (`_sass`).
3. **Saída (Site):** O site compilado é gerado na pasta `_site` (ignorada no git) e servida pelo GitHub Pages na produção.

O script `migrar_posts.py` atua em uma etapa pré-build, pegando um `feed.atom` offline e gerando os arquivos `.md` brutos.
