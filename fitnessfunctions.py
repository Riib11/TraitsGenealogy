import numpy as np

def adjust(traits,traits_values,identity):
    for i in range(len(traits)):
        if(traits[i]): traits[i] = traits_values[i]
        else: traits[i] = identity
    return traits

def PROD(ts,traits_values):
    traits = adjust(ts[:],traits_values,1) # 1 is mult id
    print(traits,np.prod(traits))
    return np.prod(traits)

def SUM(ts,traits_values):
    traits = adjust(ts[:],traits_values,0) # 0 is add id
    return sum(traits)