from methods.texteffect import textLine
from methods.player_create import create_player

def power_off(Game):
    print('\n')
    textLine("Obrigado por jogar")
    Game.power_off()
    return

def new_game(Game):
    name = input('Digite nome do personagem: ')
    character = create_player(name)
    Game.setup_player(character)
    Game.change_state(1)