class Cliente:
    def __init__(self, id_cliente, nome, telefone):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone

    def exibir_dados(self):
        print("\n===== CLIENTE =====")
        print(f"ID: {self.id_cliente}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")

    def para_lista(self):
        return [
            self.id_cliente,
            self.nome,
            self.telefone
        ]