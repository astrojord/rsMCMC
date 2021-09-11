import numpy as np
from SelfParam import SelfParam
from TargetParam import TargetParam
from calcHitChance import *
from calcAbilityDmg import *

def calcDmg(ability, player, target, hitChance, abilityDmg)
    # inputs: Ability ability, SelfParam player, TargetParam target, float hitChance, int abilityDmg
    # return int finalDamage

    # STEP 1: determine if the ability hits or not
    if (np.random.rand() >= hitChance):
        return 0

    # STEP 2: determine how the percentage ability damage changes before scaling with post-percentage factors
    scaledAbilityDmg = abilityDmg
    crit = False # hits are naturally critical if above 95% of potential ability damage (ish)
    bitingRank = player.perks()[1] # 2% forced crit chance per rank
    preciseRank = player.perks()[2] # increases min hit by 1.5% per rank
    equilibriumRank = player.perks()[3] # reduces max and increases min hit by 1% and 3% respectively per rank
    flankRank = player.perks()[4] # increases min and max by 15% and 40% for thresholds and basics respectively per rank
    minDmg = ability.dmg()[0]
    maxDmg = ability.dmg()[1]

    # bleed and flank effects applied before hit mode determination
    if ability.isBleed():
        # not affected by equilibrium
        equilibriumRank = 0;

    if ability.isStun():
        # assume (for now) that all flankable abilities are flanked at same tier as main weapons with no loss of aftershock stacks
        if (ability.adrenChange > 0): # thresholds
            minDmg += .15 * flankRank
            maxDmg += .15 * flankRank
        else: # basics
            minDmg += .4 * flankRank
            maxDmg += .4 * flankRank

    # hit mode calculation, application of precise and equilibrium, and determination of natural crit
    if (target.hitMode() == "min"):  
        scaledAbilityDmg *= minDmg * (1.015 * preciseRank + 1.03 * equilibriumRank)

    elif (target.hitMode() == "max"):
        crit = True
        scaledAbilityDmg *= maxDmg * .99 * equilibriumRank

    elif (target.hitMode() == "avg"):
        newMin = minDmg * 1.015 * preciseRank
        r = np.random.uniform(newMin, maxDmg)
        naturalCritChance = .95 - (.01 * equilibriumRank)
        if r > (naturalCritChance * maxDmg):
            crit = True 
        scaledAbilityDmg *= r

    # STEP 3: determine if a crit is forced by various bonuses
    if ((player.grimoire() and (np.random.rand() < .12)) or (np.random.rand() < (player.perks()[1]*.02))):
        # grim = 12%
        crit = True

    if ability.isBleed():
        # bleeds can never crit, force them back
        crit = False

    # STEP 4: apply various bonuses to the scaled damage and check cap
    damage = scaledAbilityDmg
    hitCap = 10000
    if crit:
        hitCap = 12000
        if player.grimoire():
            hitCap = 15000
        if player.smokeCloud():
            if (ability.style() == "magic"):
                hitCap *= 1.12
                damage *= 1.15
            else: 
                hitCap *= 1.048
                damage *= 1.06
    
    return min(hitCap, damage)

