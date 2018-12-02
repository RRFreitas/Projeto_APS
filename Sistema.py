from CreateDB import criarBanco
from util.Color import *
from database.PacienteDAO import PacienteDAO
from database.PessoaDAO import PessoaDAO
from database.SecretarioDAO import SecretarioDAO
from model.Paciente import Paciente
from model.Medico import Medico
from model.Secretario import Secretario
from model.Pessoa import Pessoa


class Sistema:

    usuarioLogado = None

    def __init__(self):
        criarBanco()

    def menuPrincipal(self):
        print()
        print()
        print(BLUE + BOLD + "Clínica Médica" + RESET)
        print("1) Login paciente")
        print("2) Cadastrar paciente")
        print(YELLOW + "3) Acessar sistema" + RESET)

        try:
            op = int(input("=> "))

            if op == 1:
                print()
                cpf = input("CPF: ")
                senha = input("Senha: ")

                paciente = PacienteDAO().login(cpf, senha)

                if paciente == None:
                    print(RED + "Login incorreto." + RESET)
                    print()
                    self.menuPrincipal()
                else:
                    self.usuarioLogado = paciente
                    print(GREEN + "Logado com sucesso." + RESET)
                    print()
                    paciente.menu(self)

            elif op == 2:
                print()
                print(CYAN + "CADASTRO" + RESET)
                nome = input("Nome: ")
                cpf = input("CPF: ")

                pessoa = PessoaDAO().getPessoaByCPF(cpf)

                if(pessoa != None):
                    print(RED + "CPF já cadastrado." + RESET)
                    self.menuPrincipal()

                senha = input("Senha de acesso: ")
                print("Possui plano de saúde? (s/n)")
                res = input()
                if(res.startswith('s')):
                    plano = True
                else:
                    plano = False
                paciente = Paciente(nome, cpf, senha, plano)
                PacienteDAO().insert(paciente)
                self.menuPrincipal()
            elif op == 3:
                print()
                print("1) Login Admin")
                print("2) Login Médico")
                print("3) Login Secretário")
                print("4) Sair")

                lg = int(input("=> "))

                if lg == 1:
                    print()
                    user = input("Usuário: ")
                    senha = input("Senha: ")

                    if user == "admin" and senha == "admin":
                        self.menuSistema()
                    else:
                        print(RED + "Login incorreto. " + RESET)
                        self.menuPrincipal()
                elif lg == 2:
                    pass
                elif lg == 3:
                    print()
                    cpf = input("CPF: ")
                    senha = input("Senha: ")

                    secretario = SecretarioDAO().login(cpf, senha)

                    if secretario == None:
                        print(RED + "Login incorreto." + RESET)
                        print()
                        self.menuPrincipal()
                    else:
                        self.usuarioLogado = secretario
                        print(GREEN + "Logado com sucesso." + RESET)
                        print()
                        secretario.menu(self)
                elif lg == 4:
                    self.menuPrincipal()
                else:
                    raise ValueError()
            else:
                raise ValueError()

        except ValueError as err:
            print("Opção inválida.")
            self.menuPrincipal()
        except Exception as err:
            print(RED + err.args[0] + RESET)

    def menuSistema(self):
        print()
        print(CYAN + "Menu do sistema" + RESET)
        print("1) Cadastrar Médico")
        print("2) Cadastrar Secretário")
        print("3) Sair")

        try:
            op = int(input("=> "))

            if op == 1:
                Medico.cadastrar(self)
                self.menuSistema()
            elif op == 2:
                Secretario.cadastrar(self)
                self.menuSistema()
            elif op == 3:
                self.menuPrincipal()
            else:
                raise ValueError()
        except ValueError as err:
            print("Opção inválida.")
            self.menuSistema()