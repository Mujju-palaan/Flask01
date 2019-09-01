lottery_player_dict = {
    'name': 'Mujju',
    'numbers': (5,9,12,3,1,21)
}

class lottery_player:
    def __init__(self):
        self.name = "Mujju"
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)

player = lottery_player()
print(player.name)
print(player.numbers)

print(player.total())