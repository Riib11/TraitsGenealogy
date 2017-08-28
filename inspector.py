import numpy as np
import matplotlib.pyplot as plt

def plot(gen,title="All Trait Combinations",target=None):
    if(target): plotTargetDistribution(gen,0)
    else: plotAllDistributions(gen)
    plt.title(title)
    show()

def plotAllDistributions(gen):
    dist_histories = [[] for i in range(gen.traits_expansion)]
    for time_step in gen.distributions:
        for i in range(gen.traits_expansion):
            dist_histories[i].append(time_step[i])

    for i in range(len(dist_histories)):
        plt.plot(
            np.arange(0,gen.length),dist_histories[i][1:],
            label=str( ind_to_bin(i,len(gen.traits)) ) + " : " + str(gen.fitnesses[i]))
    plt.legend()

def plotTargetDistribution(gen,ind):
    dist_histories = [[] for i in range(gen.traits_expansion)]
    for time_step in gen.distributions:
        for i in range(gen.traits_expansion):
            dist_histories[i].append(time_step[i])

    dh = dist_histories[ind]
    plt.plot(np.arange(0,gen.length),dh[1:])
    plt.title("Targetting " + str(bin_to_ind(ind,len(gen.traits))))

def createLegend(traits_expansion):
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)

def show():
    plt.show()



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