'''Exercício 035 - Analisando triângulo v1.0
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo.'''

r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\nCom essas três retas é possível formar um triângulo.')
else:
    print('\nCom essas três retas não é possível formar um triângulo.')
