import sys
from src.ressource.computer import *
from src.ressource.utils import *

#fichier pour CLI

def main():
    vaisseau = sys.argv[1]
    empire = sys.argv[2]
    vaisseau = read_file(vaisseau)
    empire = read_file(empire)
    rob = falco_M_computer(vaisseau, empire)
    rob.build_dico()
    res = rob.get_min_rencontre()
    res = proba_of_wining(res)
    print(res*100, '%')
    


if __name__ == '__main__':
    main()