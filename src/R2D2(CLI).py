from utils import *
from falcon_millenium_computer_back import *
from pathlib import Path


vaisseau = read_file('millenium-falcon.json')
path = Path.cwd()
path = path.parent / 'test'

tests = ['at_least_one_danger.json', 'no_danger.json', 'big_test1.json']


for t in tests:
    empire = read_file(path / t)
    rob = falco_M_computer(vaisseau, empire)
    print(t)
    rob.build_dico()
    #print(rob.dico)
    res = rob.get_min_rencontre()
    if res == rob.empire_data['res']:
        print('*** Succes ! ***')
    else:
        print('*** FAIL ! ***')
    print('res trouve : ', res)
    print('attente : ', rob.empire_data['res'])