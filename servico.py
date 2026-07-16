class Servico:
    def __init__(self, id_servico, descricao, valor):
        self.id_servico = id_servico
        self.descricao = descricao
        self.valor = valor

    def exibir_dados(self):
        print(f"ID: {self.id_servico}")
        print(f"Descrição: {self.descricao}")
        print(f"Valor: R$ {self.valor:.2f}")
        