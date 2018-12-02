from database.DAO import DAO
from model.Consulta import Consulta


class ConsultaDAO(DAO):

    def __init__(self):
        super().__init__()

    def insert(self, consulta: Consulta):
        # Script de Inserção.
        query = "INSERT INTO consulta(preco, data, paciente_id, medico_id, realizada, paga) " \
                "VALUES(?, ?, ?, ?, ?, ?)"
        # Valores.
        values = (consulta.preco, consulta.data, consulta.paciente_id, consulta.medico_id, consulta.realizada, consulta.paga)

        try:
            return super().insert(query, values)
        except Exception as err:
            print("Erro no banco de dados!")
            print(err)
            return

    def delete(self, id):
        query = "DELETE FROM consulta WHERE id = ?"
        values = (id,)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def update(self, id, preco, data, realizada, paga):
        query = "UPDATE consulta " \
                "SET preco = ?, data = ?, realizada = ?, paga = ? " \
                "WHERE id = ?"
        values = (preco, data, realizada, paga, id)

        try:
            self.execute(query, values)
            return True
        except Exception as err:
            print(err)
            return False

    def getAllPendente(self):
        query = "SELECT * FROM consulta " \
                "WHERE preco is null and data is null"

        try:
            rows = self.get_rows(query)

            consultas = [Consulta(row[1], row[2], row[3], row[4], row[5], row[6], row[0]) for row in rows]

            return consultas
        except Exception as err:
            print(err)
            return []

    def getAllByPaciente(self, paciente_id):
        query = "SELECT * FROM consulta " \
                "WHERE paciente_id = ?"
        values = (paciente_id,)

        try:
            rows = self.get_rows(query, values)

            consultas = [Consulta(row[1], row[2], row[3], row[4], row[5], row[6], row[0]) for row in rows]

            return consultas
        except Exception as err:
            print(err)
            return []