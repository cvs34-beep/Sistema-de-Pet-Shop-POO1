class Servico:

    def __init__(self, id_servico, nome, descricao, valor):

        self.id_servico = id_servico
        self.nome = nome
        self.descricao = descricao
        self.valor = valor



    def exibir_dados(self):

        print("\n===== DADOS DO SERVIÇO =====")
        print(f"ID: {self.id_servico}")
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Valor: R$ {self.valor}")



    def atualizar(self, nome, descricao, valor):

        self.nome = nome
        self.descricao = descricao
        self.valor = valor



    def para_lista(self):

        return [
            self.id_servico,
            self.nome,
            self.descricao,
            self.valor
        ]



    @classmethod
    def de_lista(cls, dados):

        return cls(
            dados[0],
            dados[1],
            dados[2],
            dados[3]
        )