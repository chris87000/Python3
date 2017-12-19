import time
from datetime import datetime, timedelta



# on obtient l'heure courante sous la forme d'un flottant
# qui représente le nombre de secondes depuis le 1er Janvier 1970
t_now = time.time()
print(t_now)
t_later = t_now + 3 * 3600
type(t_later)
struct_later = time.gmtime(t_later)
print(struct_later)

print(f'heure UTC dans trois heures {time.strftime("%Y-%m-%d at %H:%M", struct_later)}')

dt_now = datetime.now()
dt_later = dt_now + timedelta(hours=3)
# on peut imprimer simplement un objet date_time
print(f'maintenant {dt_now}')

# et si on veut un autre format, on peut toujours appeler strftime
print(f'dans trois heures {dt_later.strftime("%Y-%m-%d at %H:%M")}')
# mais ce n'est même pas nécessaire, on peut passer le format directement
print(f'dans trois heures {dt_later:%Y-%m-%d at %H:%M}')

class Bateau:
    def __init__(self, id, name, country):
        self.id = id
        self.name = name
        self.country = country
        
bateau2 = Bateau(1000, "Toccata", "FRA")

print(vars(bateau2))


class Bateau:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], dict):
            self.__dict__ = args[0]
        elif len(args) == 3:
            id, name, country = args
            self.id = id
            self.name = name
            self.country = country

bateau3 = Bateau({'id': 1000, 'name': 'Leon', 'country': 'France'})
bateau4 = Bateau(1001, 'Maluba', 'SUI' )

print(vars(bateau3))
print(vars(bateau4))

