class Cliente:
    def __init__(self, id_cliente, nome, telefone):
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone

    def exibir_dados(self):
        print("\n===== DADOS DO CLIENTE =====")
        print(f"ID: {self.id_cliente}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")

    def atualizar(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def para_lista(self):
        return [
            self.id_cliente,
            self.nome,
            self.telefone
        ]

    @classmethod
    def de_lista(cls, dados):
        return cls(
            dados[0],
            dados[1],
            dados[2]
        )