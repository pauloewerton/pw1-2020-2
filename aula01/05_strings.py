# Mais de uma forma de declarar

print('uma string')
print("também uma string")
print('eu quis dizer uma "string"')
print("eu quis dizer uma 'string'")

s = '''
uma super string
com várias linhas
'''
print(s)

# Tamanho de uma string

print(len('A'))
print(len('AB'))
print(len(''))
print(len(s))

# Acessando caracteres pela posição

a = 'ABCDEF'
print(a[0]) # comportamento similar ao uma lista!
print(a[1])
print(a[5])
#print(a[6])

# Concatenação e repetição

b = 'ABC'
print(b + 'C') # operador '+' é sobrecarregado em Python
print(b + 'D' * 4) # o '*' também!
print('X' + ('-' * 10) + 'X')
print(b + 'x4 = ' + (b * 4))

# Composição (subsituição) com marcadores
nome = 'João'
idade = 22
print('O participante [%s] tem [%d] anos.' % (nome, idade))

# Formatando a apresentação de decimais

print('%f' % 5)
print('%.2f' % 5) # Útil para imprimir valores monetários!
print('%10.5f' % 5)

# Tudo junto!
grana = 52.60
print('O participante [%s] tem [%d] anos e um total de R$ [%.2f].' % (nome, idade, grana))

# Fatiamento de strings
c = 'ABCDEFGHI'
print(c[0:2])
print(c[0:2])
print(c[1:2])
print(c[2:4])
print(c[0:5])
print(c[1:8])
print(c[:2]) # omitindo o início
print(c[1:]) # omitindo o fim
print(c[0:-2]) # índice negativo indica posição a partir do fim da string, ou seja a última posição é -1, a penúltima é -2, etc.
print(c[-1:])
print(c[-5:7])
print(c[-2:-1])