from src.ressource.utils import *
from src.ressource.computer import *
from pathlib import Path

#python script for tests


vaisseau = read_file('vaisseau/vaisseau00.json')

tests = ['at_least_one_danger.json', 'no_danger.json', 'roll_back.json', 'big_test1.json']#test name

for t in tests:
    empire = read_file('empire/' + t)
    rob = falco_M_computer(vaisseau, empire)
    print(t)
    rob.build_dico()
    res = rob.get_min_rencontre()
    if res == rob.empire_data['res']:
        print('*** Succes ! ***')
    else:
        print('*** FAIL ! ***')
    print('res trouve : ', res)
    print('attente : ', rob.empire_data['res'])