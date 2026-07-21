# Testing

- O teste principal se baseia no Build Local do Jekyll.
- Ao rodar `bundle exec jekyll serve`, o desenvolvedor deve acessar `http://localhost:4000` para validar se os templates Markdown foram devidamente renderizados.
- Não existem testes automatizados unitários no nível do Ruby (Jekyll), as validações são visuais e baseadas em logs de erro da compilação do Jekyll.
- Para o script em Python, erros na API de imagem e parsing são impressos no terminal (logs).
