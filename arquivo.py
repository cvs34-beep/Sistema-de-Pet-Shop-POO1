import csv
import os
from cliente import Cliente

PASTA_DADOS = "dados"


def criar_arquivos():
    arquivos = [
        "clientes.csv",
        "pets.csv",
        "servicos.csv"
    ]

    if not os.path.exists(PASTA_DADOS):
        os.mkdir(PASTA_DADOS)

    for arquivo in arquivos:
        caminho = os.path.join(PASTA_DADOS, arquivo)

        if not os.path.exists(caminho):
            with open(caminho, "w", newline="", encoding="utf-8") as csvfile:
                pass

def salvar_cliente(cliente):
    caminho = os.path.join(PASTA_DADOS, "clientes.csv")

    with open(caminho, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(cliente.para_lista())

def salvar_pet(pet):
    caminho = os.path.join(PASTA_DADOS, "pets.csv")

    with open(caminho, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(pet.para_lista())
