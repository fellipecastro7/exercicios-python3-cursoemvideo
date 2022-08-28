'''Exercício 057 - Validação de Dados
Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto.'''

sexo = input('Informe o seu sexo [M / F]: ').strip().upper()

while sexo not in 'MF':
    sexo = input('Erro! Entre com "M" ou "F": ').strip().upper()

print(f'Sexo "{sexo}" cadastrado com sucesso.')
