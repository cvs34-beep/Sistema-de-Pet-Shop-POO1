class Servico:
    def __init__(self, id_servico, nome, valor):
        self.id_servico = id_servico
        self.nome = nome
        self.valor = valor

    def exibir_dados(self):
        print("\n===== DADOS DO SERVIÇO =====")
        print(f"ID: {self.id_servico}")
        print(f"Serviço: {self.nome}")
        print(f"Valor: R$ {self.valor}")

    def atualizar(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def para_lista(self):
        return [
            self.id_servico,
            self.nome,
            self.valor
        ]

    @classmethod
    def de_lista(cls, dados):
        return cls(
            dados[0],
            dados[1],
            dados[2]
        )