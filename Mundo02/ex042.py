'''Exercício 042 - Analisando Triângulos v2.0
Refaça o desafio 035 dos triângulos, adicionando o recurso de mostrar que tipo de triângulo será
formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\nCom essas três retas é possível formar um triângulo.')
    if r1 == r2 == r3:
        print('Triângulo Equilátero')
    if r1 == r2 or r1 == r3 or r2 == r3:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print('\nCom essas três retas não é possível formar um triângulo.')
