'''Exercício 066 - Vários números com flag
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag).'''

soma = num_digitados = 0

while True:
    num = int(input('Insira um número [999 PARA PARAR]: '))

    if num == 999:
        break

    num_digitados += 1
    soma += num

print(f'Números digitados: {num_digitados}\nSoma entre os números: {soma}')
