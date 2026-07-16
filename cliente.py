class Cliente:
    def __init__(self, id_cliente, nome, telefone):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone

    def exibir_dados(self):
        print(f"ID: {self.id_cliente}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        