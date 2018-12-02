from model.Pessoa import Pessoa
from model.Consulta import Consulta
from database.ConsultaDAO import ConsultaDAO
from database.MedicoDAO import MedicoDAO
from util.Color import *


class Paciente(Pessoa):

    def __init__(self, nome, cpf, senha, plano_saude, pessoa_id=None, id=None):
        super().__init__(nome, cpf, senha, pessoa_id)
        self.plano_saude=plano_saude
        self.id=id

    def menu(self, sistema):
        print("Bem vindo, " + CYAN + self.nome + RESET)
        print()
        print("1) Ver consultas")
        print("2) Marcar consulta")
        print("3) Sair")

        try:
            op = int(input("=> "))

            if op == 1:
                self.verConsultas(sistema)
            elif op == 2:
                self.marcarConsulta(sistema)
            elif op == 3:
                sistema.menuPrincipal()
            else:
                raise ValueError()

        except ValueError:
            print("Opção inválida.")
            self.menu(sistema)

    def verConsultas(self, sistema):
        consultas = ConsultaDAO().getAllByPaciente(self.id)

        if(len(consultas) == 0):
            print(YELLOW + "Não há consultas." + RESET)
            self.menu(sistema)
        else:
            print(BLUE + "Consultas: " + RESET)
            for i, con in enumerate(consultas):
                med = MedicoDAO().getByID(con.medico_id)
                if(con.realizada):
                    print(str(i) + ") Consulta com " + med.nome + " | " + GREEN + "REALIZADA" + RESET)
                else:
                    print(str(i) + ") Consulta com " + med.nome)

            op = int(input("=> "))

            try:
                con = consultas[op]
                con.infoConsulta(sistema)
                if con.preco == None and con.data == None:
                    print(YELLOW + "Esperando ser aprovada." + RESET)
                    sistema.usuarioLogado.menu(sistema)
                else:
                    self.menu(sistema)
            except Exception as err:
                print(err)
                print("Opção inválida.")
                self.menu(sistema)

    def marcarConsulta(self, sistema):
        print()
        print(CYAN + "Marcar consulta")
        print()

        medicos = MedicoDAO().getAll()

        if(len(medicos) == 0):
            print(YELLOW + "Não há médicos cadastrados." + RESET)
            self.menu(sistema)
        else:
            print(BLUE + "Médicos: " + RESET)
            for i, med in enumerate(medicos):
                print(str(i) + ") " + med.nome)

            op = int(input("=> "))

            try:
                med = medicos[op]

                ConsultaDAO().insert(Consulta(None, None, self.id, med.id, False, False))
                print(GREEN + "Consulta em espera para ser aprovada.")
                self.menu(sistema)
            except Exception as err:
                print(err)
                print("Opção inválida.")
                self.menu(sistema)