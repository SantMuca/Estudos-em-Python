lista_de_tarefas = []

def adicionar_tarefa():
    print("\n--- Adicionar Tarefa ---")
    tarefa1 = input("Digite o nome da tarefa: ")
    nova_tarefa = {"nome": tarefa1, "concluida": False}
    lista_de_tarefas.append(nova_tarefa)
    print(f"Tarefa '{tarefa1}' adicionada com sucesso!")

def ver_tarefas():
    print("\n--- Suas Tarefas ---")
    if not lista_de_tarefas:
        print("Você não tem tarefas no momento. Que tal adicionar uma nova?")
    else:
        for i, tarefa in enumerate(lista_de_tarefas):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i + 1}. {tarefa['nome']} [{status}]")

def concluir_tarefa():
    print("\n--- Concluir Tarefa ---")
    ver_tarefas()
    
    if not lista_de_tarefas:
        return 

    escolha = int(input("\nDigite o número da tarefa que deseja concluir: "))
    indice = escolha - 1
    
    if 0 <= indice < len(lista_de_tarefas):
        lista_de_tarefas[indice]["concluida"] = True
        print(f"Tarefa '{lista_de_tarefas[indice]['nome']}' marcada como concluída!")
    else:
        print("Número de tarefa inválido! Tente novamente.")

def remover_tarefa():
    print("\n--- Remover Tarefa ---")
    ver_tarefas()
    
    if not lista_de_tarefas:
        return

    escolha = int(input("\nDigite o número da tarefa que deseja remover: "))
    indice = escolha - 1
    
    if 0 <= indice < len(lista_de_tarefas):
        tarefa_removida = lista_de_tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida['nome']}' removida com sucesso!")
    else:
        print("Número de tarefa inválido! Tente novamente.")

def principal():
    while True:
        print("\n" + "="*30)
        print("📝 GERENCIADOR DE TAREFAS")
        print("="*30)
        print("1. Adicionar uma tarefa")
        print("2. Ver todas as tarefas")
        print("3. Concluir uma tarefa")
        print("4. Remover uma tarefa")
        print("5. Sair")
        
        escolha = input("\nEscolha uma opção (1-5): ")

        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            ver_tarefas()
        elif escolha == '3':
            concluir_tarefa()
        elif escolha == '4':
            remover_tarefa()
        elif escolha == '5':
            print("Salvando tudo e encerrando... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    principal()