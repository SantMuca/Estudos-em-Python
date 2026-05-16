# Projetos Solo - Estudos em Python 🐍

Bem-vindo(a) ao meu repositório de projetos solo!
Este espaço é dedicado a armazenar e documentar a minha jornada de estudos na linguagem Python. Aqui, desenvolvo projetos práticos para aplicar conceitos fundamentais de programação, evoluindo desde aplicações simples baseadas em linha de comando até sistemas web estruturados.

---

## 💻 Projetos Incluídos

Até o momento, este repositório contém os seguintes projetos detalhados:

### 1. 🧮 Calculadora Contínua (Terminal)

Uma aplicação interativa via linha de comando que simula o funcionamento lógico de uma calculadora física de mesa. O programa executa operações matemáticas elementares e gerencia fluxos operacionais ininterruptos.

* **Diferenciais e Recursos:**
* **Memória de Estado:** Armazena o resultado do último cálculo e o utiliza automaticamente como o primeiro valor para a próxima operação.
* **Fluxo de Controle Dinâmico:** Oferece um comando de reinicialização (`c`) que limpa a memória acumulada e redefine o estado operacional do programa, além de uma opção de saída graciosa.
* **Validação Robusta:** Proteção ativa contra falhas clássicas de execução, como a inserção de caracteres não numéricos e tentativas de divisão por zero.


* **Conceitos Aplicados:** Estruturação de funções modulares, loops infinitos de controle estrutural (`while True`), tratamento de exceções em tempo de execução (`try/except` com `ValueError` e `ZeroDivisionError`) e gerenciamento de variáveis com escopo global e estados nulos (`None`).

### 2. 📝 Gerenciador de Tarefas (To-Do List - Terminal)

Um sistema de gerenciamento básico baseado em terminal que simula operações de persistência de dados em memória RAM. O projeto foi projetado para exercitar a navegação por menus estruturados e manipulação de arranjos de dados estruturados.

* **Diferenciais e Recursos:**
* **Menu de Navegação:** Interface textual orientada por opções numéricas para direcionar as ações do usuário.
* **Operações CRUD em Memória:** Mapeamento completo para Adicionar (Create), Listar (Read), Marcar status (Update) e Excluir tarefas (Delete).
* **Feedback de Status:** Exibição dinâmica de índices e rótulos contextuais que identificam visualmente se uma tarefa está "Pendente" ou "Concluída".


* **Conceitos Aplicados:** Estruturas de dados compostas (Listas contendo dicionários chave-valor), indexação iterativa com a função nativa `enumerate()`, manipulação de elementos via métodos de lista (como `.append()` e `.pop()`), e uso avançado de operadores ternários para otimização de condicionais textuais.

### 3. 🌐 Painel de Tarefas Web (Flask & JSON Full-Stack)

A evolução natural do gerenciador de terminal para uma plataforma web real. Este aplicativo Full-Stack combina a robustez lógica do Python no back-end com uma interface moderna, responsiva e de alta fidelidade visual no front-end.

* **Diferenciais e Recursos:**
* **Rigor Visual e UI/UX:** Layout minimalista e elegante projetado com fontes tipográficas selecionadas (`Instrument Serif` e `DM Sans`), paleta de cores harmonizada via variáveis CSS (`:root`), efeitos de iluminação radial e animações fluidas de carregamento (`fadeUp` e `slideDown`).
* **Painel de Estatísticas Automatizado:** Um bloco inteligente no topo da página que calcula e exibe em tempo real o total de tarefas registradas, o volume de pendências e o índice de itens concluídos.
* **Banco de Dados baseado em Arquivo (.json):** Integração com o sistema de arquivos local para ler e salvar os dados. Desligar o servidor ou reiniciar a máquina não apaga as informações.
* **Sanfona Interativa (Acordeão) com Seta Dinâmica:** Uso de JavaScript nativo para ocultar e revelar painéis de descrição longa de cada tarefa. As setas indicadoras rotacionam suavemente entre os estados fechado (`▶`) e aberto (`▼`).
* **Edição Inline Dinâmica:** Um botão de edição substitui a visualização normal da tarefa por um formulário pré-preenchido na própria linha, permitindo alterar títulos e anotações instantaneamente sem trocar de página.
* **Confirmação e Segurança:** Filtros que ocultam botões desnecessários (como "Concluir" em tarefas já finalizadas) e alertas pop-up nativos para validação de exclusões.


* **Conceitos Aplicados:** Desenvolvimento web com micro-framework Flask, arquitetura de Rotas Dinâmicas (`@app.route` aceitando parâmetros tipados como `<int:indice>`), processamento de requisições HTTP (GET/POST), herança e injeção de templates com Jinja2 (filtros `| length` e `| selectattr`), manipulação assíncrona do DOM (Document Object Model) via JavaScript, tratamento seguro de arquivos vazios e serialização/desserialização de strings através do módulo `json`.

---

## 🛠 Tecnologias e Ferramentas Utilizadas

* **Core:** Python 3.x
* **Web Framework:** Flask
* **Persistência:** JSON (JavaScript Object Notation)
* **Front-end:** HTML5, CSS3 (Flexbox/Variables/Keyframes), JavaScript Embutido
* **Design & Tipografia:** Google Fonts, Ícones estruturados em vetores SVG nativos

---
