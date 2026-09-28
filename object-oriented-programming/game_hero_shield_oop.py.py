class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    def take_damage(self, damage):
        self.__hp -= damage
        print(f"{self.name} took {damage} damage! Remaining HP: {self.__hp}")


class ShieldHero(Hero):
    def take_damage(self, damage):
        reduced_damage = damage // 2
        
        current_hp = self.get_hp()
        
        print(f"{self.name} blocked the attack with a Shield!")
        
        super().take_damage(reduced_damage)


hero1 = Hero("Warrior", 100)
hero1.take_damage(30)

print("-----")

hero2 = ShieldHero("Paladin", 100)
hero2.take_damage(30)



    