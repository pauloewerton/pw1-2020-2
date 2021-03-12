def pesquise(lista, valor): 
    return valor if valor in lista else None;

def soma(L):
    total=0
    for e in L:
        total+=e

    return total 

def media(L):
    return(soma(L)/len(L))

L=[10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))
print(media(L))