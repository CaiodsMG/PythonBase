primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

if primeiro_valor > segundo_valor:
    print(f'o primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'o segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}')
else:
    print(f'Os valores são iguais!')

