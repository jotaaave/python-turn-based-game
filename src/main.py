from methods.texteffect import textLine, lineText
from actions import menu, player_actions

class Game:
    on = True
    player = None
    game_state = 0

    @classmethod
    def power_off(cls):
        cls.on = False

    @classmethod
    def check_game(cls):
        return cls.on
    
    @classmethod
    def change_state(cls, new_state):
        cls.game_state = new_state
    
    @classmethod
    def setup_player(cls, player):
        cls.player = player

    @classmethod
    def get_player(cls):
        return cls.player

modelMenu = {
    0: [ # Menu Principal
        "Novo Jogo [1]",
        "Sair [2]"
    ],
    1: [ # Tela de Ações
        "Bem vindo a sua aventura!\n",
        lineText(),
        "\n"
        "Informações importantes! Seu personagem é criado automaticamente toda vez que apertar em [Novo Jogo]\n"
        "\nAções:\n[1]. Checar status\n[2]. Olhar inventario\n[3]. Ação de explorar\n[4]. Magias\n[5]. Menu"
    ],
    2: [ # Tela nula para ver informações
    ],
}

allActionsScreenDict = {
    0: { # Menu Actions
        1: menu.new_game,
        2: menu.power_off
    },
    1: { # Player Actions
        1: player_actions.check_status,
        2: None,
        3: None,
        4: None,
        5: None,
    },
    2: {
        1: lambda Game: Game.change_state(1)
    }
}

def showMenu(menu):
    for text in modelMenu[menu]:
        print(text)

actionScreenDict = {
    1: "Checar Status",
    2: "Olhar inv",
    3: "explorar",
    4: "magias"
}

def playerChoiceAction(choice, menuNumber):
    allActionsScreenDict[menuNumber][int(choice)](Game)

textLine('WELCOME TO THE GAME (YES YOU LOSE)')

while Game.check_game():
    try:
        if (not Game.check_game()): break
        showMenu(Game.game_state)
        playerChoice = input("\nEscolha sua ação: ")
        playerChoiceAction(playerChoice, Game.game_state)
    except:
        print('Valor invalido tente novamente!')
        continue


