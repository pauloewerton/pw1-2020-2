# copia de listas
L=[1,2,3,4,5]
V=L  # atribuicoes apenas fazem ambas as variaveis apontarem para a mesma lista
print(V)
print(L)
V[0]=6
print(V)
print(L)
V=L[:]
V[0]=1
print(V)
print(L)