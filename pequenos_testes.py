"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input(f'Digite um número inteiro: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print(f'{numero_int} é um número par.')
#     else:
#         print(f'É um número impar ')
# else:
#     print('Esse não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)
#     if hora >= 0 and hora <= 11:
#        print(f'Bom dia.')
#     elif hora >= 12 and hora <= 17:
#        print(f'Boa tarde.')
#     elif hora >= 18 and hora <= 23:
#        print(f'Boa noite.')
#     else:
#        print('Digite uma hora válida')
# except:
#    print('Digite apenas números inteiros.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
letras_nome = len(nome)

if letras_nome >= 1 and <= 4:
    print(f'{nome} Seu nome é curto')
elif letras_nome <= 6:
    print(f'{nome} Seu nome é normal')
elif letras_nome >= 7:
    print(f'{nome} Seu nome é muito grande')
else:
    print(f'Digite um nome válido')

