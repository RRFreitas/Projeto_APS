from database.DAO import DAO
from database.PessoaDAO import PessoaDAO
from model.Medico import Medico
from util.Color import *


class MedicoDAO(DAO):

    def __init__(self):
        super().__init__()

    def insert(self, medico: Medico):
        pessoa_id = PessoaDAO().insert(medico)

        # Script de Inserção.
        query = "INSERT INTO medico(pessoa_id, especializacao, salario) " \
                "VALUES(?, ?, ?)"
        # Valores.
        values = (pessoa_id, medico.especializacao, medico.salario)

        try:
            print(GREEN + "Médico cadastrado com sucesso." + RESET)
            return super().insert(query, values)
        except Exception as err:
            print("Erro no banco de dados!")
            print(err)
            return

    def getAll(self):
        query = "SELECT * FROM medico"

        try:
            rows = self.get_rows(query)

            medicos = []

            for row in rows:
                pessoa = PessoaDAO().getPessoaByID(row[1])

                medicos.append(Medico(pessoa.nome, pessoa.cpf, pessoa.senha, row[2], row[3], row[1], row[0]))
            return medicos
        except Exception as err:
            print(err)
            return []

    def getByID(self, id):
        query = "SELECT * FROM medico " \
                "WHERE id = ?"
        values = (id,)

        try:
            row = self.get_row(query, values)
            pessoa = PessoaDAO().getPessoaByID(row[1])
            if (row == None):
                return None
            return Medico(pessoa.nome, pessoa.cpf, pessoa.senha, row[2], row[3], row[1], row[0])
        except Exception as err:
            print(err)
            return None

    def delete(self, id):
        query = "DELETE FROM medico WHERE id = ?"
        values = (id,)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def update(self, id, nome, cpf, senha, especializacao, salario):
        query = "UPDATE medico " \
                "SET nome = ?, cpf = ?, senha = ?, especializacao = ?, salario = ? " \
                "WHERE id = ?"
        values = (nome, cpf, senha, especializacao, salario, id)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False