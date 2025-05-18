class Agendamento:
    def __init__(self, pet, servico, data):
        self.pet = pet
        self.servico = servico
        self.data = data

    def exibir_detalhes(self):
        print(f"{self.pet.nome} vai fazer {self.servico.tipo} em {self.data}")
