def retângulo(largura, altura, caractere="*"): 
    linha = caractere * largura
    for i in range(altura):
        print(linha)

retângulo(3,4)
retângulo(3,4, caractere="-")
retângulo(largura=3, altura=4)
retângulo(altura=4, largura=3) # utilizando parametros nomeados, a ordem pode mudar
retângulo(caractere="-", altura=4, largura=3)
# isso aqui nao pode, iniciou nomeando tem que terminar!
#retângulo(largura=3, 4)
#retângulo(largura=3, altura=4, "*")