'''Exercício 048 - Soma ímpares múltiplos de três
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se
encontram no intervalo de 1 até 500.'''

soma = 0

for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            soma += i
print(f'Somatório: {soma}')
