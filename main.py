import numpy as np
import sys
from mcStep import *
from damagePlot import *
from makeAbilities import *
from calcHitChance import *
from calcAbilityDmg import *
from Ability import Ability
from SelfParam import SelfParam
from TargetParam import TargetParam

# EXPECTED COMMAND LINE USAGE:
# $ python main.py n it

def main(args):
    # unpack args
    n, it, weaponStyle, weaponTier, weaponType = args[0:5]

    # get SelfParam info from user
    weaponStyle = input("style of weapon: (magic, ranged, or melee) ")
    weaponTier = int(input("tier of weapon: (number) "))
    weaponType = input("type of weapon: (2h, dw, or both) ")

    totalBonus = np.zeros(3)
    totalBonus[0] = int(input("magic bonus: (number) "))
    totalBonus[1] = int(input("ranged bonus: (number) "))
    totalBonus[2] = int(input("melee bonus: (number) "))
    
    perks = np.zeros(5)
    perks[0] = int(input("aftershock rank: (number) "))
    perks[1] = int(input("biting rank: (number) "))
    perks[2] = int(input("precise rank: (number) "))
    perks[3] = int(input("equilibrium rank: (number) "))
    perks[4] = int(input("flanking rank: (number) "))
    
    curse = int(input("curse tier: (0, 95, or 99) "))
    aura = input("active aura: (berserker, accuracy, or none) ")
    overloadType = input("active overload: (normal, supreme, elder, or none) ")

    activeAbilities = np.empty(0, dtype=str)

    _ = input("swapping vigour for ults? (y or n) ")
    vigour = True if (s.lower() == "y") else False

    _ = input("grimoire on? (y or n) ")
    grimoire = True if (s.lower() == "y") else False

    _ = input("cancelling fury/concentrated blast after 1st hit? (y or n) ")
    cancelledChannels = True if (s.lower() == "y") else False

    # get TargetParam info from user
    # do this soon

    # instantiate player and target, then calculate the hit chance and ability damage
    player = SelfParam(weaponStyle, weaponTier, weaponType, totalBonus, perks, curse, 
                       aura, overloadType, activeAbilities, vigour, grimoire, cancelledChannels)
    target = TargetParam() # do this soon 
    hitChance = calcHitChance(player, target)
    abilityDmg = calcAbilityDmg(player, target)

    # instantiate abilities
    makeAbilities()

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