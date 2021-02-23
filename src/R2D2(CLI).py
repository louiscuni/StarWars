import sqlite3 as sql
from universe_requetor import *
from utils import *
from pathlib import Path
from falcon_millenium_computer_back import *


class R2D2:

    def __init__(self, vaisseau_data, empire_data ):
        self.vaisseau_data = vaisseau_data
        self.empire_data = empire_data
        db_path = Path.cwd()
        db_path = db_path.parent / 'database' 
        self.requetor = universe_requetor(db_path / vaisseau_data['routes_db'])
        self.dico = {}

    def build_dico(self):
    #build dico that represent all possible actions in the universe (the database)
        self.dico = {'Tatooine':{},
                'Dagobah' : {},
                'Hoth': {},
                'Endor': {}}#a modifier
        self.dico[self.vaisseau_data['departure']][0] = [{"fuel": 6, "danger": 0}]

        for day in range(empire['countdown']):
            for planet in self.dico.keys():
                actions = self.requetor.get_possible_action(planet)
                if day in self.dico[planet].keys():
                    for possibility in self.dico[planet][day]:
                        self.update_dico( actions, possibility, [day, planet] )
        return self.dico

    def update_dico(self, actions, old_state, current_info):
    #update dico with the possible actions in days
        #action = (planet, dist)
        planet = current_info[1]
        day = current_info[0]
        for a in actions:
            if a[0] == 'refuel':
                new_state = { "fuel" : 6, "danger" : old_state["danger"] + self.danger(planet, day) }
                if day + 1 in self.dico[planet].keys():
                    self.dico[planet][day + 1].append( new_state ) 
                else:
                    self.dico[planet][day + 1] =  [new_state]
            else:
                if check_fuel(a, old_state) and self.check_countdown(a, day):#check if action is possible and if it will end in time
                    new_state = { 'fuel' : old_state['fuel'] - a[1], "danger" : old_state["danger"] + self.danger(planet, day)}
                    if day + a[1] in self.dico[a[0]].keys():
                        self.dico[a[0]][day + a[1]].append( new_state ) 
                    else : 
                        self.dico[a[0]][day + a[1]] = [new_state]

    def danger(self, planet, day):
        #check if a body hunter is on planet on day
        for danger in self.empire_data["bounty_hunters"]:
            if danger['planet'] == planet and danger['day'] == day:
                return 1
        return 0

    def check_countdown(self, action, day):
        #check if an action will end before final countdown
        if day + action[1] > self.empire_data["countdown"]:
            return False
        else:
            return True

    def get_min_rencontre(self):
        endor = self.dico['Endor']
        min_r = 42000#pas ouf
        for day in endor:
            for p in endor[day]:
                if p['danger'] < min_r:
                    min_r = p['danger']
        return min_r




# vaisseau = {
#   "autonomy": 6,
#   "departure": "Tatooine",
#   "arrival": "Endor",
#   "routes_db": "universe.db"
# }

# empire = {
#   "countdown": 9, 
#   "bounty_hunters": [
#     {"planet": "Hoth", "day": 6 }, 
#     {"planet": "Hoth", "day": 7 },
#     {"planet": "Hoth", "day": 8 }
#   ]
# }

vaisseau = read_file('millenium-falcon.json')
empire = read_file('empire.json')

print(empire["countdown"])

droid = R2D2(vaisseau, empire)
droid.build_dico()
print(droid.dico)
m = droid.get_min_rencontre()
print(proba_of_wining(m))