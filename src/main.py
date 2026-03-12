from methods.texteffect import line, downLineText, textLine, lineText
from methods.player_create import create_player

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
    def setup_player(cls, player):
        cls.player = player

modelMenu = {
    0: [
        "Novo Jogo [1]",
        "Sair [2]"
    ],
    1: [
        "Bem vindo a sua aventura!\n",
        lineText(),
        "\n"
        "Informações importantes! Seu personagem é criado automaticamente toda vez que apertar em [Novo Jogo]"
    ]
}

def showMenu(menu):
    textLine('WELCOME TO THE GAME (YES YOU LOSE)')

    for text in modelMenu[menu]:
        print(text)

def playerChoiceAction(choice, menuNumber):
    if choice == "2" and menuNumber == 0:
        print('\n')
        textLine("Obrigado por jogar")
        Game.power_off()
        return
    
    if choice == "1" and menuNumber == 0:
        name = input('Digite nome do personagem: ')
        character = create_player(name)
        Game.setup_player(character)

while Game.check_game():
    for menuNumber in range(len(modelMenu)):
        if (not Game.check_game()): break
        showMenu(menuNumber)
        playerChoice = input("\nEnter your action: ")
        playerChoiceAction(playerChoice, menuNumber)


