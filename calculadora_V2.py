saida = ''

def adicao(numero1, numero2):
    return int(numero1) + int(numero2)

def subtracao(numero1, numero2):
    return int(numero1) - int(numero2)

def multiplicacao(numero1, numero2):
    return int(numero1) * int(numero2)

def divisao(numero1, numero2):
    if numero1 == 0 or numero2 == 0:
        return 'Não foi possível realizar a divisão por 0'
    else:
        return int(numero1) / int(numero2)


def calculadora(n1, n2, operacao):
    if operacao == "+":
        resultado = adicao(n1, n2)
    
    elif operacao == "-":
        resultado = subtracao(n1,n2)

    elif operacao == "*":
        resultado = multiplicacao(n1,n2)

    elif operacao == "/":
        resultado = divisao(n1,n2)

    else:
        resultado = "operacao invalida"

    return resultado

while saida.lower() != "n":
    entrada1 = int(input('Digite um número qualquer: '))
    entrada2 = int(input('Digite outro número qualquer: '))
    entrada3 = input('Digite a operação que quer realizar: ')
    resultado = calculadora(entrada1, entrada2, entrada3)
    print("Resultado da operação: ", resultado)

    saida = input('deseja contunuar? S/N ')








    
