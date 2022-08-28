'''Exercício 034 - Aumentos múltiplos
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais o aumento é de 15%.'''

salario = float(input('Informe o seu salário: '))

if salario > 1250.00:
    aumento = salario * (10 / 100)
    novo_salario = salario + aumento
    print(f'\nO seu novo salário, com o aumento de 10%, é de {novo_salario:.2f}')
else:
    aumento = salario * (15 / 100)
    novo_salario = salario + aumento
    print(f'\nO seu novo salário, com o aumento de 15%, é de {novo_salario:.2f}')
