fim = int(input("Digite o último número a imprimir: "))
x = 0 # utilizacao de contador
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1 # incrementa a cada iteracao do laco