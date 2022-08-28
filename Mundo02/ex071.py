'''Exercício 071 - Simulador de Caixa Eletrônico
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
valor serão entregues.

OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=-' * 16)
print('\tCAIXA ELETRÔNICO')
print('=-' * 16)
valor = int(input('Insira o valor a ser sacado: R$'))

total = valor
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1

    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula:.2f}')

        if cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 1

        total_cedula = 0

        if total == 0:
            break
