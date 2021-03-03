# dicionarios
tabela = { "Alface": 0.45, "Batata": 1.20, "Tomate": 2.30,
           "Feijao": 1.50 }
while True:
    produto=input("Digite o nome do produto, fim para terminar: ") 
    if produto == "fim":
        break
    if produto in tabela: # verifica se a chave existe
        print("Preço %5.2f" % tabela[produto]) # captura o valor associado à chave
    else:
        print("Produto não encontrado!")