import csv
import os

PASTA_DADOS = "dados"


# ==========================
# CRIAÇÃO DOS ARQUIVOS
# ==========================

def criar_arquivos():

    if not os.path.exists(PASTA_DADOS):
        os.mkdir(PASTA_DADOS)

    arquivos = [
        "clientes.csv",
        "pets.csv",
        "servicos.csv"
    ]

    for arquivo in arquivos:
        caminho = os.path.join(PASTA_DADOS, arquivo)

        if not os.path.exists(caminho):
            with open(caminho, "w", newline="", encoding="utf-8"):
                pass


# ==========================
# CLIENTES
# ==========================

def salvar_cliente(cliente):
    caminho = os.path.join(PASTA_DADOS, "clientes.csv")

    with open(caminho, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(cliente.para_lista())


# ==========================
# PETS
# ==========================

def salvar_pet(pet):
    caminho = os.path.join(PASTA_DADOS, "pets.csv")

    with open(caminho, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(pet.para_lista())


# ==========================
# SERVIÇOS
# ==========================

def salvar_servico(servico):
    caminho = os.path.join(PASTA_DADOS, "servicos.csv")

    with open(caminho, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(servico.para_lista())
# ==========================
# LISTAR CLIENTES
# ==========================

def listar_clientes():
    caminho = os.path.join(PASTA_DADOS, "clientes.csv")

    try:
        with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            print("\n===== CLIENTES CADASTRADOS =====")

            encontrou = False

            for linha in leitor:
                encontrou = True

                print(f"ID: {linha[0]}")
                print(f"Nome: {linha[1]}")
                print(f"Telefone: {linha[2]}")
                print("-" * 30)

            if not encontrou:
                print("Nenhum cliente cadastrado.")

    except FileNotFoundError:
        print("Arquivo de clientes não encontrado.")

    input("\nPressione ENTER para continuar...")


# ==========================
# LISTAR PETS
# ==========================

def listar_pets():
    caminho = os.path.join(PASTA_DADOS, "pets.csv")

    try:
        with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            print("\n===== PETS CADASTRADOS =====")

            encontrou = False

            for linha in leitor:
                encontrou = True

                print(f"ID: {linha[0]}")
                print(f"Nome: {linha[1]}")
                print(f"Espécie: {linha[2]}")
                print(f"Raça: {linha[3]}")
                print(f"Idade: {linha[4]}")
                print(f"Tutor: {linha[5]}")
                print("-" * 30)

            if not encontrou:
                print("Nenhum pet cadastrado.")

    except FileNotFoundError:
        print("Arquivo de pets não encontrado.")

    input("\nPressione ENTER para continuar...")


# ==========================
# LISTAR SERVIÇOS
# ==========================

def listar_servicos():
    caminho = os.path.join(PASTA_DADOS, "servicos.csv")

    try:
        with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)

            print("\n===== SERVIÇOS CADASTRADOS =====")

            encontrou = False

            for linha in leitor:
                encontrou = True

                print(f"ID: {linha[0]}")
                print(f"Serviço: {linha[1]}")
                print(f"Valor: R$ {linha[2]}")
                print("-" * 30)

            if not encontrou:
                print("Nenhum serviço cadastrado.")

    except FileNotFoundError:
        print("Arquivo de serviços não encontrado.")

    input("\nPressione ENTER para continuar...")
# ==========================
# ATUALIZAR CLIENTE
# ==========================

def atualizar_cliente(id_cliente, novo_nome, novo_telefone):
    caminho = os.path.join(PASTA_DADOS, "clientes.csv")

    clientes = []

    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == id_cliente:
                linha = [id_cliente, novo_nome, novo_telefone]

            clientes.append(linha)

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(clientes)


# ==========================
# ATUALIZAR PET
# ==========================

def atualizar_pet(id_pet, nome, especie, raca, idade, tutor):
    caminho = os.path.join(PASTA_DADOS, "pets.csv")

    pets = []

    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == id_pet:
                linha = [
                    id_pet,
                    nome,
                    especie,
                    raca,
                    idade,
                    tutor
                ]

            pets.append(linha)

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(pets)


# ==========================
# ATUALIZAR SERVIÇO
# ==========================

def atualizar_servico(id_servico, nome, valor):
    caminho = os.path.join(PASTA_DADOS, "servicos.csv")

    servicos = []

    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] == id_servico:
                linha = [
                    id_servico,
                    nome,
                    valor
                ]

            servicos.append(linha)

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(servicos)
# ==========================
# EXCLUIR CLIENTE
# ==========================

def excluir_cliente(id_cliente):
    caminho = os.path.join(PASTA_DADOS, "clientes.csv")

    clientes = []

    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] != id_cliente:
                clientes.append(linha)

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(clientes)


# ==========================
# EXCLUIR PET
# ==========================

def excluir_pet(id_pet):
    caminho = os.path.join(PASTA_DADOS, "pets.csv")

    pets = []

    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] != id_pet:
                pets.append(linha)

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(pets)


# ==========================
# EXCLUIR SERVIÇO
# ==========================

def excluir_servico(id_servico):
    caminho = os.path.join(PASTA_DADOS, "servicos.csv")

    servicos = []

    with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            if linha[0] != id_servico:
                servicos.append(linha)

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(servicos)
        