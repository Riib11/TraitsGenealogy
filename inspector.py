import numpy as np
import matplotlib.pyplot as plt

def plotAllDistributions(gen):
    dist_histories = [[] for i in range(gen.traits_expansion)]
    for time_step in gen.distributions:
        for i in range(gen.traits_expansion):
            dist_histories[i].append(time_step[i])

    for dh in dist_histories:
        plt.plot(np.arange(0,gen.length),dh[1:])

def plotTargetDistribution(gen,ind):
    dist_histories = [[] for i in range(gen.traits_expansion)]
    for time_step in gen.distributions:
        for i in range(gen.traits_expansion):
            dist_histories[i].append(time_step[i])

    dh = dist_histories[ind]
    plt.plot(np.arange(0,gen.length),dh[1:])

def show():
    plt.show()