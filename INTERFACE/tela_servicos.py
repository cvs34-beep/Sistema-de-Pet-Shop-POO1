import tkinter as tk
from tkinter import messagebox

from servico import Servico
from arquivo import salvar_servico, criar_arquivos


# ==========================
# CORES
# ==========================

FUNDO = "#FCE4EC"
ROSA = "#F48FB1"
ROSA_ESCURO = "#EC407A"
TEXTO = "#880E4F"


# ==========================
# TELA DE SERVIÇOS
# ==========================

def abrir_tela_servicos():

    criar_arquivos()

    tela = tk.Toplevel()
    tela.title("Serviços")
    tela.geometry("500x550")
    tela.resizable(False, False)
    tela.configure(bg=FUNDO)

    # ==========================
    # TÍTULO
    # ==========================

    tk.Label(
        tela,
        text="GERENCIAR SERVIÇOS",
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
    # CADASTRAR SERVIÇO
    # ==========================

    def cadastrar():

        cadastro = tk.Toplevel(tela)

        cadastro.title("Cadastrar Serviço")
        cadastro.geometry("500x500")
        cadastro.resizable(False, False)
        cadastro.configure(bg=FUNDO)

        tk.Label(
            cadastro,
            text="CADASTRO DE SERVIÇO",
            font=("Arial", 20, "bold"),
            bg=FUNDO,
            fg=TEXTO
        ).pack(pady=30)

        # ID

        tk.Label(
            cadastro,
            text="ID do serviço:",
            font=("Arial", 11),
            bg=FUNDO,
            fg=TEXTO
        ).pack()

        entrada_id = tk.Entry(
            cadastro,
            width=35,
            font=("Arial", 11)
        )

        entrada_id.pack(pady=5)

        # NOME

        tk.Label(
            cadastro,
            text="Nome do serviço:",
            font=("Arial", 11),
            bg=FUNDO,
            fg=TEXTO
        ).pack()

        entrada_nome = tk.Entry(
            cadastro,
            width=35,
            font=("Arial", 11)
        )

        entrada_nome.pack(pady=5)

        # VALOR

        tk.Label(
            cadastro,
            text="Valor:",
            font=("Arial", 11),
            bg=FUNDO,
            fg=TEXTO
        ).pack()

        entrada_valor = tk.Entry(
            cadastro,
            width=35,
            font=("Arial", 11)
        )

        entrada_valor.pack(pady=5)

        # ==========================
        # SALVAR
        # ==========================

        def salvar():

            id_servico = entrada_id.get().strip()
            nome = entrada_nome.get().strip()
            valor = entrada_valor.get().strip()

            if not id_servico or not nome or not valor:

                messagebox.showwarning(
                    "Atenção",
                    "Preencha todos os campos!"
                )

                return

            try:
                valor = float(valor.replace(",", "."))

            except ValueError:

                messagebox.showwarning(
                    "Atenção",
                    "Digite um valor válido."
                )

                return

            servico = Servico(
                id_servico,
                nome,
                valor
            )

            salvar_servico(servico)

            messagebox.showinfo(
                "Sucesso",
                "Serviço cadastrado com sucesso!"
            )

            entrada_id.delete(0, tk.END)
            entrada_nome.delete(0, tk.END)
            entrada_valor.delete(0, tk.END)

        # BOTÃO CADASTRAR

        tk.Button(
            cadastro,
            text="CADASTRAR",
            font=("Arial", 12, "bold"),
            width=20,
            height=2,
            bg=ROSA,
            fg="white",
            activebackground=ROSA_ESCURO,
            activeforeground="white",
            command=salvar
        ).pack(pady=25)

        # BOTÃO FECHAR

        tk.Button(
            cadastro,
            text="FECHAR",
            font=("Arial", 11),
            width=20,
            command=cadastro.destroy
        ).pack()

    # ==========================
    # LISTAR SERVIÇOS
    # ==========================

    def listar():

        lista = tk.Toplevel(tela)

        lista.title("Serviços Cadastrados")
        lista.geometry("500x500")
        lista.configure(bg=FUNDO)

        tk.Label(
            lista,
            text="SERVIÇOS CADASTRADOS",
            font=("Arial", 20, "bold"),
            bg=FUNDO,
            fg=TEXTO
        ).pack(pady=25)

        texto = tk.Text(
            lista,
            width=50,
            height=20,
            font=("Arial", 10)
        )

        texto.pack(pady=10)

        try:

            with open(
                "dados/servicos.csv",
                "r",
                encoding="utf-8"
            ) as arquivo:

                encontrou = False

                for linha in arquivo:

                    dados = linha.strip().split(",")

                    if len(dados) >= 3:

                        encontrou = True

                        try:
                            valor = float(dados[2])
                            valor_formatado = f"R$ {valor:.2f}"
                        except ValueError:
                            valor_formatado = dados[2]

                        texto.insert(
                            tk.END,
                            f"ID: {dados[0]}\n"
                            f"Serviço: {dados[1]}\n"
                            f"Valor: {valor_formatado}\n"
                            + "-" * 40
                            + "\n"
                        )

                if not encontrou:

                    texto.insert(
                        tk.END,
                        "Nenhum serviço cadastrado."
                    )

        except FileNotFoundError:

            texto.insert(
                tk.END,
                "Nenhum serviço cadastrado."
            )

        texto.config(state="disabled")

    # ==========================
    # ATUALIZAR
    # ==========================

    def atualizar():

        messagebox.showinfo(
            "Atualizar Serviço",
            "A atualização será feita na próxima etapa!"
        )

    # ==========================
    # EXCLUIR
    # ==========================

    def excluir():

        messagebox.showinfo(
            "Excluir Serviço",
            "A exclusão será feita na próxima etapa!"
        )

    # ==========================
    # BOTÕES
    # ==========================

    tk.Button(
        tela,
        text="CADASTRAR SERVIÇO",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        bg=ROSA,
        fg="white",
        activebackground=ROSA_ESCURO,
        activeforeground="white",
        command=cadastrar
    ).pack(pady=8)

    tk.Button(
        tela,
        text="LISTAR SERVIÇOS",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        bg=ROSA,
        fg="white",
        activebackground=ROSA_ESCURO,
        activeforeground="white",
        command=listar
    ).pack(pady=8)

    tk.Button(
        tela,
        text="ATUALIZAR SERVIÇO",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        bg=ROSA,
        fg="white",
        activebackground=ROSA_ESCURO,
        activeforeground="white",
        command=atualizar
    ).pack(pady=8)

    tk.Button(
        tela,
        text="EXCLUIR SERVIÇO",
        font=("Arial", 12, "bold"),
        width=25,
        height=2,
        bg=ROSA,
        fg="white",
        activebackground=ROSA_ESCURO,
        activeforeground="white",
        command=excluir
    ).pack(pady=8)

    tk.Button(
        tela,
        text="VOLTAR",
        font=("Arial", 11),
        width=25,
        command=tela.destroy
    ).pack(pady=15)
    