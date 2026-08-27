class Servico:

    def __init__(self, id_servico, nome, valor):

        self.id_servico = id_servico
        self.nome = nome
        self.valor = valor

    def exibir_dados(self):

        print(f"ID: {self.id_servico}")
        print(f"Serviço: {self.nome}")
        print(f"Valor: R${self.valor:.2f}")

    def para_lista(self):

        return [
            self.id_servico,
            self.nome,
            self.valor
        ]
    