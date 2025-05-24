import random

class ZombieDiceBot:
    def _init_(self, name):
        self.name = name
        self.score = 0

    def turn(self):
        brains = 0
        shotgun = 0
        feet = 0
        rolls = 0
        while rolls < 3:
            roll = random.choice(['brain', 'shotgun', 'foot'])
            if roll == 'brain':
                brains += 1
            elif roll == 'shotgun':
                shotgun += 1
            else:
                feet += 1
            rolls += 1
            if shotgun >= 3:
                break
        self.score += brains
        return brains, shotgun, feet

def simulate_game(bots):
    while True:
        for bot in bots:
            brains, shotgun, feet = bot.turn()
            print(f"{bot.name} got {brains} brains, {shotgun} shotguns, and {feet} feet.")
            if bot.score >= 13:
                print(f"{bot.name} wins!")
                return

def main():
    bots = [ZombieDiceBot("Zombie1"), ZombieDiceBot("Zombie2"), ZombieDiceBot("Zombie3")]
    simulate_game(bots)

if _name_ == "_main_":
    main()
