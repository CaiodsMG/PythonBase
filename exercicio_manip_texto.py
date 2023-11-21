'''
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A útima letra do seu nome é {letra}
Se nada for digitado em idade:
Exiba:  
        "Desculpe, você deixou campos em vazios."
'''

nome = input('Digite o seu nome ')
idade = input('Digite sua idade ')

nome_invertido = nome[::-1]
quantidade_letras = len(nome)
primeira_letra = nome[0:1]
ultima_letra = nome[-1::]

if nome and idade != '':
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    if ' ' in nome:
        print(f'Seu nome tem espaços')
    else:
        print(f'Seu nome não tem espaços')
    print(f'Seu nome tem {quantidade_letras} letras')
    print(f'A primeira letra do seu nome é: {primeira_letra}')
    print(f'A ultima letra do seu nome é: {ultima_letra}')
    
    # print(f'A sua idade é: {idade}')
else:
    print(f'Desculpe, você deixou campos em vazios.')