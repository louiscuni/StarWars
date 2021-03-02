import json

###MATHS###
def proba_of_wining (k):
    #return a probability (0-1) based on a Math formula
    res = 0
    if k < 1000:
        for i in range(k):
            res += pow(9, i)/pow(10, i + 1)
        return 1 - res
    else:
        return 0

###DIVERS###
def check_fuel(action, old_state):
    #check if there is enough fuel for an action
    if old_state["fuel"] - action[1] >= 0:
        return True
    else:
        return False

def read_file(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data


def safest(list_p):
    #return the safest path from list
    res = list_p[0]
    for p in list_p:
        if res['danger'] > p['danger']:
            res = p
    return res

def tabOfTuple_to_tab(tab):
    #transform tuple array to array
    res = []
    for i in tab:
        res.append(i[0])
    return res

def tab_to_dico(tab):
    #transforme array to a dico of dico indexed on array element 
    res = {}
    for i in tab:
        res[i] = {}
    return res

###PARETO POINT###
#pareto front multi objectif concept, it represent the set of point that are dominant, eg no points are better than them

def build_pareto(list_p):
    #return a list of possibiliies that are pareto dominant
    res = [list_p[0]]
    for p in list_p:
        if on_pareto(res, p):
            res =update_pareto(res, p)
    return res

def on_pareto(list_p, p):
    #return true if p is on pareto front of list_p
    for i in list_p :
        if i['danger'] <= p['danger'] and i['fuel'] >= p['fuel']:
            return False
    return True

def update_pareto(list_p, possibility):
    #update pareto list point with a new point
    res = [possibility]
    for p in list_p:
        if p['danger'] < possibility['danger'] or p['fuel'] > possibility['fuel']:
            res.append(p)
    return res

