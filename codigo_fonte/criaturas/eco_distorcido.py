class EcoTorcido:
    def __init__(self):
        self.nome = "Eco-Torcido"  # Nome da criatura
        self.saude = 150            # Saúde inicial
        self.dano_electrico = 20    # Dano que pode causar

    def atacar(self, alvo):
        # Método que representa o ataque da criatura
        print(f"{self.nome} ataca {alvo.nome} causando {self.dano_electrico} de dano elétrico.")

    def receber_dano(self, dano):
        # Método que reduz a saúde quando a criatura é atacada
        self.saude -= dano
        print(f"{self.nome} recebe {dano} de dano. Saúde restante: {self.saude}")

    def verificar_morte(self):
        # Método para verificar se a criatura foi derrotada
        if self.saude <= 0:
            print(f"{self.nome} foi derrotado.")
            return True
        return False
