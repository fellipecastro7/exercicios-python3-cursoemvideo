'''Exercício 065 - Maior e Menor valores
Crie um programa que leia vários números inteiros pelo teclado. No final da execução leia a média
entre todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.'''

flag = False
media = 0
num_digitados = 0
maior = -99999
menor = 99999

while flag is False:
    num = int(input('Insira um número: '))
    num_digitados += 1
    media += num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    opcao = input('Deseja continuar inserindo números? [S / N] ').strip().upper()

    if opcao == 'N':
        flag = True
        print(f'Média: {media / num_digitados:.2f}\nMaior valor: {maior}\nMenor valor: {menor}')

    elif opcao == 'S':
        flag = False

    else:
        print('Opção inválida! Digite "S" ou "N".')
        flag = True
