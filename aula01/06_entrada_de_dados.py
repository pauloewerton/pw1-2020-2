# Usando a funcao input
x = input('Digite um numero: ')
print(x)

nome = input('Digite o seu nome: ')
print('Voce digitou "%s"' % nome)
print('Ola, %s!' % nome)

# Conversao da entrada
anos = int(input('Anos de servico: '))
valor_por_ano = float(input('Valor por ano: '))
bonus = anos * valor_por_ano
print('Bonus de R$ %5.2f' % bonus)

# Problemas de conversao
n = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
saldo = float(input('Digite o saldo de sua conta bancaria: '))
print(n)
print(idade)
print(saldo)