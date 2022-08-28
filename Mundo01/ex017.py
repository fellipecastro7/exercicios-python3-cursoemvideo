'''Exercício 017 - Catetos e Hipotenusa
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo, calcule e mostre o comprimento da hipotenusa.'''

from math import hypot
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
print(f'\nA hipotenusa é de {hypot(co, ca):.2f}')
