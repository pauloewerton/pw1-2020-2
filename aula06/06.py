def barra():
    print("*" * 40) # nao e uma funcao muito generica :(

# usando parametros opcionais
def barra_opt(n=40, caractere="*"): 
    print(caractere * n)

# parametros obrigatorios e opcionais
def soma(a, b, imprime=False):  
    s=a+ b
    if imprime: 
        print(s)
    return s

barra()
barra_opt()
barra_opt(10)
barra_opt(10, '-')
print(soma(2, 2))
soma(2, 2, True)