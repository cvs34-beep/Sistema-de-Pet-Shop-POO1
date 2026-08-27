import csv
import os

from cliente import Cliente
from pet import Pet
from servico import Servico



# ==============================
# PASTA DOS ARQUIVOS
# ==============================

PASTA_DADOS = "dados"


# ==============================
# CRIAR ARQUIVOS
# ==============================

def criar_arquivos():

    if not os.path.exists(PASTA_DADOS):
        os.mkdir(PASTA_DADOS)

    arquivos = [
        "clientes.csv",
        "pets.csv",
        "servicos.csv"
    ]


    for arquivo in arquivos:

        caminho = os.path.join(
            PASTA_DADOS,
            arquivo
        )



        if not os.path.exists(caminho):

            with open(
                caminho,
                "w",
                newline="",
                encoding="utf-8"
            ):
                pass


# ==============================
# CLIENTES
# ==============================


def salvar_cliente(cliente):

    caminho = os.path.join(
        PASTA_DADOS,
        "clientes.csv"
    )

    with open(
        caminho,
        "a",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(
            cliente.para_lista()
        )


def listar_clientes():

    caminho = os.path.join(
        PASTA_DADOS,
        "clientes.csv"
    )

    clientes = []

    try:

        with open(
            caminho,
            "r",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            leitor = csv.reader(arquivo)

            for linha in leitor:

                cliente = Cliente.de_lista(linha)

                clientes.append(cliente)

    except FileNotFoundError:

        pass

    return clientes



def atualizar_cliente(cliente):

    caminho = os.path.join(
        PASTA_DADOS,
        "clientes.csv"
    )

    clientes = []

    with open(
        caminho,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:

            if linha[0] == cliente.id_cliente:

                linha = cliente.para_lista()

            clientes.append(linha)

    with open(
        caminho,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerows(clientes)



def excluir_cliente(id_cliente):

    caminho = os.path.join(
        PASTA_DADOS,
        "clientes.csv"
    )

    clientes = []

    with open(
        caminho,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:

            if linha[0] != id_cliente:

                clientes.append(linha)

    with open(
        caminho,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerows(clientes)
# ==================================
# PETS
# ==================================


def salvar_pet(pet):

    caminho = os.path.join(
        PASTA_DADOS,
        "pets.csv"
    )

    with open(
        caminho,
        "a",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(
            pet.para_lista()
        )

        escritor.writerow(
            pet.para_lista()
        )


def listar_pets():

    caminho = os.path.join(
        PASTA_DADOS,
        "pets.csv"
    )

    pets = []

    try:

        with open(
            caminho,
            "r",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            leitor = csv.reader(arquivo)

            for linha in leitor:

                pet = Pet.de_lista(linha)

                pets.append(pet)

    except FileNotFoundError:

        pass

    return pets



def atualizar_pet(pet):

    caminho = os.path.join(
        PASTA_DADOS,
        "pets.csv"
    )

    pets = []

    with open(
        caminho,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:

            if linha[0] == pet.id_pet:

                linha = pet.para_lista()

            pets.append(linha)

    with open(
        caminho,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerows(pets)



def excluir_pet(id_pet):

    caminho = os.path.join(
        PASTA_DADOS,
        "pets.csv"
    )

    pets = []

    with open(
        caminho,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:

            if linha[0] != id_pet:

                pets.append(linha)

    with open(
        caminho,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerows(pets)
# ==================================
# SERVIÇOS
# ==================================


def salvar_servico(servico):

    caminho = os.path.join(
        PASTA_DADOS,
        "servicos.csv"
    )

    with open(
        caminho,
        "a",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow(
            servico.para_lista()
        )



def listar_servicos():

    caminho = os.path.join(
        PASTA_DADOS,
        "servicos.csv"
    )

    servicos = []

    try:

        with open(
            caminho,
            "r",
            newline="",
            encoding="utf-8"
        ) as arquivo:

            leitor = csv.reader(arquivo)

            for linha in leitor:

                servico = Servico.de_lista(linha)

                servicos.append(servico)

    except FileNotFoundError:

        pass

    return servicos



def atualizar_servico(servico):

    caminho = os.path.join(
        PASTA_DADOS,
        "servicos.csv"
    )

    servicos = []

    with open(
        caminho,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:

            if linha[0] == servico.id_servico:

                linha = servico.para_lista()

            servicos.append(linha)

    with open(
        caminho,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerows(servicos)



def excluir_servico(id_servico):

    caminho = os.path.join(
        PASTA_DADOS,
        "servicos.csv"
    )

    servicos = []

    with open(
        caminho,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.reader(arquivo)

        for linha in leitor:

            if linha[0] != id_servico:

                servicos.append(linha)

    with open(
        caminho,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerows(servicos)

