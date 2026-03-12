from random import randrange

class Player:
    def __init__(self, name):
        self.name = name
        self.life = (randrange(1, 12) * 4)
        self.mana = (randrange(1, 12) * 2)
        self.power = (randrange(1, 12) * 3)
        self.intelect = (randrange(1, 12) * 1)

    def create(self):
        return {
            "name": self.name,
            "life": self.life,
            "mana": self.mana,
            "power": self.power,
            "intelect": self.intelect,
            "inventory": [

            ]
        }

def create_player(name):
    player = Player(name)
    return player.create()