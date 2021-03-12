# para importar um objeto usamos import
#import entrada
from entrada import valida_inteiro

L=[]
for x in range(5):
    L.append(valida_inteiro("Digite um número entre 0 e 20: ", 0, 20)) 
print("Soma: %d" % (sum(L)))