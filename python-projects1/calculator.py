
#Funcoes

def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro! Divisões por 0 não são possíveis."
    
    #Main Calculadora

def calculadora():

    #Menu
    print("Escolha a operação")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite o número da operação desejada|1|2|3|4|: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    
    #Condição de escolha

    if escolha == '1':
        print("Resultado: ", adicionar(num1, num2))
    elif escolha == '2':
        print("Resultado: ", subtrair(num1, num2))
    elif escolha =='3':
        print("Resultado: ", multiplicar(num1, num2))
    elif escolha == '4':
        print("Resultado: ", dividir(num1, num2))    
    else:
        print("Opção inválida! Escolha outra por favor.")            

calculadora()
