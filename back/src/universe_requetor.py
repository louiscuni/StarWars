import sqlite3 as sql
from utils import *

class universe_requetor:
    table = ['routes']
    routes_columns = ['ORIGIN', 'DESTINATION', 'TRAVEL_TIME']


    def __init__(self, path_db):
        self.path_db = path_db
        self.connection = sql.connect(path_db)
        self.cursor = self.connection.cursor()

    def printDB(self):
        with self.connection:
            self.cursor.execute("SELECT * FROM routes")
            print(self.cursor.fetchall())

    def get_possible_action(self, planet):
        #return a list of possible action [(destination, time_it_take)]
        planet_acces = []
        with self.connection:
            self.cursor.execute("SELECT DESTINATION, TRAVEL_TIME FROM routes WHERE ORIGIN=(:ORIGIN)", {'ORIGIN' : planet} )
            planet_acces += self.cursor.fetchall()
            self.cursor.execute("SELECT ORIGIN, TRAVEL_TIME FROM routes WHERE DESTINATION=(:DESTINATION)", {'DESTINATION' : planet} )
            planet_acces += self.cursor.fetchall()
        planet_acces += [('refuel', 1)]
        return planet_acces

    def get_all_planets(self):
        #return a list of every planet in the db
        res = []
        with self.connection:
            self.cursor.execute("""SELECT DESTINATION FROM routes
                             UNION 
                             SELECT ORIGIN FROM routes""" )
            res += self.cursor.fetchall()
        res = tabOfTuple_to_tab(res)
        return res

    def get_edges(self):
        edges = []
        with self.connection:
            self.cursor.execute("SELECT * FROM routes")
            edges += self.cursor.fetchall()
        return edges

    def db_ok():
        #check if db is good
        return 0