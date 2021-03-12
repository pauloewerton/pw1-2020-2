def épar(x):
    return(x%2==0)

# pode ter diversar funcoes definidas em um script
def par_ou_ímpar(x): 
    # reutilizando a funcao epar em outra funcao
    if épar(x):
        return "par" 
    else:
        return "ímpar"

print(par_ou_ímpar(4)) 
print(par_ou_ímpar(5))