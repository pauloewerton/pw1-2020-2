# decoradores em python
def hello(func):                                                                                            
    # definimos uma funcao empacotadora
    def inner():
        # adicionamos algo novo (decoramos) a chamada a func
        print("Hello ")
        # chamamos a funcao decorada
        func()
    return inner # retornamos a funcao interna
                                                                                                            
def name():
    print("Alice")
                                                                                                            
obj = hello(name) # dizemos que a funcao name esta sendo decorada com hello
obj()  