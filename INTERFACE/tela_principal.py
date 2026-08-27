import tkinter as tk
from tkinter import messagebox

from .tela_clientes import abrir_tela_clientes
from .tela_pets import abrir_tela_pets
from .tela_servicos import abrir_tela_servicos


# ==============================
# CORES DO SISTEMA
# ==============================

FUNDO = "#FCE4EC"
ROSA = "#F48FB1"
ROSA_ESCURO = "#EC407A"
TEXTO = "#880E4F"


# ==============================
# FUNÇÕES
# ==============================

def abrir_clientes():
    abrir_tela_clientes()


def abrir_pets():
    abrir_tela_pets()


def abrir_servicos():
    abrir_tela_servicos()


def sair():
    resposta = messagebox.askyesno(
        "Sair",
        "Deseja realmente sair do sistema?"
    )

    if resposta:
        janela.destroy()


# ==============================
# JANELA PRINCIPAL
# ==============================

janela = tk.Tk()

janela.title("Sistema Pet Shop")
janela.geometry("500x600")
janela.resizable(False, False)
janela.configure(bg=FUNDO)


# ==============================
# TÍTULO
# ==============================

tk.Label(
    janela,
    text="🐾 SISTEMA PET SHOP 🐾",
    font=("Arial", 24, "bold"),
    bg=FUNDO,
    fg=TEXTO
).pack(pady=(45, 10))


tk.Label(
    janela,
    text="Gerenciamento de Pet Shop",
    font=("Arial", 12),
    bg=FUNDO,
    fg=TEXTO
).pack(pady=(0, 35))


# ==============================
# BOTÃO CLIENTES
# ==============================

tk.Button(
    janela,
    text="CLIENTES",
    font=("Arial", 14, "bold"),
    width=22,
    height=2,
    bg=ROSA,
    fg="white",
    activebackground=ROSA_ESCURO,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=abrir_clientes
).pack(pady=10)


# ==============================
# BOTÃO PETS
# ==============================

tk.Button(
    janela,
    text="PETS",
    font=("Arial", 14, "bold"),
    width=22,
    height=2,
    bg=ROSA,
    fg="white",
    activebackground=ROSA_ESCURO,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=abrir_pets
).pack(pady=10)


# ==============================
# BOTÃO SERVIÇOS
# ==============================

tk.Button(
    janela,
    text="SERVIÇOS",
    font=("Arial", 14, "bold"),
    width=22,
    height=2,
    bg=ROSA,
    fg="white",
    activebackground=ROSA_ESCURO,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=abrir_servicos
).pack(pady=10)


# ==============================
# BOTÃO SAIR
# ==============================

tk.Button(
    janela,
    text="SAIR",
    font=("Arial", 14, "bold"),
    width=22,
    height=2,
    bg=ROSA,
    fg="white",
    activebackground=ROSA_ESCURO,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=sair
).pack(pady=10)


# ==============================
# INICIAR SISTEMA
# ==============================

janela.mainloop()
