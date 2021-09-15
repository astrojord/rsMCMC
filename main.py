import numpy as np
import sys
from mcmc import *
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
    # unpack args and get all the input stuff
    n, it = args[0:1] # need to type check/error handle here
    playerInfo, targetInfo = getInputs()
    weaponStyle, weaponTier, weaponType, totalBonus, perks, curse, aura, overloadType, activeAbilities, vigour, grimoire, cancelledChannels = playerInfo  
    level, armorRating, size, affinity, hitMode, vulnerability, smokeCloud = targetInfo

    # instantiate player and target, then calculate the hit chance and ability damage
    player = SelfParam(weaponStyle, weaponTier, weaponType, totalBonus, perks, curse, 
                       aura, overloadType, activeAbilities, vigour, grimoire, cancelledChannels)
    target = TargetParam() # do this soon 
    hitChance = calcHitChance(player, target)
    abilityDmg = calcAbilityDmg(player, target)

    # instantiate abilities
    abilities = makeAbilities()

    # start with n length sequence of all wrack/piercing shot/slice
    startSequence = []
    if (player.weaponStyle == "magic"):
        startSequence = [wrack] * n
    elif (player.weaponStyle == "ranged"):
        startSequence = [piercingShot] * n
    elif (player.weaponStyle == "melee"):
        startSequence = [_slice] * n

    # run MCMC for specified iterations and store damage for each iteration
    endSequence, damageList = mcLoop(n, it, startSequence, player, target, abilities, hitChance, abilityDmg)
    
    # plot damage over each iteration and return final sequence
    damagePlot(n, it, damageList)
    print("Sequence at final iteration: \n" + endSequence)

if __name__ == '__main__':
    args = sys.argv
    main(args)