from model.Pessoa import Pessoa
from database.PessoaDAO import PessoaDAO
from util.Color import *


class Medico(Pessoa):
    def __init__(self, nome, cpf, senha, especializacao, salario, pessoa_id=None, id=None):
        super().__init__(nome, cpf, senha, pessoa_id)
        self.especializacao=especializacao
        self.salario=salario
        self.id=id

    def menu(self):
        print("Bem vindo, " + CYAN + self.nome + RESET)

    @staticmethod
    def cadastrar(sistema):
        from database.MedicoDAO import MedicoDAO

        print()
        print(BLUE + "CADASTRO MÉDICO" + RESET)
        nome = input("Nome: ")
        cpf = input("CPF: ")
        pessoa = PessoaDAO().getPessoaByCPF(cpf)
        if pessoa != None:
            print(RED + "CPF já cadastrado." + RESET)
            sistema.menuPrincipal()
            return

        senha = input("Senha: ")
        especializacao = input("Especialização: ")
        salario = float(input("Salário: "))
        medico = Medico(nome, cpf, senha, especializacao, salario)
        MedicoDAO().insert(medico)
        print()