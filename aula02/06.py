categoria = int(input("Digite a categoria do produto: "))

# vários if-else aninhados
if categoria == 1:
    preço = 10
else:
    if categoria == 2:
        preço = 18
    else: # vários níveis de indentação dificultam a leitura do código
        if categoria == 3:
            preço = 23
        else:
            if categoria == 4:
                preço = 26
            else:
                if categoria == 5:
                    preço = 31
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5!") # validação da entrada
                    preço = 0

print(f"O preço do produto é: R${preço:6.2f}")