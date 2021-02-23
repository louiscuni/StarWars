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