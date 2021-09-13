import numpy as np
import sys
from mcStep import *
from damagePlot import *
from Ability import Ability
from SelfParam import SelfParam
from TargetParam import TargetParam

# EXPECTED COMMAND LINE USAGE:
# $ python main.py [args in an order that i will determine later]

def main(args):
    # unpack args
    n, it = args[0:1]

    # instantiate player and target, then calculate the hit chance and ability damage
    # instantiate abilities
    # start with n length sequence of all wrack/piercing shot/slice
    startSequence = []
    if (player.weaponStyle == "magic"):
        startSequence = [wrack] * n
    elif (player.weaponStyle == "ranged"):
        startSequence = [piercingShot] * n
    elif (player.weaponStyle == "melee"):
        startSequence = [_slice] * n

    # run MCMC for specified iterations and store damage for each iteration
    nextSequence = startSequence
    damageList = np.empty(it, dtype=int)
    for j in range(it)
        nextSequence, damageList[j] = mcStep(n, nextSequence, player, target, abilities, hitChance, abilityDmg)
        # how am I going to define abilities array in a nice pythonic way?
    
    # plot damage over each iteration and return final sequence
    damagePlot(n, it, damageList)

if __name__ == '__main__':
    args = sys.argv
    main(args)