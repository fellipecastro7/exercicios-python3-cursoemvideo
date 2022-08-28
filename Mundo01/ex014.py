'''Exercício 014 - Conversor de Temperaturas
Crie um programa que converta uma temperatura digitando em °C e converta para °F.'''

c = int(input('Digite a temperatura em °C: '))

f = (c * 9 / 5) + 32

print(f'\nA temperatura de {c}°C corresponde a {f}°F.')
