from database.DAO import DAO
from database.PessoaDAO import PessoaDAO
from model.Secretario import Secretario

class SecretarioDAO(DAO):

    def __init__(self):
        super().__init__()

    def insert(self, secretario: Secretario):
        pessoa_id = PessoaDAO().insert(secretario)
        # Script de Inserção.
        query = "INSERT INTO secretario(pessoa_id, salario) " \
                "VALUES(?, ?)"
        # Valores.
        values = (pessoa_id, secretario.salario)

        try:
            return super().insert(query, values)
        except Exception as err:
            print("Erro no banco de dados!")
            print(err)
            return

    def delete(self, id):
        query = "DELETE FROM secretario WHERE id = ?"
        values = (id,)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def update(self, id, nome, cpf, senha, salario):
        query = "UPDATE secretario " \
                "SET nome = ?, cpf = ?, senha = ?, salario = ? " \
                "WHERE id = ?"
        values = (nome, cpf, senha, salario, id)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def login(self, cpf, senha):

        query = "SELECT secretario.id, nome, cpf, senha, salario, pessoa.id FROM pessoa, secretario " \
                "WHERE cpf = ? and senha = ? and pessoa.id = pessoa_id"
        values = (cpf, senha)

        try:
            row = self.get_row(query, values)
            if(row == None):
                return None
            return Secretario(row[1], row[2], row[3], row[4], id=row[0], pessoa_id=[5])
        except Exception as err:
            print(err)
            return None