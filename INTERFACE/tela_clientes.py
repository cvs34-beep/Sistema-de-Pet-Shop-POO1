import tkinter as tk
from tkinter import messagebox

from cliente import Cliente
from arquivo import salvar_cliente, criar_arquivos


def abrir_tela_clientes():

    criar_arquivos()

    tela = tk.Toplevel()
    tela.title("Cadastro de Clientes")
    tela.geometry("500x500")
    tela.resizable(False, False)

    # ==========================
    # TÍTULO
    # ==========================

    titulo = tk.Label(
        tela,
        text="CADASTRO DE CLIENTES",
        font=("Arial", 20, "bold")
    )

    titulo.pack(pady=30)

    # ==========================
    # ID
    # ==========================

    label_id = tk.Label(
        tela,
        text="ID do cliente:",
        font=("Arial", 11)
    )

    label_id.pack()

    entrada_id = tk.Entry(
        tela,
        width=35,
        font=("Arial", 11)
    )

    entrada_id.pack(pady=5)

    # ==========================
    # NOME
    # ==========================

    label_nome = tk.Label(
        tela,
        text="Nome:",
        font=("Arial", 11)
    )

    label_nome.pack()

    entrada_nome = tk.Entry(
        tela,
        width=35,
        font=("Arial", 11)
    )

    entrada_nome.pack(pady=5)

    # ==========================
    # TELEFONE
    # ==========================

    label_telefone = tk.Label(
        tela,
        text="Telefone:",
        font=("Arial", 11)
    )

    label_telefone.pack()

    entrada_telefone = tk.Entry(
        tela,
        width=35,
        font=("Arial", 11)
    )

    entrada_telefone.pack(pady=5)

    # ==========================
    # CADASTRAR
    # ==========================

    def cadastrar():

        id_cliente = entrada_id.get()
        nome = entrada_nome.get()
        telefone = entrada_telefone.get()

        if id_cliente == "" or nome == "" or telefone == "":
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos!"
            )
            return

        cliente = Cliente(
            id_cliente,
            nome,
            telefone
        )

        salvar_cliente(cliente)

        messagebox.showinfo(
            "Sucesso",
            "Cliente cadastrado com sucesso!"
        )

        entrada_id.delete(0, tk.END)
        entrada_nome.delete(0, tk.END)
        entrada_telefone.delete(0, tk.END)

    # ==========================
    # BOTÃO CADASTRAR
    # ==========================

    botao_cadastrar = tk.Button(
        tela,
        text="CADASTRAR",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        command=cadastrar
    )

    botao_cadastrar.pack(pady=25)

    # ==========================
    # BOTÃO FECHAR
    # ==========================

    botao_fechar = tk.Button(
        tela,
        text="FECHAR",
        font=("Arial", 11),
        width=20,
        command=tela.destroy
    )

    botao_fechar.pack()
    