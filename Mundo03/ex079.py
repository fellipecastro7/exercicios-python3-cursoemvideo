'''Exercício 079 - Valores únicos em uma Lista
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.'''

lista = []

while True:
    num = int(input('Insira um número: '))

    if num not in lista:
        lista.append(num)

    else:
        print('Número já existente na lista. Tente outro...')

        while True:
            num = int(input('Insira um número: '))

            if num in lista:
                lista.append(num)
                break

    opcao = input('Deseja continuar cadastrando números? [S/N] -> ').strip().upper()

    while opcao not in 'SN' or opcao in '':
        opcao = input('Deseja continuar cadastrando números? [S/N] -> ').strip().upper()

    if opcao == 'N':
        break

print(lista)
