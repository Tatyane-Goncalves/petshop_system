from tutor import Tutor
from cachorro import Cachorro
from gato import Gato
from servico import Servico
from agendamento import Agendamento

tutores = []
servicos = []
agendamentos = []

def exibir_menu():
  print("\n---PETSHOP SYSTEM ---")
  print("1. Cadastrar tutor")
  print("2. Cadastrar pet")
  print("3. Cadastrar serviço")
  print("4. Agendar serviço")
  print("5. Ver agendamentos")
  print("6. Sair")

def main():
  while True: 
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      cadastrar_tutor()
    elif opcao == "2":
      cadastrar_pet()
    elif opcao == "3":
      cadastrar_servico()
    elif opcao == "4":
      agendar_servico()
    elif opcao == "5":
      ver_agendamento()
    elif opcao == "6":
      print("Saindo... até a próxima!")
    else:
      print("Opção inválida! Tente de novo.")
  
if __name__ == "__main__":
  main()

def cadastrar_tutor():
    nome = input("Nome do tutor: ")
    telefone = input("Telefone: ")
    tutor = Tutor(nome, telefone)
    tutores.append(tutor)
    print(f"Tutor {nome} cadastrado com sucesso!")

def cadastrar_pet():
  if not tutores:
    print("Cadastre um tutor antes de adicionar pets.")
  
  print("\nTutores disponíveis:")
  for i, tutor in  enumerate(tutores):
    print(f"{i} - {tutor.nome}")
  
  indice = int(input("Escolha o tutor pelo número: "))
  tutor = tutores[indice]

  nome_pet = input("Nome do pet: ")
  idade_pet = input("Idade do pet: ")
  tipo = input("Tipo do pet (cachorro/gato): ").lower

  if tipo == "cachorro":
    raca = input("Raça: ")
    pet = Cachorro(nome_pet, idade_pet, raca)
  
  elif tipo == "gato":
    cor = input("Cor do gato: ")
    pet = Gato(nome_pet, idade_pet, cor)
  
  else:
    print("Sinto muito, não atendemos esse tipo de animal.")
    return

  tutor.adicionar_pet(pet)
  print(f"{tipo.capitalize()} {nome_pet} cadastrado com sucesso para {tutor.nome}!")


def menu_servico():
  print("\n--- Menu serviços do PetShop ---")
  print("1. Banho")
  print("2. Tosa")
  print("3. Vacinação")
  print("4. Sair")

def cadastrar_servico():
  while True:
    menu_servico()
    servico_opcao = input("Escolha uma opção de serviço: ")

    if servico_opcao == "1":
      print(f"Cadastrando {}")