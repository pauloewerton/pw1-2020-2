tupla = ("a", "b", "c")
print(tupla)
print(tupla[0])
print(tupla[2])
print(tupla[1:])
print(tupla * 2)
print(len(tupla))
#tupla[0]="A"
for elemento in tupla: 
    print(elemento)
# empacotamento de valores
tupla = 100, 200, 300
print(tupla)
# desempacotamento de valores
a, b = 10, 20
print(a)
print(b)
L=[1,2,3]
T=tuple(L) # transforma lista em tupla
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2) # concatenacao