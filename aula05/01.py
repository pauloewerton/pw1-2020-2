# Listas servem para armazenar um conjunto de dados de mesmo tipo ou nao
notas=[0,0,0] # alternativa: notas = [0] * 3
soma=0
x=0
while x<3:
    notas[x]=float(input(f"Nota {x + 1}: "))
    soma += notas[x]
    x+=1
x=0
while x<3:
    print(f"Nota {x + 1}: {notas[x]:6.2f}")
    x+=1
print(f"Média: {(soma / x):5.2f}")