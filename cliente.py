class Cliente:

    def __init__(self, id_cliente, nome, telefone, email):

        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.email = email

        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.email = email


    def exibir_dados(self):
        print("\n===== DADOS DO CLIENTE =====")
        print(f"ID: {self.id_cliente}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")

        print(f"ID: {self.id_cliente}")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")



    def atualizar(self, nome, telefone, email):

        self.nome = nome
        self.telefone = telefone
        self.email = email



    def para_lista(self):

        return [
            self.id_cliente,
            self.nome,
            self.telefone,
            self.email
        ]


    @classmethod
    def de_lista(cls, dados):

        return cls(
            dados[0],
            dados[1],
            dados[2],
            dados[3]
        )

    