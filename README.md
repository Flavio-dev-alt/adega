# Sistema de Gerenciamento para Adega:
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

Este projeto nasceu como o trabalho final para a disciplina de **Programação I**, com o objetivo de colocar em prática os fundamentos da lógica de programação criando algo funcional e próximo de um cenário real: o dia a dia de uma adega. 

A ideia foi construir um sistema via terminal que ajude a organizar o estoque de bebidas, manter o cadastro de clientes em dia (respeitando a regra de negócio de venda apenas para maiores de 18 anos) e registrar cada venda realizada.

---

# O que o sistema faz na prática?

O sistema cobre o fluxo básico de um comércio, dividido em quatro módulos principais:

- **Controle de Clientes:** Permite cadastrar novos clientes, buscar quem já tem cadastro, atualizar dados e excluir registros. O sistema também faz a checagem de idade para garantir que apenas maiores de 18 anos comprem bebidas alcoólicas.
- **Gestão de Produtos:** Um controle de estoque onde dá para adicionar novas bebidas, consultar o que tem disponível, editar informações (como preço e quantidade) e remover itens.
- **Registro de Vendas:** Liga o cliente ao produto comprado, registrando a saída e mantendo o histórico organizado.
- **Relatório Geral:** Com um comando, o sistema mostra tudo o que ainda tem no estoque, lista as vendas feitas e calcula quanto entrou no caixa no total.

---

# O que eu usei para construir

- **Python 3:** Toda a lógica, menus e validações foram escritos em Python puro, aplicando os conceitos aprendidos na disciplina.
- **Arquivos de Texto (`.txt`):** Para garantir que os dados não fossem perdidos ao fechar o programa, utilizei manipulação de arquivos locais (`clientes.txt`, `produtos.txt` e `vendas.txt`) para simular a persistência de dados.

---

#  O que eu aprendi fazendo esse projeto

Desenvolver este sistema para a faculdade foi um marco importante no meu aprendizado. Os principais desafios superados foram:
- **Lidar com dados persistentes:** Aprender a ler, escrever e atualizar linhas específicas dentro de arquivos `.txt` sem corromper as informações.
- **Regras de negócio:** Implementar travas lógicas, como a validação de maioridade para a venda de produtos restritos.
- **Organização e Modularidade:** Dividir o código em funções claras para deixar o sistema limpo, organizado e fácil de manter.

---

# Para testar na sua máquina:

1. **Baixe o repositório:**
   ```bash
   git clone [https://github.com/Flavio-dev-alt/adega.git](https://github.com/Flavio-dev-alt/adega.git)
