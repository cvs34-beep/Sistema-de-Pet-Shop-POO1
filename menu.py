from pet import Pet
from arquivo import salvar_pet
from cliente import Cliente
from arquivo import salvar_cliente

def menu_clientes():
    while True:
        print("\n" + "=" * 40)
        print("         MENU CLIENTES")
        print("=" * 40)
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            print("\n>>> Listagem de clientes em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            print("\n>>> Atualização de clientes em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "4":
            print("\n>>> Exclusão de clientes em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida!")
            input("\nPressione ENTER para continuar...")

def cadastrar_cliente():

    print("\n===== CADASTRO DE CLIENTE =====")

    id_cliente = input("ID: ")
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    cliente = Cliente(
        id_cliente,
        nome,
        telefone
    )

    salvar_cliente(cliente)

    print("\nCliente cadastrado com sucesso!")

    input("\nPressione ENTER para continuar...")


def menu_principal():
    while True:
        print("\n" + "=" * 40)
        print("       SISTEMA PET SHOP")
        print("=" * 40)
        print("1 - Clientes")
        print("2 - Pets")
        print("3 - Serviços")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_clientes()

        elif opcao == "2":
            menu_pets()

        elif opcao == "3":
            menu_servicos()

        elif opcao == "0":
            print("\nSistema encerrado. Até logo!")
            break

        else:
            print("\nOpção inválida!")
            input("\nPressione ENTER para continuar...")

def menu_pets():
    while True:
        print("\n" + "=" * 40)
        print("           MENU PETS")
        print("=" * 40)
        print("1 - Cadastrar Pet")
        print("2 - Listar Pets")
        print("3 - Atualizar Pet")
        print("4 - Excluir Pet")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_pet()

        elif opcao == "2":
            print("\n>>> Listagem de pets em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            print("\n>>> Atualização de pets em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "4":
            print("\n>>> Exclusão de pets em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida!")
            input("\nPressione ENTER para continuar...")
def cadastrar_pet():

    print("\n===== CADASTRO DE PET =====")

    id_pet = input("ID: ")
    nome = input("Nome: ")
    especie = input("Espécie: ")
    raca = input("Raça: ")
    idade = input("Idade: ")
    tutor = input("Tutor: ")

    pet = Pet(
        id_pet,
        nome,
        especie,
        raca,
        idade,
        tutor
    )

    salvar_pet(pet)

    print("\nPet cadastrado com sucesso!")

    input("\nPressione ENTER para continuar...")

def menu_servicos():
    while True:
        print("\n" + "=" * 40)
        print("        MENU SERVIÇOS")
        print("=" * 40)
        print("1 - Cadastrar Serviço")
        print("2 - Listar Serviços")
        print("3 - Atualizar Serviço")
        print("4 - Excluir Serviço")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\n>>> Cadastro de serviços em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "2":
            print("\n>>> Listagem de serviços em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            print("\n>>> Atualização de serviços em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "4":
            print("\n>>> Exclusão de serviços em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida!")
            input("\nPressione ENTER para continuar...")           