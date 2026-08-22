# 🎬 Locadora de Filmes — Estruturas de Dados

Projeto desenvolvido como desafio da disciplina de **Estruturas de Dados**, com o objetivo de aplicar, na prática, conceitos fundamentais de estruturas de dados por meio da implementação de um sistema de gerenciamento de uma locadora de filmes.

O sistema simula as principais operações de uma locadora, permitindo o cadastro e gerenciamento de filmes e clientes, realização de aluguéis e devoluções, gerenciamento de reservas e consulta dos filmes alugados recentemente.

## 📚 Estruturas de Dados Utilizadas

O projeto utiliza diferentes estruturas de dados implementadas em Python:

### 🔗 Lista Encadeada

A **lista encadeada** é utilizada como estrutura principal para armazenar os filmes da locadora.

Cada filme possui informações como:

* Título
* Gênero
* Diretor
* Classificação indicativa
* Ano de lançamento
* Código
* Situação do filme
* Fila de reservas

A lista possui operações para:

* ➕ Inserir filmes
* ❌ Remover filmes
* 🔎 Buscar filmes por título e gênero
* 📋 Listar filmes
* 🎭 Listar filmes por gênero
* 🔤 Ordenar filmes por gênero e título utilizando **Insertion Sort**

A implementação utiliza nós conectados por meio de ponteiros `next`, formando a estrutura da lista encadeada.

### 🧑‍🤝‍🧑 Fila de Reservas — FIFO

Cada filme possui sua própria **fila de reservas**, também implementada utilizando uma lista encadeada.

Quando um filme está alugado, outros clientes podem entrar na fila para reservá-lo. Quando o filme é devolvido, o primeiro cliente da fila recebe prioridade.

A estrutura segue o conceito:

> **FIFO — First In, First Out**

Ou seja, o primeiro cliente a entrar na fila é o primeiro a ser atendido.

A fila possui operações para:

* ➕ Adicionar cliente à fila
* ➖ Remover o primeiro cliente
* 👀 Consultar o primeiro cliente
* 📏 Verificar o tamanho da fila
* 📋 Visualizar os clientes em espera

Cada filme possui sua própria fila de reservas, mantendo o controle individual das solicitações.

### 📚 Pilha — LIFO

Uma **pilha** é utilizada para armazenar os filmes alugados recentemente.

A estrutura segue o conceito:

> **LIFO — Last In, First Out**

Cada novo aluguel é inserido no topo da pilha. Dessa forma, é possível consultar os **5 filmes alugados mais recentemente** no sistema.

---

## 🎯 Funcionalidades

### 👤 Área do Cliente

O cliente pode realizar seu cadastro utilizando informações como nome, idade, telefone e CPF. Após o cadastro, ele possui acesso ao menu de operações da locadora.

Entre as funcionalidades disponíveis estão:

* 🎬 Alugar um filme
* ↩️ Devolver um filme
* 🔎 Buscar um filme
* 🎭 Listar filmes por gênero
* 📋 Visualizar a fila de reservas
* 🚪 Sair do sistema

Durante o aluguel, o sistema verifica a **idade do cliente em relação à classificação indicativa do filme** e também verifica a disponibilidade do título.

Caso o filme esteja indisponível, o cliente pode ser adicionado automaticamente à fila de reservas.

Quando o filme é devolvido, caso existam clientes aguardando, o primeiro da fila recebe automaticamente o filme.

### 👨‍💼 Área do Funcionário

O sistema também possui um menu destinado ao funcionário da locadora, permitindo maior controle sobre os dados e operações do sistema.

O funcionário pode:

* ➕ Inserir novos filmes
* ❌ Remover filmes
* 🔎 Buscar clientes pelo CPF
* 📋 Visualizar filas de reserva
* 🔍 Buscar filmes
* 📑 Listar todos os filmes
* 🔤 Ordenar filmes por gênero
* 📚 Visualizar os 5 filmes alugados mais recentemente

Essas operações são disponibilizadas por meio de um menu interno específico para o funcionário.

---

## 🔤 Ordenação — Insertion Sort

Para a organização dos filmes foi implementado o algoritmo de ordenação **Insertion Sort**.

A ordenação considera primeiro o **gênero do filme em ordem alfabética**. Quando dois ou mais filmes possuem o mesmo gênero, seus títulos também são utilizados como critério de desempate, seguindo a ordem alfabética.

---

## 🏗️ Estrutura do Sistema

O projeto é organizado principalmente por meio das seguintes classes:

```text
Locadora
│
├── ListaDeFilmes
│   └── Node
│
├── SistemaClientes
│   └── Cliente
│
├── Pilha
│   └── NodePilha
│
└── FilaDeReservas
    └── NodeFila
```

A classe `Locadora` funciona como a classe principal do sistema, reunindo a lista de filmes, o sistema de clientes e a pilha de aluguéis recentes.

---

## 💻 Tecnologias

* **Python**
* Estruturas de Dados
* Programação Orientada a Objetos
* Lista Encadeada
* Fila
* Pilha
* Insertion Sort


## 🖥️ Funcionamento

Ao iniciar o programa, o usuário encontra a tela inicial da **Locadora PH** e pode informar se já possui cadastro.

A partir do CPF informado, o sistema identifica se o usuário é um funcionário ou um cliente cadastrado e direciona para o menu correspondente.

O sistema também inicia com alguns filmes previamente cadastrados, como *Matrix*, *Velozes e Furiosos*, *O Impossível* e *A Cinco Passos de Você*.

---

## 🎓 Objetivo Acadêmico

Este projeto foi desenvolvido com foco na aplicação prática dos conceitos estudados na disciplina de **Estruturas de Dados**.

Através da criação de uma locadora de filmes, foi possível trabalhar com diferentes estruturas e algoritmos, compreendendo na prática como **listas encadeadas, filas, pilhas e algoritmos de ordenação** podem ser utilizados para solucionar problemas de gerenciamento e organização de informações.

---

## 👩‍💻 Autora

**Paola Hanna de Moura Coutinho**

Estudante de Engenharia da Computação.

---

⭐ Projeto desenvolvido para fins acadêmicos.

