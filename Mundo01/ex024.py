'''Exercício 024 - Verificando as primeiras letras de um texto
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.'''

cidade = input('Informe o nome de sua cidade: ').strip()

cidade1 = cidade[:5].upper() == 'SANTO'

print(f'\nSua cidade é {cidade}')
print(f'Começa com SANTO? {cidade1}')
