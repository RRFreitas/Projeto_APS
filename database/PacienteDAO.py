from database.DAO import DAO
from database.PessoaDAO import PessoaDAO
from model.Paciente import Paciente
from util.Color import *


class PacienteDAO(DAO):

    def __init__(self):
        super().__init__()

    def insert(self, paciente: Paciente):
        pessoa_id = PessoaDAO().insert(paciente)

        # Script de Inserção.
        query = "INSERT INTO paciente(pessoa_id, plano_saude) " \
                "VALUES(?, ?)"
        # Valores.
        values = (pessoa_id, paciente.plano_saude)

        try:
            print(GREEN + "Paciente cadastrado com sucesso." + RESET)
            return super().insert(query, values)
        except Exception as err:
            print(RED + "Erro no banco de dados!")
            print(str(err) + RESET)
            return

    def delete(self, id):
        query = "DELETE FROM paciente WHERE id = ?"
        values = (id,)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def update(self, id, pessoa_id, nome, cpf, senha, plano_saude):
        PessoaDAO().update(pessoa_id, nome, cpf, senha)
        query = "UPDATE paciente " \
                "SET plano_saude = ? " \
                "WHERE id = ?"
        values = (plano_saude, id)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def getByID(self, id):
        query = "SELECT * FROM paciente " \
                "WHERE id = ?"
        values = (id,)

        try:
            row = self.get_row(query, values)
            pessoa = PessoaDAO().getPessoaByID(row[1])
            if (row == None):
                return None
            return Paciente(pessoa.nome, pessoa.cpf, pessoa.senha, row[2], row[1], row[0])
        except Exception as err:
            print(err)
            return None

    def login(self, cpf, senha):

        query = "SELECT paciente.id, nome, cpf, senha, plano_saude, pessoa.id FROM pessoa, paciente " \
                "WHERE cpf = ? and senha = ? and pessoa.id = pessoa_id"
        values = (cpf, senha)

        try:
            row = self.get_row(query, values)
            if(row == None):
                return None
            return Paciente(row[1], row[2], row[3], row[4], id=row[0], pessoa_id=row[5])
        except Exception as err:
            print(err)
            return None