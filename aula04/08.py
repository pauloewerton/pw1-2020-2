tabuada = 1
while tabuada <= 10:
    numero = 1
    while numero <= 10: # aninhamento de lacos
        print("%d x %d = %d" % (tabuada, numero, tabuada * numero))
        numero += 1
    tabuada += 1
