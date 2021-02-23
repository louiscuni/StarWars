import json

def proba_of_wining (k):
    res = 0
    if k < 1000:
        for i in range(k):
            res += pow(9, i)/pow(10, i + 1)
        return 1 - res
    else:
        return 0

def check_fuel(action, old_state):
    if old_state["fuel"] - action[1] >= 0:
        return True
    else:
        return False

def read_file(path):
    with open(path) as json_file:
        data = json.load(json_file)
    return data

def safest(list_p):
    res = list_p[0]
    for p in list_p:
        if res['danger'] > p['danger']:
            res = p
    return res

def build_pareto(list_p):
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
    res = [possibility]
    for p in list_p:
        if p['danger'] < possibility['danger'] or p['fuel'] > possibility['fuel']:
            res.append(p)
    return res


l = [{'danger' : 4, 'fuel' : 1}, {'danger' : 1, 'fuel' : 2}, {'danger' : 7, 'fuel' : 4}, {'danger' : 3, 'fuel' : 5}, {'danger' : 5, 'fuel' : 7} ]
print(build_pareto(l))