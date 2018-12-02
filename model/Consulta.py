from util.Color import *


class Consulta():

    def __init__(self, preco, data, paciente_id, medico_id, realizada, paga, id=None):
        self.id=id
        self.preco=preco
        self.data=data
        self.paciente_id=paciente_id
        self.medico_id=medico_id
        self.realizada=realizada
        self.paga=paga

    def infoConsulta(self, sistema):
        from database.MedicoDAO import MedicoDAO
        from database.PacienteDAO import PacienteDAO

        print(CYAN + "CONSULTA" + RESET)
        print("Médico: " + MedicoDAO().getByID(self.medico_id).nome)
        print("Paciente: " + PacienteDAO().getByID(self.paciente_id).nome)