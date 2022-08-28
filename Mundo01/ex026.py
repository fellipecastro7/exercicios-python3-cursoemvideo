'''Exercício 026 - Primeira e última ocorrência de uma string
Faça um programa que leia uma frase pelo teclado e mostre:
-> Quantas vezes aparece a letra "A".
-> Em que posição ela aparece a primeira vez.
-> Em que posição ela aparece a última vez.'''

frase = input('Digite uma frase: ').strip().upper()

cont_a = frase.count('A')
posicaoI = frase.find('A') + 1
posicaoF = frase.rfind('A') + 1

print(f'\nA letra "A" aparece {cont_a} vezes nessa frase.')
print(f'A letra "A" aparece pela primeira vez na posição {posicaoI}.')
print(f'A letra "A" aparece pela última vez na posição {posicaoF}.')
