import numpy as np

def adjust(traits,traits_values,identity):
    for i in range(len(traits)):
        if(traits[i]): traits[i] = traits_values[i]
        else: traits[i] = identity
    return traits

def BINRULES(rules):
    def RULES(ts, traits_values):
        res = rules[:]
        for t in ts:
            res = res[t]
        return res
    return RULES

# all functions stores with keys
functions = {
    'PROD': lambda ts, traits_values: np.prod(adjust(ts[:],traits_values,1)), # 1 is mult id
    'SUM': lambda ts, traits_values: sum(adjust(ts[:],traits_values,0)), # 0 is add id
    'BINRULES': BINRULES
}