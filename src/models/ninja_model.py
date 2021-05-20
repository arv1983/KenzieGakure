from src.models.jutsu_model import Jutsu

class Ninja:
    def __init__(self, name, clan, village, ninja_level='Unranked'):
        self.name = name
        self.clan = clan
        self.village = village
        self.ninja_level = ninja_level
        self.jutsu_list = []
        self.health_pool = 100
        self.chakra_pool = 100
        self.concious = True
    
    def learn_jutsu(self, jutsu):
        print(jutsu.__dict__)
        self.jutsu_list.append(jutsu)
        return f'O ninja {self.name} {self.clan} acabou de aprender um novo jutsu: {jutsu.jutsu_name}'

    @staticmethod
    def check_health(ninja_to_check):
        if ninja_to_check.health_pool < 0:
            ninja_to_check.health_pool = 0
            ninja_to_check.concious = False
        return ninja_to_check.concious

    def cast_jutsu(self, jutsu, adversary):
        if not adversary.concious:
            return False
        for name in self.jutsu_list:
            if (name.jutsu_name == jutsu.jutsu_name) and (jutsu.chakra_spend <= self.chakra_pool): 
                adversary.health_pool -= jutsu.jutsu_damage
                self.chakra_pool -= jutsu.chakra_spend
                return True
        return False

            



