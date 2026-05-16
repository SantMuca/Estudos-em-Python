def adicionar(x, y):
    return x + y

def subtrair (x, y):
    return x - y

def multiplicar (x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y

def calculadora():
    print("___Calculadora___")
    print("Escolha a operação desejada: ")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("\nDigite o número da operação (1/2/3/4) ou 's' para sair: ")

        if escolha.lower() == 's':
                print("Encerrando... Até mais!")
                break

        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primieiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Por favor, digite apenas números.")
                continue
            
            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("Operação inválida! Escolha uma das opções (1, 2, 3 ou 4.)")

if __name__ == "__main__":
    calculadora()