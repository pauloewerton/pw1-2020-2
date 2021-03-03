L = [7, 9, 10, 12]
p = int(input("Digite um número a pesquisar: "))
for e in L: # busca linear com for e break
    if e == p:
        print("Elemento encontrado!")
        break
else:
    print("Elemento não encontrado.")
