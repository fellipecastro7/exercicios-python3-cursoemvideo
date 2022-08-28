'''Exercício 018 - Seno, Cosseno e Tangente
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
desse ângulo.'''

from math import sin, cos, tan, radians
angulo = int(input('Informe o valor do ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'\nO ângulo de {angulo}°, tem:')
print(f'Seno igual a {seno:.2f}')
print(f'Cosseno igual a {cosseno:.2f}')
print(f'Tangente igual a {tangente:.2f}')
