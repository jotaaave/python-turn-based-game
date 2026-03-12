from methods.texteffect import line
from random import choice, randrange

def check_status(Game):
    Game.change_state(2)
    player = Game.player
    while Game.check_state() == 2:
        print(f"\nINFORMAÇÔES DO JOGADOR:\nNOME: {player["name"]}\nFORÇA: {player["power"]}\nVIDA: {player["life"]}\nINTELECTO: {player["intelect"]}\n")
        print('\n[1]. Voltar')

        action = input('\nEscolha uma ação: ')

        if (int(action) == 1):
            Game.change_state(1)
            break

def view_inventory(Game):
    Game.change_state(2)
    player = Game.player
    while Game.check_state() == 2:
        print('\nINVENTARIO DO JOGADOR:')
        line()

        if (player["inventory"]):
            count = 0
            for item in player["inventory"]:
                count += 1
                print(f"[{count}]. {item["name"]}")
        else:
            print('Inventário está vazio! Vá explorar')

        print('\n[1]. Voltar')

        action = input('\nEscolha uma ação: ')

        if (int(action) == 1):
            Game.change_state(1)
            break

def explore(Game):
    Game.change_state(2)
    # O jogador podera ter algumas coisas quando explorar
    # Encontrar báu, Encontrar monstro, Encontrar área, Encontrar NPC, Encontrar Aliados
    # E cada encontro desse é totalmente aleatorio, podendo ser qualquer monstro, npc, area, etc
    exploreType = {
        "chests": [
            {
                "name": "Báu Comum",
                "rarity": 1,
            }
        ],
        "monsters": [
            {
                "name": "Esqueleto",
                "life": 10,
                "attack": [
                    {
                        "attack_name": "Flechada",
                        "damage": 12 # Esse número é para decidir entre 1 e damage para dar dano (1d12)
                    }
                ]
            }
        ],
        # "npcs": [],
        # "locals": [],
        # "alies": []
    }

    selectedExploration = choice(list(exploreType.keys()))
    event = exploreType[selectedExploration]
    
    if (selectedExploration == "chests"):
        while Game.check_state() == 2:
            line()
            print(f'Booa! Você encontrou um {event[0]['name']}!')
            print('\n[1]. Pegar items\n[2]. Descartar\n')
            value = input('Escolha sua ação: ')
            Game.change_state(1)

    if (selectedExploration == "monsters"):
        while Game.check_state() == 2:
            mob = {
                'name': event[0]['name'],
                'life': event[0]['life'] * randrange(1, 6),
                'attack': event[0]['attack']
            }

            line()
            print(f"Você foi interceptado por um {event[0]['name']}!\n")
            print(f'[1]. Atacar\n[2]. Usar item\n{'[3]. Fugir\n' if not Game.check_battle_state() else '\n'}')
            value = input('Escolha sua ação: ')

            if (value == '1'):
                Game.set_battle(True)

            if (value == '3' and not Game.check_battle_state()):
                Game.change_state(1)
                mob = None