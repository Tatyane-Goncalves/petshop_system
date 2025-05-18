class Tutor:
  def __init__(self, nome, telefone):
    self.nome = nome
    self.telefone = telefone
    self.pets = []

  def adicionar_pet(self, pet):
    self.pets.append(pet)