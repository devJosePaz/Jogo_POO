import sys
import os
# Adiciona o diretório pai ao caminho
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from codigo_fonte.personagem import Protagonista  # Certifique-se de usar a letra maiúscula

def testar_protagonista():
    # Criando uma instância de Protagonista
    player = Protagonista(nome="Player", mochila=["faca"])  

    # Testando o ataque
    player.atacar()

    # Testando o dano
    player.receber_dano(20)

    player.exibir_mochila()

    
testar_protagonista()
