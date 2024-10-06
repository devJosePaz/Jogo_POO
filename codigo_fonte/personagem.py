class protagonista:
    def __init__(self, nome, corrompido=False, mochila=None, decisoes=None):
        self.nome = nome
        self.corrompido = corrompido
        self.mochila = mochila = [{}]
        self.decisoes = decisoes

    def atacar(self):
        print(f"{self.protagonista} atacou")

    def receber_dano(self, dano):
        self.saude -= dano
        print(f"O {self.nome} tomou {self.dano} de dano")
    


