a=5 # definindo a variavel global a
def muda_e_imprime():
    global a
    a=7 # aqui e uma variavel local a
    print("A dentro da função: %d" % a)
print("a antes de mudar: %d" % a)
muda_e_imprime()
print("a depois de mudar: %d" % a)