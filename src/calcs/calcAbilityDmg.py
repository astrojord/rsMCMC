import numpy as np
from classes.SelfParam import SelfParam
from classes.TargetParam import TargetParam

def calcAbilityDmg(player, target):
    # inputs: SelfParam player, TargetParam target

    style = player.weaponStyle()
    baseDmg = 0
    abilityDmg = 0
    if (style == "magic"):
        baseDmg = 950.4 # Exsanguinate
    elif (style == "ranged"):
        baseDmg = 912 # enchanted bakriminel bolts (any type)
    # damage is the same for 2H vs. DW given that the offhand tier is equal to mainhand tier
    abilityDmg = 3.75*player.effectiveLevel + min(14.4*player.weaponTier, 1.5*baseDmg) + 1.5*player.totalBonus[0]

    if (style == "melee"):
        mainhandDmg = 883.2 # MH khopesh
        offhandDmg = 441.6 # OH khopesh
        if (player.weaponType == "2h"):
            multiplier = 96/149 # average speed
            abilityDmg = 3.75*player.effectiveLevel + mainhandDmg*multiplier + 1.5*player.totalBonus[2]
        else: # dual wield or swapping
            # mainhand + offhand = total
            # multiplier = 1 for fastest speed
            abilityDmg = (2.5*player.effectiveLevel + mainhandDmg + player.totalBonus[2]) 
                         + (1.25*player.effectiveLevel + offhandDmg + 0.5*player.totalBonus[2])

    return np.floor(abilityDmg)
