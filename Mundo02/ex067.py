'''Exercício 067 - Tabuada v3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

num = 0

print('=-=-=- TABUADA -=-=-=')
while True:
    num = int(input('\nInsira um número para ver a sua tabuada [NEGATIVO PARA PARAR]: '))
    i = 1

    if num < 0:
        break

    while i <= 10:
        print(f'{num} x {i} = {num * i}')
        i += 1
