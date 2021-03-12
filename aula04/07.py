s = 0
while True:
    v = int(input("Digite um número a somar ou 0 para sair: "))
    s = s + v
    if v != 0:
        continue 
    break
print(s)