# desempacotando elementos passados como uma lista
def soma(*args):
    s=0
    for x in args: 
        s+=x
    return s 

def imprime_maior(mensagem, *numeros): 
    maior = None
    for e in numeros:
        if maior == None or maior < e:
            maior = e 
    print(mensagem, maior)
    
print(soma(1,2))
print(soma(2))
print(soma(5,6,7,8))
print(soma(9,10,20,30,40))

imprime_maior("Maior: ",5,4,3,1) 
imprime_maior("Max: ", *[1,7,9])
imprime_maior("Max: ")
imprime_maior()