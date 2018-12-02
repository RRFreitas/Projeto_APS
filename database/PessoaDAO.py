from database.DAO import DAO
from model.Pessoa import Pessoa


class PessoaDAO(DAO):

    def __init__(self):
        super().__init__()

    def insert(self, pessoa: Pessoa):
        # Script de Inserção.
        query = "INSERT INTO pessoa(nome, cpf, senha) " \
                "VALUES(?, ?, ?)"
        # Valores.
        values = (pessoa.nome, pessoa.cpf, pessoa.senha)

        try:
            return super().insert(query, values)
        except Exception as err:
            print("Erro no banco de dados!")
            print(err)
            return

    def delete(self, id):
        query = "DELETE FROM pessoa WHERE id = ?"
        values = (id,)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def update(self, id, nome, cpf, senha):
        query = "UPDATE pessoa " \
                "SET nome = ?, cpf = ?, senha = ? " \
                "WHERE id = ?"
        values = (nome, cpf, senha, id)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def getPessoaByCPF(self, cpf):
        query = "SELECT * FROM pessoa " \
                "WHERE cpf = ?"
        values = (cpf,)

        try:
            row = self.get_row(query, values)
            if(row == None):
                return None
            return Pessoa(row[1], row[2], row[3])
        except Exception as err:
            print(err)
            return None

    def getPessoaByID(self, id):
        query = "SELECT * FROM pessoa " \
                "WHERE id = ?"
        values = (id,)

        try:
            row = self.get_row(query, values)
            if(row == None):
                return None
            return Pessoa(row[1], row[2], row[3])
        except Exception as err:
            print(err)
            return None