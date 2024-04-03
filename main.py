class Weapon:
    def attack(self):
        pass

    def weapon_name(self):
        pass

class Sword(Weapon):
    def attack(self):
        return 'Боец наносит удар мечом.'

    # def weapon_name(self):
    #     return 'меч'

class Bow(Weapon):
    def attack(self):
        return 'Боец наносит удар из лука.'

    def weapon_name(self):
        return 'лук'

class Fighter:
    def __init__(self):
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon
        print(f'Боец выбирает {self.weapon.weapon_name()}.')

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())

class Monster:
    pass

# Game starts
fighter = Fighter()
monster = Monster()

# fighter picks up a sword
sword = Sword()
fighter.changeWeapon(sword)

# check the attack method
fighter.attack()
print('Монстр побежден!n')

# fighter switches to bow
bow = Bow()
fighter.changeWeapon(bow)

# check the attack method
fighter.attack()
print('Монстр побежден!')