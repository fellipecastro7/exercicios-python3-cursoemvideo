'''Exercício 059 - Criando um Menu de Opções
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
print('\n=-=-=- MENU DE OPÇÕES -=-=-=')
print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n')

flag = False

while flag is False:
    opcao = int(input('Informe a sua opção: '))

    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é igual a {soma}\n')

    elif opcao == 2:
        m = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é igual a {m:.2f}\n')

    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}\n')
        else:
            print(f'{num2} é maior que {num1}\n')

    elif opcao == 4:
        num1 = float(input('Informe o primeiro número: '))
        num2 = float(input('Informe o segundo número: '))

    elif opcao == 5:
        flag = True

    else:
        print('Erro! Entre com alguma das opções do menu.')
