# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 
#  C a i o
# -4-3-2-1

# nome = 'Caio'
# print(nome[2])
# print(nome[-2])
# print('a' in nome) # checa se a letra 'a' está contida na variavel -- #True
# print('z' in nome) # checa se a letra 'z' está contida na variavel -- #False
# print(10 * '-')
# print('aio' not in nome) # checa se as letras "aio" não estão na varial -- #False
# print('bdz' not in nome) # checa se as letras "bdz" não estão na varial -- #True

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está dentro de {nome}')
else:
    print(f'{encontrar} não está dentro de {nome}')