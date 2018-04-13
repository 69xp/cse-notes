import random


class Character(object):
    def __init__(self, name, description, health, items, atk, defense):
        self.name = name
        self.description = description
        self.health = health
        self.inventory = items
        self.dmg = atk
        self.defense = defense
        self.death = False

    def attack(self, opponent):
        attack = random.randint(1, 3)
        damage = random.randint(0, self.dmg)
        if attack == 1:
            print('%s hits %s!' % (self.name, opponent.name))
            opponent.health -= damage
        if attack == 2:
            print('%s missed %s!' % (self.name, opponent.name))

        if attack == 3:
            print('%s hits %s!' % (opponent.name, self.name))
            self.health -= damage

    def take_damage(self):
        self.health -= 1

    def death(self):
        if self.take_damage >= self.health:
            if self.health == 0:
                self.death = True
                print('%s is dead...' % self.name)


HERO = Character('Randomly Generic Name', 'A blank slate', 6, ['butter knife'], 3, 3)
Ogre = Character('Yo-Ogre-Urt', 'like a cyclops only with two eyes.', 5, ['bone club'], 4, 2)
Skeleton1 = Character('Skelton B. Bones', 'A half-petrified skeleton, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Skeleton2 = Character('Skelton C. Bones', 'A skeleton with armor, creaking along slowly', 1,
                      ['Stone Rapier', "Iron Helm", 'Stone Boots', 'Rusty Light Armor', 'Iron Chausses'], 1, 1)
Skeleton3 = Character('Skelton D. Bones', 'A skeleton with one arm, creaking along slowly', 1, ['Stone Rapier'], 1, 1)
Necromancer = Character('Lebn Fundi Toyte', '', 8, ["Stygian Bone Steel Longsword"], 3, 4)
Dragon = Character('Bone Dragon', "A dragon made out of bones", 30, [''], 12, 18)
