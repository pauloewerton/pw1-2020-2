x =1
soma = 0 # utilizacao de acumulador
while x <= 5:
    n = int(input("Digite o %do número: " % x))
    soma = soma + n # acumulacao a cada iteracao do laco
    x = x + 1
print(f"Média: {(soma / 5):5.2f}") # usando acumulador para calcular media