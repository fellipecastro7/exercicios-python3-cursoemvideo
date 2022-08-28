'''Exercício 040 - Aquele clássico da Média
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'\nSua média é de {media:.1f}\n\033[31mREPROVADO!\033[m')
elif 5 <= media <= 6.9:
    print(f'\nSua média é de {media:.1f}\n\033[36mRECUPERAÇÃO!\033[m')
else:
    print(f'\nSua média é de {media:.1f}\n\033[32mAPROVADO!\033[m')
