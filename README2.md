# Como Rodar o Blog Localmente

Este projeto utiliza **Jekyll**, um gerador de sites estáticos feito em Ruby. Siga os passos abaixo para instalar as dependências e rodar o projeto na sua máquina após clonar o repositório.

## Pré-requisitos
Você precisará ter instalado no seu computador:
- **Ruby** (e o DevKit associado, caso esteja no Windows)
- **Bundler** (gerenciador de dependências do Ruby)

## Instalação

1. Abra o terminal na pasta raiz do projeto.
2. Execute o comando abaixo para instalar todas as dependências necessárias listadas no `Gemfile`:
   ```bash
   bundle install
   ```
   *Nota: Esse processo pode demorar alguns minutos dependendo da sua conexão.*

## Rodando o Projeto

Após a instalação das dependências, você pode iniciar o servidor local do Jekyll:

```bash
bundle exec jekyll serve
```

O Jekyll irá compilar o site e fornecer um endereço local. Geralmente, você poderá acessar o blog no seu navegador através do endereço:
**http://localhost:4000**

O servidor continuará rodando no terminal e vai atualizar o site automaticamente (live reload) sempre que você salvar um arquivo. Para parar o servidor, pressione `Ctrl + C` no terminal.
