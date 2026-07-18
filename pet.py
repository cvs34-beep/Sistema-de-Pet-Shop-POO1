class Pet:
    def __init__(self, id_pet, nome, especie, raca, idade, tutor):
        self.id_pet = id_pet
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.tutor = tutor

    def exibir_dados(self):
        print(f"ID: {self.id_pet}")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Raça: {self.raca}")
        print(f"Idade: {self.idade}")
        print(f"Tutor: {self.tutor}")

    def para_lista(self):
        return [
            self.id_pet,
            self.nome,
            self.especie,
            self.raca,
            self.idade,
            self.tutor
        ]
    