import numpy as np
from Ability import Ability
from SelfParam import SelfParam
from TargetParam import TargetParam

def generateSequence(n, abilities, player, target):
    # inputs: int n, array of Ability abilities, SelfParam player, TargetParam target
    # returns n length array of validated abilities

    adren = 100 # asssumes start at 100% adrenaline
    sequence = [None] * n

    # pick a new ability to add and validate it, until the array has length n
    i = 0
    while (i < n):
        r = np.random.randInt(0,len(abilities)-1)
        candidate = abilities[r]
        
        # check if ability is right style, player has enough adrenaline, and ability is not on cooldown
        recentlyUsed = sequence[(max(0,i-candidate.cooldown()):i] # get all the ticks since the last cooldown, not going backwards in the array
        if ((candidate.style() == player.weaponStyle()) and (candidate.adrenReq() < adren) and (candidate.name() not in recentlyUsed)):
            sequence[i] = candidate
            i += candidate.duration() # move the pointer forward the amount of ticks it takes to cast the ability successfully
            adren += candidate.adrenChange()