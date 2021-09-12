import numpy as np
from calcDmg import *
from Ability import Ability
from SelfParam import SelfParam
from TargetParam import TargetParam

def calcSequenceDamage(sequence, player, target, hitChance, abilityDmg):
    # input: array of Ability (length n), SelfParam player, TargetParam target, int abilityDmg, float hitChance

    # add up the damage of each ability
    total = 0
    for a in sequence:
        total += calcDmg(a, player, target, hitChance, abilityDmg)
    
    # determine the number of aftershock perks and apply damage
    aftershockCount = total // 50000
    aftershockRank = player.perks()[0]
    total += .318 * abilityDmg * aftershockRank # 31.8% on average, will implement full range later

    return np.floor(total)
