# Concerns

- **ImgBB API Limit:** Se as chaves expirarem ou baterem num limite diário, o script `migrar_posts.py` pode falhar no upload. (Mitigado pelo uso do `imgbb_cache.json`).
- **Links Quebrados Internos:** A migração do Blogger pode deixar links cruzados apontando para `.html` do antigo domínio ao invés da sintaxe interna. Seria interessante fazer um refactor futuramente nestes URLs se eles existirem.
- **Live Reload:** Amarrando o desenvolvedor à dependência de Ruby+Bundler nativos no sistema.
