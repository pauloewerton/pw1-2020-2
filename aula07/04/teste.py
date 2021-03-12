from nomes import Nome

A=Nome("Paulo")
print(A)
# B=Nome(" ") # invalido
# C=Nome(None) # invalido
print(A == Nome("Paulo"))
print(A != Nome("Paulo"))
print(A < Nome("Paulo"))
print(A > Nome("Paulo"))
print(A >= Nome("Paulo")) # erro, nao implementado
print(A <= Nome("Paulo")) # erro, nao implmentado
