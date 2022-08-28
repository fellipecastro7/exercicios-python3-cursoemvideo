'''Exercício 037 - Conversor de Bases Numéricas
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

print('=-=-=-BASES DE CONVERSÃO-=-=-=')
print('\n- 1 para binário\n- 2 para octal\n- 3 para hexadecimal')
opcao = input('\nInforme a sua opção: ').strip()
num = int(input('Informe um número: '))

if opcao == '1':
    print(f'\nO número {num} convertido para binário é igual a {bin(num)[2:]}')
elif opcao == '2':
    conversao = format(num, 'o')
    print(f'\nO número {num} convertido para octal é igual a {oct(num)[2:]}')
elif opcao == '3':
    conversao = format(num, 'x')
    print(f'\nO número {num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print('\nErro! Você não entrou com nenhuma das opções acima.')
