# usando funcoes para tarefas de validacao
def faixa_int(pergunta, mínimo, máximo): 
    while True:
        v=int(input(pergunta)) 
        if v<mínimo or v>máximo:
            print("Valor inválido. Digite um valor entre %d e %d" % (mínimo,máximo)) 
        else:
            return v

resultado = faixa_int("Digite um valor entre 5 e 10: ", 5, 10)
print("o valor digitado foi: " + str(resultado))