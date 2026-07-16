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
            print("\n>>> Cadastro de clientes em construção...")
            input("\nPressione ENTER para continuar...")

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
            print("\n>>> Menu de Pets em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            print("\n>>> Menu de Serviços em construção...")
            input("\nPressione ENTER para continuar...")

        elif opcao == "0":
            print("\nSistema encerrado. Até logo!")
            break

        else:
            print("\nOpção inválida!")
            input("\nPressione ENTER para continuar...")
