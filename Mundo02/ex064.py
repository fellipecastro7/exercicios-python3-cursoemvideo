'''Exercício 064 - Tratando vários valores v1.0
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag).'''

flag = False
num_digitados = 0
soma = 0

while flag is False:
    num = int(input('Insira um número: '))

    if num != 999:
        num_digitados += 1
        soma += num

    else:
        flag = True
        print(f'Números digitados: {num_digitados}\nSoma entre os números: {soma}')
