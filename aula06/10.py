def hello(func):                                                                                            
    def inner():
        print("Hello ")
        func()
    return inner

@hello # outra forma de decorar name com hello, igual a obj = hello(name)
def name():
    print("Alice")

name()