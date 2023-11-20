# Operador lógico NOT (não) - Inverte expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')
elif senha == '123456':
    print('Você acertou a senha')
else:
    print('Você errou a senha')