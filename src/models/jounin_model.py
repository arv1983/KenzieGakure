from src.models.ninja_model import Ninja


class Jounin(Ninja):
    def __init__(self, name, clan, village, proficiency, ninja_level='Unranked'):
        
        super().__init__(name, clan, village)
        self.ninja_level = ninja_level
        self.name = name
        self.clan = clan
        self.village = village
        self.proficiency = proficiency
        self.is_in_mission = False
        
    def list_best_proficiency(self):
        return f'{self.name} demonstra maior proficiência em {max(self.proficiency, key=self.proficiency.get)}'

    def start_mission(self):
        if not self.is_in_mission:
            self.is_in_mission = True
            return f'O ninja {self.name} {self.clan} saiu em missão'
        return f'O ninja {self.name} {self.clan} já está em uma missão'

    def return_from_mission(self):
        if self.is_in_mission:
            self.is_in_mission = False
            return f'O ninja {self.name} {self.clan} retornou em segurança da missão'
        return f'O ninja {self.name} {self.clan} não está em nenhuma missão no momento'
