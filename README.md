# Jogo Futurista Pós-Apocalíptico

## Descrição

Este é um jogo linear que se passa em um mundo futurista e distorcido, onde o protagonista luta para sobreviver em uma cidade dominada por aberrações. O jogador faz escolhas que afetam o desfecho da história, enquanto tenta manter sua sanidade e derrotar criaturas monstruosas.

## Estrutura do Jogo

O jogo é composto por uma interface simples que exibe o progresso da história e as escolhas do jogador. As aberrações que você encontrará possuem diferentes habilidades, e o protagonista deve lutar ou fugir enquanto tenta não se distorcer.

### Personagens Principais

- **Protagonista**: Um sobrevivente que deve resistir à distorção enquanto enfrenta aberrações. Ele não tem poderes, apenas sua vontade de sobreviver.
- **Eco-Torcido**: Uma aberração formada por resíduos tecnológicos e orgânicos. Vulnerável a eletricidade de alta voltagem.
- **Sombra Insana**: Um ser que se esconde nas sombras e drena a sanidade dos humanos. Vulnerável à luz intensa.
- **Ancião Desfigurado**: Uma criatura deformada com poderes hipnóticos. Pode ser interrompido por ruídos caóticos.

## Funcionalidades

- **Sistema de Combate**: O jogador pode enfrentar aberrações ou usar estratégias para derrotá-las.
- **Escolhas**: As decisões do jogador impactam o final da história.
- **Mochila**: O jogador coleta itens ao longo da jornada para ajudá-lo em batalhas ou na história.

## Como Executar o Jogo

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/jogo-futurista.git

jogo_futurista/
│
├── recursos/                   # Pasta para recursos como imagens, sons, etc.
│
├── codigo_fonte/               # Código-fonte principal do jogo
│   ├── __init__.py             # (Pode ser vazio, apenas para tratar codigo_fonte como pacote)
│   ├── iniciar_jogo.py         # Arquivo principal que executa o jogo
│   ├── personagem.py           # Classe do protagonista
│   ├── criaturas/              # Pasta contendo as aberrações
│   │   ├── __init__.py         # (Pode ser vazio)
│   │   ├── eco_torcido.py      # Classe da primeira criatura
│   │   ├── sombra_insana.py    # Classe da segunda criatura
│   │   └── anciao_desfigurado.py # Classe da terceira criatura
│   └── utilidades/             # Utilitários ou funções auxiliares
│       ├── historia.py         # Gerencia a história e as escolhas
│       └── combate.py          # Funções relacionadas a combate
│
├── testes/                     # Testes para validar as funcionalidades
│   ├── test_personagem.py      # Testes para a classe Personagem
│   ├── test_criaturas.py       # Testes para as criaturas
│   └── test_historia.py        # Testes para o progresso da história
│
└── LEIA-ME.md                  # Explicação do projeto, como executar e detalhes do jogo
