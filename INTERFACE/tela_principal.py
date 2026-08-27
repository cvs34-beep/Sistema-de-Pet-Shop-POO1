import tkinter as tk
from tkinter import messagebox

from INTERFACE.tela_clientes import abrir_tela_clientes

def abrir_clientes():
    abrir_tela_clientes()

def abrir_pets():
    messagebox.showinfo(
        "Pets",
        "A tela de Pets será desenvolvida em breve!"
    )


def abrir_servicos():
    messagebox.showinfo(
        "Serviços",
        "A tela de Serviços será desenvolvida em breve!"
    )


def sair():
    resposta = messagebox.askyesno(
        "Sair",
        "Deseja realmente sair do sistema?"
    )

    if resposta:
        janela.destroy()


# ==========================
# JANELA PRINCIPAL
# ==========================

janela = tk.Tk()

janela.title("Sistema Pet Shop")
janela.geometry("500x500")
janela.resizable(False, False)


# ==========================
# TÍTULO
# ==========================

titulo = tk.Label(
    janela,
    text="SISTEMA PET SHOP",
    font=("Arial", 24, "bold")
)

titulo.pack(pady=40)


subtitulo = tk.Label(
    janela,
    text="Gerenciamento de Pet Shop",
    font=("Arial", 12)
)

subtitulo.pack(pady=5)


# ==========================
# BOTÃO CLIENTES
# ==========================

botao_clientes = tk.Button(
    janela,
    text="CLIENTES",
    font=("Arial", 14, "bold"),
    width=20,
    height=2,
    command=abrir_clientes
)

botao_clientes.pack(pady=10)


# ==========================
# BOTÃO PETS
# ==========================

botao_pets = tk.Button(
    janela,
    text="PETS",
    font=("Arial", 14, "bold"),
    width=20,
    height=2,
    command=abrir_pets
)

botao_pets.pack(pady=10)


# ==========================
# BOTÃO SERVIÇOS
# ==========================

botao_servicos = tk.Button(
    janela,
    text="SERVIÇOS",
    font=("Arial", 14, "bold"),
    width=20,
    height=2,
    command=abrir_servicos
)

botao_servicos.pack(pady=10)


# ==========================
# BOTÃO SAIR
# ==========================

botao_sair = tk.Button(
    janela,
    text="SAIR",
    font=("Arial", 14, "bold"),
    width=20,
    height=2,
    command=sair
)

botao_sair.pack(pady=10)


# ==========================
# INICIAR JANELA
# ==========================

janela.mainloop()
