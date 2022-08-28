'''Exercício 036 - Aprovando Empréstimo
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o
empréstimo será negado.'''

valor_casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
anos = int(input('Informe em quantos anos você irá pagar: '))

meses = anos * 12
prestacao = valor_casa / meses

print(f'\nPara pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será', end=' ')
print(f'de R${prestacao:.2f}')

if prestacao <= salario * (30 / 100):
    print('EMPRÉSTIMO CONCEDIDO!')
else:
    print('EMPRÉSTIMO NEGADO!')
