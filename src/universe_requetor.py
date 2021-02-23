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
        #print('destination possibles depuis ', planet)
        planet_acces = []
        with self.connection:
            self.cursor.execute("SELECT DESTINATION, TRAVEL_TIME FROM routes WHERE ORIGIN=(:ORIGIN)", {'ORIGIN' : planet} )
            planet_acces += self.cursor.fetchall()
            self.cursor.execute("SELECT ORIGIN, TRAVEL_TIME FROM routes WHERE DESTINATION=(:DESTINATION)", {'DESTINATION' : planet} )
            planet_acces += self.cursor.fetchall()
        #planet_acces = get_destinations(planet_acces, planet)
        planet_acces += [('refuel', 0)]
        #print(planet_acces)
        return planet_acces

    def db_ok():
        #check if db is good
        return 0