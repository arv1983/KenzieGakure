from src.models.jutsu_model import Jutsu
from src.models.ninja_model import Ninja
from src.models.jounin_model import Jounin



modelo = Jutsu('Rasengan', 'Vento', 'a', 20, -15)

naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')

rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)


res = naruto.learn_jutsu(rasengan)

# print(res)

# print(naruto.__dict__)

kakashi_proficiency = {'taijutsu': 7, 'ninjutsu': 8, 'genjutsu': 4}
kakashi = Jounin('Kakashi', 'Hatake', 'Konoha', kakashi_proficiency)
result = kakashi.list_best_proficiency()
#                 nome       familia  cidade

print('resultado abaixo')
print(result)
resaa = kakashi.return_from_mission()
rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
print(resaa)
sasuke = Ninja('Sasuke', 'Uchiha', 'Konoha')
teste = Ninja.check_health(kakashi)
print('teste')
print(teste)


res = naruto.cast_jutsu(rasengan, sasuke)
print(res)