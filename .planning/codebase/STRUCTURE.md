# Structure

- `_posts/`: Diretório core onde todo o conteúdo reside (arquivos .md de datas sequenciais).
- `_layouts/` & `_includes/`: Templates do "So Simple Theme" que controlam o visual do site e os blocos de HTML reutilizáveis.
- `assets/`: Arquivos estáticos como CSS, Javascript e imagens adicionais (logotipos).
- `migrar_posts.py`: Script customizado escrito em Python para automação de exportação/limpeza dos dados do blogger.
- `imgbb_cache.json`: Cache offline das URLs das imagens para evitar chamadas duplicadas à API externa durante o script de migração.
- `_config.yml`: Arquivo principal de configuração do site, metadados globais e dependências.
