import numpy as np
from calcDmg import *
from calcSequenceDamage import *
from generateSequence import *
from Ability import Ability
from SelfParam import SelfParam
from TargetParam import TargetParam

def mcStep(n, current, player, target, hitChance, abilityDmg):
    # calculate the damage of the current sequence
    currentDmg = calcSequenceDamage(current, player, target, hitChance, abilityDmg)

    # generate a new sequence of abilities of length n and get its damage
    new = generateSequence(n, player, target)
    newDmg = calcSequenceDamage(new, player, target, hitChance, abilityDmg)

    # determine whether to keep or reject new sequence
    u = np.random.rand()
    r = currentDmg/newDmg # >1 means current is better, =1 means equivalent, <1 means new is better
    if (u < r):
        return new # accept
    else: 
        return current # reject and keep current