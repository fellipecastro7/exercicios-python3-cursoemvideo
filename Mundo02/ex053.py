'''Exercício 053 - Detector de Palíndromo
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
espaços'''

frase = input('Digite uma frase: ').strip()

fraseM = frase.replace(' ', '')
inverso = ''

for i in range(len(fraseM) - 1, -1, -1):
    inverso += fraseM[i]
if inverso == fraseM:
    print('Trata-se de um palíndromo.')
else:
    print('Não se trata de um palíndromo.')
