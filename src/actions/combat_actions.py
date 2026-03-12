def combat_attack(forward, receiver):
    if (forward > receiver['life']):
        receiver['life'] = 0
        return receiver['life']
    
    receiver['life'] -= forward
    return receiver['life']
