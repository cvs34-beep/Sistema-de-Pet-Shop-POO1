import tkinter as tk
from tkinter import messagebox

from cliente import Cliente
from arquivo import salvar_cliente, criar_arquivos


# CORES
FUNDO = "#FCE4EC"
ROSA = "#F48FB1"
ROSA_ESCURO = "#EC407A"
TEXTO = "#880E4F"


def abrir_tela_clientes():

    criar_arquivos()

    tela = tk.Toplevel()
    tela.title("Clientes")
    tela.geometry("500x550")
    tela.resizable(False, False)
    tela.configure(bg=FUNDO)


    # TÍTULO
    tk.Label(
        tela,
        text="GERENCIAR CLIENTES",
        font=("Arial", 22, "bold"),
        bg=FUNDO,
        fg=TEXTO
    ).pack(pady=35)


    tk.Label(
        tela,
        text="Escolha uma operação:",
        font=("Arial", 12),
        bg=FUNDO,
        fg=TEXTO
    ).pack(pady=5)


    # ==========================
    # CADASTRAR
    # ==========================

    def cadastrar():

        cadastro = tk.Toplevel(tela)
        cadastro.title("Cadastrar Cliente")
        cadastro.geometry("500x500")
        cadastro.resizable(False, False)
        cadastro.configure(bg=FUNDO)


        tk.Label(
            cadastro,
            text="CADASTRO DE CLIENTE",
            font=("Arial", 20, "bold"),
            bg=FUNDO,
            fg=TEXTO
        ).pack(pady=30)


        tk.Label(
            cadastro,
            text="ID do cliente:",
            bg=FUNDO,
            fg=TEXTO,
            font=("Arial", 11)
        ).pack()

        entrada_id = tk.Entry(
            cadastro,
            width=35,
            font=("Arial", 11)
        )
        entrada_id.pack(pady=5)


        tk.Label(
            cadastro,
            text="Nome:",
            bg=FUNDO,
            fg=TEXTO,
            font=("Arial", 11)
        ).pack()

        entrada_nome = tk.Entry(
            cadastro,
            width=35,
            font=("Arial", 11)
        )
        entrada_nome.pack(pady=5)


        tk.Label(
            cadastro,
            text="Telefone:",
            bg=FUNDO,
            fg=TEXTO,
            font=("Arial", 11)
        ).pack()

        entrada_telefone = tk.Entry(
            cadastro,
            width=35,
            font=("Arial", 11)
        )
        entrada_telefone.pack(pady=5)


        def salvar():

            id_cliente = entrada_id.get()
            nome = entrada_nome.get()
            telefone = entrada_telefone.get()


            if not id_cliente or not nome or not telefone:

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


        tk.Button(
            cadastro,
            text="CADASTRAR",
            font=("Arial", 12, "bold"),
            width=20,
            height=2,
            bg=ROSA,
            fg="white",
            activebackground=ROSA_ESCURO,
            command=salvar
        ).pack(pady=25)


        tk.Button(
            cadastro,
            text="FECHAR",
            font=("Arial", 11),
            width=20,
            command=cadastro.destroy
        ).pack()


    # ==========================
    # LISTAR
    # ==========================

    def listar():

        janela_lista = tk.Toplevel(tela)
        janela_lista.title("Clientes Cadastrados")
        janela_lista.geometry("500x500")
        janela_lista.configure(bg=FUNDO)


        tk.Label(
            janela_lista,
            text="CLIENTES CADASTRADOS",
            font=("Arial", 20, "bold"),
            bg=FUNDO,
            fg=TEXTO
        ).pack(pady=25)


        texto = tk.Text(
            janela_lista,
            width=50,
            height=20,
            font=("Arial", 10)
        )

        texto.pack(pady=10)


        try:

            with open(
                "dados/clientes.csv",
                "r",
                encoding="utf-8"
            ) as arquivo:

                encontrou = False

                for linha in arquivo:

                    dados = linha.strip().split(",")

                    if len(dados) >= 3:

                        encontrou = True

                        texto.insert(
                            tk.END,
                            f"ID: {dados[0]}\n"
                            f"Nome: {dados[1]}\n"
                            f"Telefone: {dados[2]}\n"
                            + "-" * 40 + "\n"
                        )


                if not encontrou:

                    texto.insert(
                        tk.END,
                        "Nenhum cliente cadastrado."
                    )


        except FileNotFoundError:

            texto.insert(
                tk.END,
                "Nenhum cliente cadastrado."
            )


        texto.config(state="disabled")


    # ==========================
    # ATUALIZAR
    # ==========================

    def atualizar():

        messagebox.showinfo(
            "Atualizar",
            "A atualização será feita na próxima etapa!"
        )


    # ==========================
    # EXCLUIR
    # ==========================

    def excluir():

        messagebox.showinfo(
            "Excluir",
            "A exclusão será feita na próxima etapa!"
        )


    # BOTÕES

    tk.Button(
        tela,
        text="CADASTRAR CLIENTE",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        bg=ROSA,
        fg="white",
        activebackground=ROSA_ESCURO,
        command=cadastrar
    ).pack(pady=8)


    tk.Button(
        tela,
        text="LISTAR CLIENTES",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        bg=ROSA,
        fg="white",
        activebackground=ROSA_ESCURO,
        command=listar
    ).pack(pady=8)


    tk.Button(
        tela,
        text="ATUALIZAR CLIENTE",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        bg=ROSA,
        fg="white",
        activebackground=ROSA_ESCURO,
        command=atualizar
    ).pack(pady=8)


    tk.Button(
        tela,
        text="EXCLUIR CLIENTE",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        bg=ROSA,
        fg="white",
        activebackground=ROSA_ESCURO,
        command=excluir
    ).pack(pady=8)


    tk.Button(
        tela,
        text="VOLTAR",
        font=("Arial", 11),
        width=25,
        command=tela.destroy
    ).pack(pady=15)