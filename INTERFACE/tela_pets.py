import tkinter as tk
from tkinter import messagebox

from pet import Pet
from arquivo import salvar_pet, criar_arquivos


# ==========================
# CORES
# ==========================

FUNDO = "#FCE4EC"
ROSA = "#F48FB1"
ROSA_ESCURO = "#EC407A"
TEXTO = "#880E4F"


# ==========================
# TELA DE PETS
# ==========================

def abrir_tela_pets():

    criar_arquivos()

    tela = tk.Toplevel()

    tela.title("Pets")
    tela.geometry("500x600")
    tela.resizable(False, False)
    tela.configure(bg=FUNDO)

    # ==========================
    # TÍTULO
    # ==========================

    tk.Label(
        tela,
        text="GERENCIAR PETS",
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

        cadastro.title("Cadastrar Pet")
        cadastro.geometry("500x650")
        cadastro.resizable(False, False)
        cadastro.configure(bg=FUNDO)

        tk.Label(
            cadastro,
            text="CADASTRO DE PET",
            font=("Arial", 20, "bold"),
            bg=FUNDO,
            fg=TEXTO
        ).pack(pady=25)

        # ID

        tk.Label(
            cadastro,
            text="ID do pet:",
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
            text="Nome:",
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

        # ESPÉCIE

        tk.Label(
            cadastro,
            text="Espécie:",
            font=("Arial", 11),
            bg=FUNDO,
            fg=TEXTO
        ).pack()

        entrada_especie = tk.Entry(
            cadastro,
            width=35,
            font=("Arial", 11)
        )

        entrada_especie.pack(pady=5)

        # RAÇA

        tk.Label(
            cadastro,
            text="Raça:",
            font=("Arial", 11),
            bg=FUNDO,
            fg=TEXTO
        ).pack()

        entrada_raca = tk.Entry(
            cadastro,
            width=35,
            font=("Arial", 11)
        )

        entrada_raca.pack(pady=5)

        # IDADE

        tk.Label(
            cadastro,
            text="Idade:",
            font=("Arial", 11),
            bg=FUNDO,
            fg=TEXTO
        ).pack()

        entrada_idade = tk.Entry(
            cadastro,
            width=35,
            font=("Arial", 11)
        )

        entrada_idade.pack(pady=5)

        # TUTOR

        tk.Label(
            cadastro,
            text="Tutor:",
            font=("Arial", 11),
            bg=FUNDO,
            fg=TEXTO
        ).pack()

        entrada_tutor = tk.Entry(
            cadastro,
            width=35,
            font=("Arial", 11)
        )

        entrada_tutor.pack(pady=5)

        # ==========================
        # SALVAR PET
        # ==========================

        def salvar():

            id_pet = entrada_id.get().strip()
            nome = entrada_nome.get().strip()
            especie = entrada_especie.get().strip()
            raca = entrada_raca.get().strip()
            idade = entrada_idade.get().strip()
            tutor = entrada_tutor.get().strip()

            if not id_pet or not nome or not especie or not raca or not idade or not tutor:

                messagebox.showwarning(
                    "Atenção",
                    "Preencha todos os campos!"
                )

                return

            pet = Pet(
                id_pet,
                nome,
                especie,
                raca,
                idade,
                tutor
            )

            salvar_pet(pet)

            messagebox.showinfo(
                "Sucesso",
                "Pet cadastrado com sucesso!"
            )

            entrada_id.delete(0, tk.END)
            entrada_nome.delete(0, tk.END)
            entrada_especie.delete(0, tk.END)
            entrada_raca.delete(0, tk.END)
            entrada_idade.delete(0, tk.END)
            entrada_tutor.delete(0, tk.END)

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
    # LISTAR
    # ==========================

    def listar():

        lista = tk.Toplevel(tela)

        lista.title("Pets Cadastrados")
        lista.geometry("500x550")
        lista.configure(bg=FUNDO)

        tk.Label(
            lista,
            text="PETS CADASTRADOS",
            font=("Arial", 20, "bold"),
            bg=FUNDO,
            fg=TEXTO
        ).pack(pady=25)

        texto = tk.Text(
            lista,
            width=50,
            height=22,
            font=("Arial", 10)
        )

        texto.pack(pady=10)

        try:

            with open(
                "dados/pets.csv",
                "r",
                encoding="utf-8"
            ) as arquivo:

                encontrou = False

                for linha in arquivo:

                    dados = linha.strip().split(",")

                    if len(dados) >= 6:

                        encontrou = True

                        texto.insert(
                            tk.END,
                            f"ID: {dados[0]}\n"
                            f"Nome: {dados[1]}\n"
                            f"Espécie: {dados[2]}\n"
                            f"Raça: {dados[3]}\n"
                            f"Idade: {dados[4]}\n"
                            f"Tutor: {dados[5]}\n"
                            + "-" * 40
                            + "\n"
                        )

                if not encontrou:

                    texto.insert(
                        tk.END,
                        "Nenhum pet cadastrado."
                    )

        except FileNotFoundError:

            texto.insert(
                tk.END,
                "Nenhum pet cadastrado."
            )

        texto.config(state="disabled")

    # ==========================
    # ATUALIZAR
    # ==========================

    def atualizar():

        messagebox.showinfo(
            "Atualizar Pet",
            "A atualização será feita na próxima etapa!"
        )

    # ==========================
    # EXCLUIR
    # ==========================

    def excluir():

        messagebox.showinfo(
            "Excluir Pet",
            "A exclusão será feita na próxima etapa!"
        )

    # ==========================
    # BOTÕES
    # ==========================

    tk.Button(
        tela,
        text="CADASTRAR PET",
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
        text="LISTAR PETS",
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
        text="ATUALIZAR PET",
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
        text="EXCLUIR PET",
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
    