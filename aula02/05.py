minutos = int(input("Quantos minutos você utilizou este mês: "))

if minutos < 200:
    preço = 0.20
else:
    if minutos < 400: # este bloco if está dentro do else, o alinhamento é importante!
        preço = 0.18
    else:
        preço = 0.15

print(f"Você vai pagar este mês: R${minutos * preço:6.2f}") # o 'f' antes da string indica um formato
print("Você vai pagar este mês: R${:6.2f} ".format(minutos * preço)) # é equivalente a chamar a função format