import numpy as np
from calcDmg import *
from calcSequenceDamage import *
from generateSequence import *
from Ability import Ability
from SelfParam import SelfParam
from TargetParam import TargetParam

def mcStep(n, current, player, target, abilities, hitChance, abilityDmg):
    # calculate the damage of the current sequence
    currentDmg = calcSequenceDamage(current, player, target, hitChance, abilityDmg)

    # generate a new sequence of abilities of length n and get its damage
    new = generateSequence(n, abilities, player, target)
    newDmg = calcSequenceDamage(new, player, target, hitChance, abilityDmg)

    # determine whether to keep or reject new sequence
    u = np.random.rand()
    r = currentDmg/newDmg # >1 means current is better, =1 means equivalent, <1 means new is better
    if (u < r):
        return new, newDmg # accept
    else: 
        return current, currentDmg # reject and keep current

def mcLoop(n, it, startSequence, player, target, abilities, hitChance, abilityDmg)
    current = startSequence
    damageList = np.empty(it, dtype=int)
    for j in range(it)
        current, damageList[j] = mcStep(n, current, player, target, abilities, hitChance, abilityDmg)

    return damageList, current