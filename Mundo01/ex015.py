'''Exercício 015 - Aluguel de Carros
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
e R$0,15 por Km rodado.'''

dias = int(input('Informe a quantidade de dias alugados: '))
km = float(input('Informe a quantidade de Km percorridos: '))

preco = dias * 60 + km * 0.15

print(f'\nO preço total a ser pago é: R${preco:.2f}')
