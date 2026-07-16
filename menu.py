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
            print("\n>>> Menu de Clientes em construção...")
            input("\nPressione ENTER para continuar...")

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
            