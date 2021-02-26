from src.ressource.utils import *
from src.ressource.computer import *
from pathlib import Path


vaisseau = read_file('default_file/millenium-falcon.json')

def main(empire, vaisseau=vaisseau):
    rob = falco_M_computer(vaisseau, empire)
    rob.build_dico()
    res = rob.get_min_rencontre()
    res = proba_of_wining(res)
    return res*100
