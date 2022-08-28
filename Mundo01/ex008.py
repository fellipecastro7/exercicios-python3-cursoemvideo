'''Exercício 008 - Conversor de Medidas
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

v = float(input('Digite um valor (em metros): '))
print(f'\nO valor convertido em quilômetros é {v / 1000}km')
print(f'O valor convertido em hectômetros é {v / 100}hm')
print(f'O valor convertido em decâmetros é {v / 10}dam')
print(f'O valor convertido em decímetros é {v * 10}dm')
print(f'O valor convertido em centímetros é {v * 100}cm')
print(f'O valor convertido em milímetros é {v * 1000}mm')
