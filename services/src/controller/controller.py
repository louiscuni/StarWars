from src.ressource.utils import *
from src.ressource.computer import *
from pathlib import Path

#file called by run.py

path = Path.cwd()#= ~/dataiku
vaisseau = read_file(path / 'services/src/default_file/millenium-falcon.json')

def main(empire, vaisseau=vaisseau):
    rob = falco_M_computer(vaisseau, empire)
    rob.build_dico()
    res = rob.get_min_rencontre()
    res = proba_of_wining(res)
    path = rob.get_best_path()
    return res*100, path
