from cliente import Cliente
from pet import Pet
from servico import Servico

from arquivo import (
    criar_arquivos,

    salvar_cliente,
    listar_clientes,
    atualizar_cliente,
    excluir_cliente,

    salvar_pet,
    listar_pets,
    atualizar_pet,
    excluir_pet,

    salvar_servico,
    listar_servicos,
    atualizar_servico,
    excluir_servico
)
def menu_principal():

    criar_arquivos()

    while True:

        print("\n" + "=" * 40)
        print("      SISTEMA PET SHOP")
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
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida!")
            input("\nPressione ENTER para continuar...")
if __name__ == "__main__":
    menu_principal()
def menu_clientes():

    while True:

        print("\n" + "=" * 40)
        print("          MENU CLIENTES")
        print("=" * 40)
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")


        # CADASTRAR CLIENTE
        if opcao == "1":

            print("\n--- Cadastro de Cliente ---")

            id_cliente = input("ID do cliente: ")
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")

            cliente = Cliente(
                id_cliente,
                nome,
                telefone,
                email
            )

            salvar_cliente(cliente)

            print("\nCliente cadastrado com sucesso!")


        # LISTAR CLIENTES
        elif opcao == "2":

            print("\n--- Lista de Clientes ---")

            clientes = listar_clientes()

            if len(clientes) == 0:
                print("Nenhum cliente cadastrado.")

            else:

                for cliente in clientes:
                    print("\n---------------------")
                    print(f"ID: {cliente.id_cliente}")
                    print(f"Nome: {cliente.nome}")
                    print(f"Telefone: {cliente.telefone}")
                    print(f"Email: {cliente.email}")


        # ATUALIZAR CLIENTE
        elif opcao == "3":

            print("\n--- Atualizar Cliente ---")

            id_cliente = input("Digite o ID do cliente: ")

            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Novo email: ")


            cliente = Cliente(
                id_cliente,
                nome,
                telefone,
                email
            )


            atualizar_cliente(cliente)

            print("\nCliente atualizado com sucesso!")


        # EXCLUIR CLIENTE
        elif opcao == "4":

            print("\n--- Excluir Cliente ---")

            id_cliente = input("Digite o ID do cliente: ")

            excluir_cliente(id_cliente)

            print("\nCliente excluído com sucesso!")


        # VOLTAR
        elif opcao == "0":

            break


        else:

            print("\nOpção inválida!")

        input("\nPressione ENTER para continuar...")
def menu_pets():

    while True:

        print("\n" + "=" * 40)
        print("            MENU PETS")
        print("=" * 40)
        print("1 - Cadastrar pet")
        print("2 - Listar pets")
        print("3 - Atualizar pet")
        print("4 - Excluir pet")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")


        # CADASTRAR PET
        if opcao == "1":

            print("\n--- Cadastro de Pet ---")

            id_pet = input("ID do pet: ")
            nome = input("Nome do pet: ")
            especie = input("Espécie: ")
            raca = input("Raça: ")
            idade = input("Idade: ")
            tutor = input("Nome do tutor: ")


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


        # LISTAR PETS
        elif opcao == "2":

            print("\n--- Lista de Pets ---")

            pets = listar_pets()


            if len(pets) == 0:

                print("Nenhum pet cadastrado.")


            else:

                for pet in pets:

                    print("\n---------------------")
                    print(f"ID: {pet.id_pet}")
                    print(f"Nome: {pet.nome}")
                    print(f"Espécie: {pet.especie}")
                    print(f"Raça: {pet.raca}")
                    print(f"Idade: {pet.idade}")
                    print(f"Tutor: {pet.tutor}")



        # ATUALIZAR PET
        elif opcao == "3":

            print("\n--- Atualizar Pet ---")


            id_pet = input("Digite o ID do pet: ")

            nome = input("Novo nome: ")
            especie = input("Nova espécie: ")
            raca = input("Nova raça: ")
            idade = input("Nova idade: ")
            tutor = input("Novo tutor: ")


            pet = Pet(
                id_pet,
                nome,
                especie,
                raca,
                idade,
                tutor
            )


            atualizar_pet(pet)


            print("\nPet atualizado com sucesso!")



        # EXCLUIR PET
        elif opcao == "4":

            print("\n--- Excluir Pet ---")


            id_pet = input("Digite o ID do pet: ")


            excluir_pet(id_pet)


            print("\nPet excluído com sucesso!")



        # VOLTAR
        elif opcao == "0":

            break



        else:

            print("\nOpção inválida!")


        input("\nPressione ENTER para continuar...")
def menu_servicos():

    while True:

        print("\n" + "=" * 40)
        print("          MENU SERVIÇOS")
        print("=" * 40)
        print("1 - Cadastrar serviço")
        print("2 - Listar serviços")
        print("3 - Atualizar serviço")
        print("4 - Excluir serviço")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")



        # CADASTRAR SERVIÇO
        if opcao == "1":

            print("\n--- Cadastro de Serviço ---")


            id_servico = input("ID do serviço: ")
            nome = input("Nome do serviço: ")
            descricao = input("Descrição: ")
            valor = input("Valor: ")


            servico = Servico(
                id_servico,
                nome,
                descricao,
                valor
            )


            salvar_servico(servico)


            print("\nServiço cadastrado com sucesso!")




        # LISTAR SERVIÇOS
        elif opcao == "2":

            print("\n--- Lista de Serviços ---")


            servicos = listar_servicos()


            if len(servicos) == 0:

                print("Nenhum serviço cadastrado.")


            else:

                for servico in servicos:

                    print("\n---------------------")
                    print(f"ID: {servico.id_servico}")
                    print(f"Nome: {servico.nome}")
                    print(f"Descrição: {servico.descricao}")
                    print(f"Valor: R$ {servico.valor}")






        # ATUALIZAR SERVIÇO
        elif opcao == "3":

            print("\n--- Atualizar Serviço ---")


            id_servico = input("Digite o ID do serviço: ")

            nome = input("Novo nome: ")
            descricao = input("Nova descrição: ")
            valor = input("Novo valor: ")



            servico = Servico(
                id_servico,
                nome,
                descricao,
                valor
            )


            atualizar_servico(servico)


            print("\nServiço atualizado com sucesso!")







        # EXCLUIR SERVIÇO
        elif opcao == "4":

            print("\n--- Excluir Serviço ---")


            id_servico = input("Digite o ID do serviço: ")


            excluir_servico(id_servico)


            print("\nServiço excluído com sucesso!")







        # VOLTAR
        elif opcao == "0":

            break



        else:

            print("\nOpção inválida!")



        input("\nPressione ENTER para continuar...")
