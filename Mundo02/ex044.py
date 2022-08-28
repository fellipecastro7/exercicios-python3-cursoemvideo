'''Exercício 044 - Gerenciador de Pagamentos
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

preco = float(input('Informe o preço do produto: R$'))
print('\n=-=-=-PAGAMENTO-=-=-=')
print('1 - à vista dinheiro/cheque\n2 - à vista no cartão\n3 - em até 2x no cartão')
print('4 - 3x ou mais no cartão\n')
opcao = input('Informe a sua opção: ').strip()

if opcao == '1':
    desconto = preco * (10 / 100)
    print(f'\nValor a ser pago (com 10% de desconto): R${preco - desconto:.2f}')
elif opcao == '2':
    desconto = preco * (5 / 100)
    print(f'\nValor a ser pago (com 5% de desconto): R${preco - desconto:.2f}')
elif opcao == '3':
    parcela = preco / 2
    print(f'\nSua compra será parcelada em 2x de R${parcela:.2f}')
    print(f'Valor a ser pago: R${preco:.2f}')
elif opcao == '4':
    total_parc = int(input('\nQuantas parcelas? '))
    juros = preco * (20 / 100)
    parcela = (preco + juros) / total_parc
    print(f'Sua compra será parcela em {total_parc}x de R${parcela:.2f}')
    print(f'Valor a ser pago (com 20% de juros): R${preco + juros:.2f}')
else:
    print('\nERRO! ENTRE COM ALGUMA DAS OPÇÕES ACIMA.')
