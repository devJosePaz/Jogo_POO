class Protagonista:
    def __init__(self, nome, corrompido=False, mochila=None, decisoes=None):
        self.nome = nome
        self.corrompido = corrompido
        self.mochila = mochila or []  # Inicializa mochila como lista vazia se não for fornecida
        self.decisoes = decisoes
        self.saude = 100

    def atacar(self):
        print(f"{self.nome} ataca!")

    def receber_dano(self, dano):
        self.saude -= dano
        print(f"O {self.nome} tomou {dano} de dano. Saúde restante: {self.saude}")

    def exibir_mochila(self):
        if self.mochila:
            print(f"Mochila de {self.nome}: {', '.join(self.mochila)}")
        else:
            print(f"A mochila de {self.nome} está vazia.")
