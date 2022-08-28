'''Exercício 063 - Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
primeiros elementos de uma Sequência de Fibonacci.'''

print('=-=-=- SÉRIE DE FIBONACCI -=-=-=')
termos = int(input('Insira a quantidade de termos da série: '))

a1 = 1
a2 = 1

if termos == 1:
    print('0')

elif termos == 2:
    print('0  1')

else:
    print(f'0  {a1}  {a2}', end='  ')
    i = 0

    while i < termos - 3:
        proximo = a1 + a2
        a2 = a1
        a1 = proximo
        print(proximo, end='  ')
        i += 1
