class Receita():
    def __init__(self, indicacoes, medicamentos, paciente_id, medico_id, id=None):
        self.indicacoes=indicacoes
        self.medicamentos=medicamentos
        self.paciente_id=paciente_id
        self.medico_id=medico_id
        self.id=id