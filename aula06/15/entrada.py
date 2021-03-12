# nossos scripts python tambem sao modulos (colecoes de objetos)
def valida_inteiro(mensagem, mínimo, máximo): 
    while True:
        try:
            v=int(input(mensagem))
            if v >= mínimo and v <= máximo:
                return v
            else:
                print("Digite um valor entre %d e %d" % (mínimo, máximo))
        except:
            print("Você deve digitar um número inteiro")