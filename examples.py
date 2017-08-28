import numpy as np
from traitsgenealogy import Genealogy
import fitnessfunctions as ff
import inspector

def basicProduct():
    gen = Genealogy(
        50, # how many iterations :: int
        100, # number of members in each generation
        3, # parents each member has :: int
        [2,3], # how much each trait is worth :: [float]
        ff.functions['PROD'], # how to combine traits into fitness :: [bool] -> float
        [0,50,50,0] # relative abundancy of traits in gen0 :: [bool]
    )
    inspector.plot(gen)

def basicRules():
    gen = Genealogy(
        50, # how many iterations :: int
        100, # number of members in each generation
        2, # parents each member has :: int
        [1,1], # how much each trait is worth :: [float]
        ff.functions['BINRULES']([[0,1],[2,3]]), # how to combine traits into fitness :: [bool] -> float
        [25,25,25,25] # relative abundancy of traits in gen0 :: [bool]
    )
    inspector.plot(gen)

def custom(args):
    length, size, parents, traits_function, initial_distribution = args[0], args[1], args[2], args[3], args[4], args[5]
    if(len(args) == 7): title = args[6]
    else: title = "All Trait Combinations"
    tf = fitnessfunctions.functions[traits_function.upper()] # get by key
    init_dist = initial_distribution.split(',') # write in terminal as "1,2,3,4..."
    gen = Genealogy(length,size,parents,traits,tf,init_dist)
    inspector.plot(gen,title)

examples = {
    "BASIC_PRODUCT": basicProduct,
    "BASIC_RULES": basicRules   
}