# listas dentro de listas
compras = [ ] # compras e uma lista de listas!
while True:
    produto = input("Produto: ") 
    if produto == "fim":
        break
    quantidade = int(input("Quantidade: ")) 
    preço = float(input("Preço: ")) 
    compras.append([produto, quantidade, preço]) # uma lista para cada produto
soma = 0.0
for e in compras:
    print("%20s x%5d %5.2f %6.2f" % (e[0], e[1],e[2], e[1] * e[2]))
    soma += e[1] * e[2]
print("Total: %7.2f" % soma)