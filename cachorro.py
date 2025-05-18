class Cachorro(Animal):
  def __init__(self, nome, idade, raca):
    self.nome = nome
    self.idade = idade
    self.raca = raca
  
  def fazer_som(self):
    return "Au au!"