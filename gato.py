class Gato(Animal):
  def __init__(self, nome, idade, cor):
    self.nome = nome
    self.idade = idade
    self.cor = cor

  def fazer_som(self):
    return "Miau!"