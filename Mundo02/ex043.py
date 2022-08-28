'''Exercício 043 - Índice de Massa Corporal
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

peso = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura: '))

imc = peso / altura ** 2

if imc < 18.5:
    print(f'\nIMC = {imc:.2f}kg/m²\nStatus: Abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'\nIMC = {imc:.2f}kg/m²\nStatus: Peso ideal')
elif 25 <= imc < 30:
    print(f'\nIMC = {imc:.2f}kg/m²\nStatus: Sobrepeso')
elif 30 <= imc < 40:
    print(f'\nIMC = {imc:.2f}kg/m²\nStatus: Obesidade')
else:
    print(f'\nIMC = {imc:.2f}kg/m²\nStatus: Obesidade mórbida')
