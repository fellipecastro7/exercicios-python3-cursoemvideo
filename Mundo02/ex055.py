'''Exercício 055 - Maior e menor da sequência
Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso
lidos.'''

maior = 0
menor = 99999

for i in range(5):
    peso = float(input('Informe o seu peso (kg): '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'Maior peso: {maior:.1f}kg\nMenor peso: {menor:.1f}kg')
