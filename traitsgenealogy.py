import numpy as np
import random
random.seed()
#\\
#+\\
"""\\
]]=//|//=]]=//|//=\]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=
                   \///
Traits genealogy   /+/
                  ///
]]=//|//=]]=//|==//]

This version of genealogy will simply be tracking traits (with no effect of the age and popular factors.)

Important objects:
- Generation :: [int] where the index is the index of the binary form of the trait combination


]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//=]]=//|//="""

class Genealogy:
    def __init__(self,
        length, # how many iterations :: int
        size, # number of members in each generation
        parents, # parents each member has :: int
        traits, # how much each trait is worth :: [float]
        traits_function, # how to combine traits into fitness :: [bool] -> float
        initial_distribution # relative abundancy of traits in gen0 :: [int]
    ):
        # initializations
        self.length = length
        self.size = size
        self.traits = traits
        self.parents = parents
        self.traits_function = traits_function
        self.initial_distribution = initial_distribution
        
        self.traits_expansion = 2**len(traits)
        self.tlen = len(traits)
        self.generations = []
        self.distributions = []
        self.blank_generation = [ 0 for i in range(self.traits_expansion) ]
        self.fitnesses = [
            self.traits_function(ind_to_bin(i,self.tlen),self.traits)
                for i in range(self.traits_expansion) ]
        self.current_generation = -1

        # fill generation 0
        gen0 = self.new_generation()
        for i in range(self.traits_expansion):
            gen0[i] += initial_distribution[i]
        # kick off the distributions history
        self.distributions.append(self.normalize(initial_distribution))

        # filling subsequent generations
        for i in range(self.length):
            self.fill_next_generation()

    
    def new_generation(self):
        self.generations.append(self.blank_generation[:])
        self.current_generation += 1
        return self.get_current_generation()

    
    def get_current_generation(self):
        return self.generations[self.current_generation]

    
    def get_absolute_distribution(self):
        distribution = self.blank_generation[:]
        for gi in range(0,self.current_generation):
            for ti in range(self.traits_expansion):
                distribution[ti] += self.generations[gi][ti]
        return distribution

    
    def fill_next_generation(self):
        gen = self.new_generation()
        # distribution of entire population
        distribution = self.get_absolute_distribution()
        # add to history of distributions
        self.distributions.append(self.normalize(distribution))
        # distribution * fitnesses (normalized)
        fits = self.normalize([ self.fitnesses[i] * distribution[i] for i in range(self.traits_expansion) ])
        # fitnesses per member (for non-replacement calculation)
        fits_rate = self.rate(fits,distribution)
        # create new members
        for m in range(self.size): # for each member in the new generation
            parents = []
            for p in range(self.parents):
                # this is selection without replacement
                parent_choice = np.random.choice(np.arange(self.traits_expansion), p=fits)
                parents.append(parent_choice)
                # subtract the fitness of the chosen parent, since can't choose that parent again
                prev = fits[parent_choice]
                fits[parent_choice] -= fits_rate[parent_choice]
                # re-normalize after removing a member
                fits = self.normalize(fits)
                fits_rate = self.rate(fits,distribution)
            # inheret_traits translates parents trait indecies to [bool]
            self.add_member(self.inheret_traits(parents))


    # chooses traits from parents=[int], and produces [bool]
    def inheret_traits(self,parents):
        traits_pool = [ 0 for i in range(len(self.traits))]
        for i in range(len(parents)):
            bin_arr = ind_to_bin(parents[i],self.tlen) # len(bin_arr) == len(self.traits)
            # add 1 to appropriate slot in trait pool if has trait
            for j in range(len(bin_arr)):
                if bin_arr[j]: traits_pool[j] += 1
        # for each trait, choose to inherit or not
        choices = []
        for i in range(len(self.traits)):
            # normalized chances of getting and not getting trait
            pro_trait = traits_pool[i] / len(parents); # print("pro:",pro_trait)
            con_trait = (len(parents) - (pro_trait * len(parents)) ) / len(parents); # print("con:",con_trait)
            # assign trait
            choices.append(np.random.choice([0,1], p=[con_trait,pro_trait]))
        return choices

    
    def add_member(self,traits):
        bin_ind = bin_to_ind(traits)
        self.get_current_generation()[bin_ind] += 1

    
    def normalize(self,dist):
        total = sum(dist)
        return [i/total for i in dist]


    def rate(self,fits,dist):
        res = []
        for i in range(self.traits_expansion):
            if(dist[i] != 0):
                res.append(fits[i]/dist[i])
            else:
                res.append(0)
        return res



##################
### UTILITIES
##################

# ind in binary order -> [bool] representation binary
def ind_to_bin(x,tlen):
    n = to_bin(x)
    res = [int(i) for i in list(str(n))]
    while(len(res) < tlen):
        res = [0] + res
    return res


def to_bin(x):
    return int(bin(x)[2:])


# [bool] -> int, representing index in binary order
def bin_to_ind(l):
    total = 0
    for i in range(len(l)):
        total += (2**i) * int(l[i])
    return total