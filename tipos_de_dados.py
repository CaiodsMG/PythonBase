# Aqui deixarei salvo todos os tipos de dados e exemplos.

#Usando os argumentos sep e end (separar e pra quebra de linhas)

print(12, 34, sep='/', end='\n') #trás um output com os números separados por uma barra (/)
print(56, 78, sep='-', end='\n') #trás um output com os números separados por um traço (-)

# String - Textos dentro de aspas simples ou duplas.
print('Caio Guilherme')
print("Caio Guilherme")

# Int e Float - Números inteiros ou qualquer outro número

print(11) #int
print(-11) #int
print(1.1) #float - separado por um ponto(.)
print(0.0) #float
print(-5,3) #float

# Type - Retorna o tipo inferido ao valor.
print(type('Caio')) # retorno = str.
print(type(1.1)) # retorno = float.  
print(type(3)) # retorno = int.

# Boolean (bool) - retorna true ou false questionando se um valor é igual a outro.
print(10 == 10) # True (Verdadeiro)
print (10 == 9) # False (Falso)

# conversão de tipos

print(int("1"), type(int("1"))) # converte para tipo inteiro o que antes era uma string.
print(str(1), type(str(1))) # converte para string o que antes era um inteiro.