saida =''
def adicao(a,b):
    return a + b
def subtracao(a,b):
    return a - b
def multiplicacao(a,b):
    return a * b
def divisao(a,b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por 0"
def calculadora(a,b,operacao):
    if operacao == '+':
        return adicao(a,b)
    elif operacao == '-':
        return subtracao(a,b)
    elif operacao == '*':
        return multiplicacao(a,b)
    elif operacao == '/':
        return divisao(a,b)
    else:
        print('operação invalida')
while saida.lower() != 'n':
    try:
        a = float(input('Digite o primeiro numero: '))
        b = float(input('Digite o segundo numero: '))
        operacao = input('Escolha a operação entre (+, , - , ,*, , / ): ')

        resultado = calculadora(a,b,operacao)
        print('resultado da operação: ', resultado)
    except ValueError:
        print('Operacao invalida')
    saida = input('deseja Realizar outra operação [S/N]?: ')

