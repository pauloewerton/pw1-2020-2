from nomes import Nome

A=Nome("Paulo")
print(A)
#print(A.__nome) # erro
# print(A.__chave) # erro
print(A.chave)
#A.chave="paulo ewerton" #erro nao pode setar direatmente
A.nome="Paulo Ewerton"
print(A.chave)
print(Nome.CriaChave("Um Nome"))