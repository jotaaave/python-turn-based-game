def check_status(Game):
    Game.change_state(2)
    player = Game.player
    print(f"\nINFORMAÇÔES DO JOGADOR:\nNOME: {player["name"]}\nFORÇA: {player["power"]}\nVIDA: {player["life"]}\nINTELECTO: {player["intelect"]}\n")
    print('\n[1]. Voltar')