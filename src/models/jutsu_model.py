class Jutsu:
    def __init__(self, jutsu_name, jutsu_type, jutsu_level, jutsu_damage, chakra_spend):
        self.jutsu_name = jutsu_name
        self.jutsu_type = jutsu_type
        self.jutsu_level = jutsu_level.upper()
        self.jutsu_damage = jutsu_damage
        if chakra_spend <= 0:
            chakra_spend = 100
        self.chakra_spend = chakra_spend

