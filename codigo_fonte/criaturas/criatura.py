class Criatura:
    def __init__(self, nome, saude, intensidade_corrupcao):
        self.nome = nome
        self.saude = saude
        self.intensidade_corrupcao = intensidade_corrupcao

    def corromper(self, protagonista):
        pass


    def receber_dano(self, dano):   
        self.saude -= dano
        print(f"{self.nome} recebeu {self.dano} de dano. Saúde restante: {self.saude} ")


class ecoDistorcido(Criatura):
    def corromper(self, protagonista):
        protagonista.sanidade -= self.intensidade_corrupcao
