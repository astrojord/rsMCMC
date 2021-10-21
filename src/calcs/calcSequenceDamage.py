import numpy as np
from calcs.calcDmg import calcDmg
from classes.Ability import Ability
from classes.SelfParam import SelfParam
from classes.TargetParam import TargetParam

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
