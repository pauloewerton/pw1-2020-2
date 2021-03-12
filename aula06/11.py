# passando parametros para a funcao o decorador
def hello(func):                                                                                            
    def inner(a, b):
        print(str(a) + " + " + str(b) + " = ", end="")
        # e preciso retornar o valor da chamada se quisermos usa-lo
        return func(a, b)
    return inner

@hello
def soma(a, b):
    return a + b

print(soma(2, 2))