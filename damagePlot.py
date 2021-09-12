import numpy as np
import matplotlib.pyplot as plt

def damagePlot(n, it, damageList):
    # inputs: int length of sequence, int # of iterations, np.array of damage from each MC iteration

    t = "damage over full run ("+ n + " tick sequence)"
    plt.plot(np.arange(0,it), damageList, '.-', color="red")
    plt.xlabel("iteration #")
    plt.ylabel("calculated damage")
    plt.title(t)
