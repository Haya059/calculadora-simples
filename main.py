operacao = input('Você deseja fazer uma conta de mais, menos, vezes ou dividir? ')

def mensagem_resultado(resultado):
    print(f'O resultado é: {resultado}')

def somar():
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite um outro número: '))
    soma = numero1 + numero2
    mensagem_resultado(soma)

def subtrair():
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite um outro número: '))
    diferenca = numero1 - numero2
    mensagem_resultado(diferenca)

def multiplicar():
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite um outro número: '))
    produto = numero1 * numero2
    mensagem_resultado(produto)

def dividir():
    numero1 = int(input('Digite um número: '))
    numero2 = int(input('Digite um outro número: '))
    razao = numero1 / numero2
    mensagem_resultado(razao)


if operacao == 'mais':
    somar()
elif operacao == 'menos':
    subtrair()
elif operacao == 'vezes':
    multiplicar()
elif operacao == 'dividir':
    dividir()
else:
    print('Operação não reconhecida')