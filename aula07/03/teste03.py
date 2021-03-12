from clientes import Cliente
from bancos import Banco
from contas import Conta

joão = Cliente("João da Silva", "3241-5599")
maria = Cliente("Maria Silva", "7231-9955")
josé = Cliente("José Vargas","9721-3040")
contaJM = Conta( [joão, maria], 100)
contaJ = Conta( [josé], 10)
tatu = Banco("Tatú")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()