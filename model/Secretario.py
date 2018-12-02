from model.Pessoa import Pessoa
from model.Consulta import Consulta
from database.PessoaDAO import PessoaDAO
from database.ConsultaDAO import ConsultaDAO
from database.MedicoDAO import MedicoDAO
from database.PacienteDAO import PacienteDAO
from datetime import datetime
from util.Color import *


class Secretario(Pessoa):
    def __init__(self, nome, cpf, senha, salario, pessoa_id=None, id=None):
        super().__init__(nome, cpf, senha, pessoa_id)
        self.salario=salario
        self.id=id

    def menu(self, sistema):
        print("Bem vindo, " + CYAN + self.nome + RESET)
        print()
        print("1) Ver consultas pendentes")
        print("2) Sair")

        try:
            op = int(input("=> "))

            if op == 1:
                self.verConsultas(sistema)
            elif op == 2:
                sistema.menuPrincipal()
            else:
                raise ValueError()

        except ValueError:
            print("Opção inválida.")
            self.menu(sistema)

    def verConsultas(self, sistema):
        consultas = ConsultaDAO().getAllPendente()

        if (len(consultas) == 0):
            print(GREEN + "Não há consultas." + RESET)
            self.menu(sistema)
        else:
            print(BLUE + "Consultas: " + RESET)
            for i, con in enumerate(consultas):
                med = MedicoDAO().getByID(con.medico_id)
                print(str(i) + ") Consulta com " + med.nome)

            op = int(input("=> "))

            try:
                con = consultas[op]
                con.infoConsulta(sistema)

                paciente = PacienteDAO().getByID(con.paciente_id)

                print("Plano de saúde: " + str(paciente.plano_saude))

                preco = float(input("Preço da consulta: "))

                formato_data = "%d/%m/%Y"
                data = datetime.strptime(input("Data: "), formato_data)

                ConsultaDAO().update(con.id, preco, data, False, False)
                print(GREEN + "Consulta marcada." + RESET)

                self.menu(sistema)

            except Exception as err:
                print(err)
                print("Opção inválida.")
                self.menu(sistema)

    @staticmethod
    def cadastrar(sistema):
        from database.SecretarioDAO import SecretarioDAO

        print()
        print(BLUE + "CADASTRO SECRETÁRIO" + RESET)
        nome = input("Nome: ")
        cpf = input("CPF: ")
        pessoa = PessoaDAO().getPessoaByCPF(cpf)
        if pessoa != None:
            print(RED + "CPF já cadastrado." + RESET)
            sistema.menuPrincipal()
            return

        senha = input("Senha: ")
        salario = float(input("Salário: "))
        secretario = Secretario(nome, cpf, senha, salario)
        SecretarioDAO().insert(secretario)
        print()