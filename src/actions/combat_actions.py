def combat_attack(forward, receiver, Game):
    if (forward > receiver['life']):
        receiver['life'] = 0
        Game.change_state(1)
        return receiver['life']
    
    receiver['life'] -= forward
    return receiver['life']
