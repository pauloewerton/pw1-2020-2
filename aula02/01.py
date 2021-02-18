a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b:  # os dois pontos indicam início de um novo bloco
    print("O primeiro valor é o maior!")  # a indentação é importante
if b > a:  # novo bloco, fora do anterior pois a indentação é no mesmo nível
    print("O segundo valor é o maior!")
