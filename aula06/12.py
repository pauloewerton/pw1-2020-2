def soma(a,b): 
   print(a+b)

def barra(n=10, c="*"): 
    print(c*n)

# empacotando parametros em listas
L=[2,3] 
soma(*L) # usamos o operador * para indicar o empacotamento

L=[ [5, "-"], [10, "*"], [5], [6,"."] ] 
for e in L:
    barra(*e)