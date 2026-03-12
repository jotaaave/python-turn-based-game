from methods.texteffect import line

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
