---
layout: post
title: "Demonstração de Markdown: Explorando todas as possibilidades"
description: "Um post de teste para visualizar como os diferentes elementos do Markdown são renderizados no tema So Simple."
date: 2026-07-20 18:30:00 -0300
categories: [Testes, Markdown]
tags: [demo, jekyll, formatação]
---

Este é um parágrafo inicial para testar como o texto normal é exibido. O Markdown é uma linguagem de marcação leve e muito poderosa, ideal para escrever posts em blogs!

## Formatação de Texto Básica

Você pode usar várias formatações de texto no meio dos seus parágrafos:
* Este texto está em **negrito** (usando asteriscos duplos).
* Este texto está em *itálico* (usando asteriscos simples).
* Podemos também ter ***negrito e itálico*** ao mesmo tempo.
* E que tal um texto ~~riscado~~ para mostrar algo que foi corrigido?

## Citações (Blockquotes)

Sempre que você quiser destacar uma citação de algum autor famoso ou um trecho importante, você pode usar blocos de citação:

> "A simplicidade é o último grau de sofisticação." 
> — Leonardo da Vinci

> Você também pode aninhar citações!
>> Como esta citação aqui, que está dentro da primeira.

## Listas

Temos diferentes tipos de listas para organizar informações.

### Listas Não Ordenadas (Marcadores)
- Item 1
- Item 2
  - Sub-item 2.1
  - Sub-item 2.2
    - Sub-sub-item 2.2.1
- Item 3

### Listas Ordenadas (Numéricas)
1. Primeiro passo
2. Segundo passo
   1. Detalhe do segundo passo
   2. Outro detalhe
3. Terceiro passo

### Listas de Tarefas (Checklists)
- [x] Limpar as postagens de teste antigas
- [x] Criar uma postagem nova de demonstração
- [ ] Configurar o título e o nome do autor
- [ ] Publicar no mundo!

## Links e Imagens

Adicionar [Links para outros sites](https://google.com) é super simples.

E também podemos adicionar imagens. Aqui vai um exemplo de uma imagem de paisagem puxada diretamente do Unsplash:

![Uma paisagem bonita](https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80)
*Legenda: As imagens ficam responsivas automaticamente no tema So Simple.*

## Tabelas

As tabelas são ótimas para exibir dados estruturados:

| Funcionalidade | Suportado nativamente? | Dificuldade |
| :--- | :---: | ---: |
| Negrito e Itálico | Sim | Fácil |
| Tabelas | Sim | Média |
| Equações Matemáticas | Sim (via MathJax) | Difícil |

*(Note que podemos alinhar as colunas à esquerda, centro ou direita)*

## Códigos (Code Blocks)

Se você escreve sobre tecnologia, pode inserir blocos de código com destaque de sintaxe (Syntax Highlighting). 

Um código no meio do texto fica assim: `console.log("Olá Mundo");`.

Já um bloco inteiro fica assim (exemplo em Python):

```python
def saudacao(nome):
    """
    Função simples para saudar o usuário.
    """
    mensagem = f"Olá, {nome}! Bem-vindo ao seu novo blog."
    print(mensagem)
    return True

saudacao("Silviane")
```

## Divisórias

Quando quiser separar grandes seções do seu post, use uma linha horizontal:

---

### Conclusão

Esses são os principais recursos do Markdown suportados nativamente pelo Jekyll. A partir daqui, você pode usar e abusar desses blocos para escrever seus artigos!
