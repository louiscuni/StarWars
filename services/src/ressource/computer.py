import json
import sqlite3 as sql
from src.database.universe_requetor import *
from src.ressource.utils import *
from pathlib import Path
import networkx as nx


class falco_M_computer:

    def __init__(self, vaisseau_data, empire_data ):
        self.vaisseau_data = vaisseau_data
        self.empire_data = empire_data
        db_path = Path.cwd()
        db_path = db_path.parent.parent / 'database' 
        self.requetor = universe_requetor(db_path / vaisseau_data['routes_db'])
        self.dico = {}


    def init_dico(self):
        #initialize dico
        planets = self.requetor.get_all_planets()
        self.dico = tab_to_dico(planets)
        paths = self.shortest_paths(planets)
        
        for p in planets:
            self.dico[p]['end_day'] = self.empire_data['countdown'] - paths[p] 
        
        self.dico[self.vaisseau_data['departure']][0] = [{"fuel": self.vaisseau_data['autonomy'], "danger": 0, 'last_planet': [(self.vaisseau_data['departure'], 0)] }]    


    def build_dico(self):
        #build dico that represent all possible actions in the universe (the database)
        self.init_dico()

        for day in range(self.empire_data['countdown'] + 1):#iteration on days
            for planet in self.dico.keys():#iteration on planet
                if day <= self.dico[planet]['end_day']:#check if planet is still useable
                    if planet != self.vaisseau_data['arrival']:#doesnt need to update arrival planet
                        actions = self.requetor.get_possible_action(planet)
                        if day in self.dico[planet].keys():#check if it exist any possibility to be on this planet on this day
                            possibilities = build_pareto(self.dico[planet][day])
                            self.dico[planet][day] = possibilities

                            for p in possibilities:#iteration on possibilities
                                self.update_dico( actions, p, [day, planet] )
                    else:
                        if day in self.dico[planet].keys():
                            possibility = safest(self.dico[planet][day])
                            self.dico[planet][day] = possibility
        return self.dico


    def update_dico(self, actions, old_state, current_info):
    #update dico with the possible actions in days
    #action = (planet, dist)
        planet = current_info[1]
        day = current_info[0]
        for a in actions:
            if a[0] == 'refuel':
                new_state = { "fuel" : self.vaisseau_data['autonomy'], "danger" : old_state["danger"] + self.danger(planet, day + 1), "last_planet" : old_state['last_planet'] + [(planet, day +1)] }
                if day + 1 in self.dico[planet].keys():
                    self.dico[planet][day + 1].append( new_state ) 
                else:
                    self.dico[planet][day + 1] =  [new_state]
            else:
                if check_fuel(a, old_state) and self.check_countdown(a, day):#check if action is possible and if it will end in time
                    new_state = { 'fuel' : old_state['fuel'] - a[1], "danger" : old_state["danger"] + self.danger(a[0], day + a[1]), "last_planet" : old_state['last_planet'] + [(a[0], day + a[1])]}
                    if day + a[1] in self.dico[a[0]].keys():
                        self.dico[a[0]][day + a[1]].append( new_state ) 
                    else : 
                        self.dico[a[0]][day + a[1]] = [new_state]


    def shortest_paths(self, list_planet):
        #return a dico of shortest path to arrival
        G = nx.Graph()

        edges = self.requetor.get_edges()
        true_edges= []
        for e in edges:
            true_edges.append( (e[0], e[1], {'weight': e[2]}) )

        G.add_nodes_from(list_planet)
        G.add_edges_from(true_edges)

        return nx.single_source_dijkstra_path_length(G, self.vaisseau_data['arrival'])


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
        #print(endor)
        for day in endor.keys():
            if day != 'end_day':
                if endor[day]['danger'] < min_r:
                    min_r = endor[day]['danger']
                # if endor[day]['danger'] == 0:
                #     print(day, endor[day])
        return min_r
