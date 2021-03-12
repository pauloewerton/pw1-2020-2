# definicao de funcoes menores, anonimas
a=lambda x: x*2 # usamos a palavra reservada lambda seguida de uma tupla de parametros
print(a(3))

# funcoes lambda devem ser usadas para rotinas simples e repetitivas
aumento=lambda a,b: (a*b/100) # apenas uma linha
print(aumento(100, 5))