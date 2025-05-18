class Tutor():
  def __init__(self, nome_tutor, telefone_tutor):
    self.nome_tutor = nome_tutor
    self.telefone_tutor = telefone_tutor

  def inserir_nome(self):
    print(f"Olá, {self.nome_tutor}! Seu nome foi inserido com sucesso no nosso sistema.")

  def inserir_telefone(self):
    print(f"Seu {self.telefone_tutor} foi inserido com sucesso.")

tutor1 = Tutor("José", "(12) 9-3456-8978")
tutor1.inserir_nome()
tutor1.inserir_telefone()