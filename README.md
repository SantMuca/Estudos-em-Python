# Tarefas (Flask CRUD Application) 🐍

Um gerenciador de tarefas web completo e profissional, construído com Python e o micro-framework Flask. O projeto evoluiu de uma aplicação simples de terminal para uma plataforma web Full-Stack com persistência de dados em JSON e uma interface de usuário moderna e responsiva.

---

## 💻 Recursos Atuais

Este projeto implementa um sistema CRUD completo, focado na experiência do usuário e na organização.

### 🚀 Novas Funcionalidades Web:

* **Interface Web Moderna:** Design minimalista e elegante inspirado no `Instrument Serif` e `DM Sans`, com paleta de cores centralizada e animações suaves (`fadeUp`, `slideDown`).
* **CRUD Completo no Navegador:**
    * **Criar (Create):** Adicionar tarefas via formulário interativo (com título e descrição opcional).
    * **Ler (Read):** Visualizar a lista completa de tarefas pendentes e concluídas.
    * **Atualizar (Update):**
        * Marcar tarefas como concluídas com feedback visual (linha tachada, cor verde).
        * **Edição Inline:** Modificar o título e a descrição de tarefas existentes diretamente na linha da tarefa, sem sair da página, mantendo o status atual.
    * **Deletar (Delete):** Remover tarefas com uma confirmação de segurança (pop-up nativo) para evitar exclusões acidentais.
* **Persistência de Dados em JSON:** Todas as tarefas são salvas no arquivo `tarefas.json`, garantindo que os dados não sejam perdidos ao reiniciar o servidor.
* **Lógica Dinâmica com Jinja2:** Painel de estatísticas em tempo real (Total, Pendentes, Concluídas) e geração de IDs únicos para interação (sanfonas, edição).
* **Interatividade com JavaScript:** Lógica de sanfona (acordeão) para expandir/retrair descrições com setinhas dinâmicas (`▶` e `▼`), confirmações de exclusão e controle de visibilidade dos formulários.
* **Design Responsivo:** Adaptado para telas de celulares e desktops.
* **Personalização de Marca:** Logo customizada (`logo.png`) integrada ao cabeçalho.

---

## 🛠 Habilidades Praticadas

Este projeto foi essencial para consolidar conhecimentos Full-Stack:

* **Python:** Lógica de CRUD aplicada, manipulação de estruturas de dados (Listas de Dicionários), funções e tratamento de exceções.
* **Flask:** Criação de rotas dinâmicas, gerenciamento de contexto de requisições (`request`, `redirect`), renderização de templates (`render_template`).
* **JSON:** Serialização e desserialização de dados para persistência.
* **HTML:** Estruturação avançada (`<form>`, `<textarea>`, `<svg>`), semântica e acessibilidade.
* **Jinja2:** Uso de loops (`for`), condicionais (`if/else`), definição de variáveis (`{% set %}`), filtros (`| length`, `| selectattr`) e manipulação de loops mágicos (`{{ loop.index0 }}`).
* **CSS:** Uso de variáveis (`:root`), design responsivo (`@media`), animações (`@keyframes`, `transition`), tipografia (Google Fonts) e posicionamento flexível.
* **JavaScript:** Manipulação do DOM (`getElementById`), controle de visibilidade (`display`), troca de conteúdo (`innerText`) e lógica de interação.

---

## 🚀 Como Executar o Projeto

Certifique-se de ter o Python e o Flask instalados.

1.  Clone este repositório.
2.  Abra o terminal na pasta do projeto (`Projeto_Web`).
3.  Instale o Flask, se necessário:
    ```bash
    pip install flask
    ```
4.  Certifique-se de que a estrutura de pastas é:
    ```text
    Projeto_Web/
    ├── app.py
    ├── tarefas.json  (Opcional, será criado automaticamente)
    ├── templates/
    │   └── index.html
    └── static/
        └── logo.png
    ```
5.  Para rodar a aplicação, execute:
    ```bash
    python app.py
    ```
6.  Abra o navegador no endereço indicado (geralmente `http://127.0.0.1:5000`).

---

*Repositório focado no aprendizado contínuo e evolução na engenharia de software Full-Stack.* 🚀
