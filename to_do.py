def menu():
    print("""
======== To-Do List ========
1 - Adicionar Tarefa
2 - Mostrar Tarefas
3 - Excluir Tarefa
4 - Sair
============================
""")

# Função para adicionar uma tarefa 
def adicionarTarefa(lista):
    tarefa = input("Digite a nova tarefa: ")
    lista.append(tarefa)  # Adiciona a nova tarefa
    print("Tarefa adicionada com sucesso!")

# Função para mostrar todas as tarefas
def mostrarTarefas(lista):
    if lista:
        print("\n--- Suas Tarefas ---")
        for i, tarefa in enumerate(lista, start=1):
            print(f"{i} - {tarefa}")
    else:
        print("\nNenhuma tarefa na lista!")

# Função para excluir uma tarefa 
def excluirTarefas(lista):
    mostrarTarefas(lista)
    if lista:
        try:
            numero = int(input("\nDigite o número da tarefa que deseja excluir: "))
            if 1 <= numero <= len(lista):
                tarefa_removida = lista.pop(numero - 1)  # Remove a tarefa pelo índice
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Por favor, digite um número válido!")
    else:
        print("Não há tarefas para excluir!")

# Função principal
def main():
    lista = []
    while True:
        menu()
        op = input("Escolha uma opção: ")

        if op == "1":
            adicionarTarefa(lista)
        elif op == "2":
            mostrarTarefas(lista)
        elif op == "3":
            excluirTarefas(lista)
        elif op == "4":
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Roda o programa
main()
