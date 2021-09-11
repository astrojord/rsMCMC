import numpy as np
from SelfParam import SelfParam
from TargetParam import TargetParam

def calcAbilityDmg(player, target):
    # inputs: SelfParam player, TargetParam target

    abilityDmg = 0
    if (player.weaponStyle() == "magic"):
        mainhandSpellDmg = 950.4 # Exsanguinate
        offhandSpellDmg = 950.4 # Exsanguinate
        if (player.weaponType() == "2h"):
            abilityDmg = 3.75*player.effectiveLevel() + min(14.4*player.weaponTier(), 1.5*mainhandSpellDmg) + 1.5*player.totalBonus()[0]
        else: # dual wield or swapping
            # mainhand + offhand = total
            abilityDmg = (2.5*player.effectiveLevel() + min(9.6*player.weaponTier(), mainhandSpellDmg) + player.totalBonus()[0]) 
                         + (1.25*player.effectiveLevel() + min(4.8*player.weaponTier(), .5*offhandSpellDmg) + 0.5*player.totalBonus()[0])
  
    if (player.weaponStyle == "ranged"):
        ammoDmg = 912 # enchanted bakriminel bolts (any type)
        if (player.weaponType() == "2h"):
            abilityDmg = 3.75*player.effectiveLevel() + min(14.4*player.weaponTier(), 1.5*ammoDmg) + 1.5*player.totalBonus()[1]
        else: # dual wield or swapping
            # mainhand + offhand = total
            abilityDmg = (2.5*player.effectiveLevel() + min(9.6*player.weaponTier(), ammoDmg) + player.totalBonus()[1]) 
                         + (1.25*player.effectiveLevel() + min(4.8*player.weaponTier(), .5*ammoDmg) + 0.5*player.totalBonus()[1])

    if (player.weaponStyle == "melee"):
        mainhandDmg = 883.2 # MH khopesh
        offhandDmg = 441.6 # OH khopesh
        if (player.weaponType() == "2h"):
            multiplier = 96/149 # average speed
            abilityDmg = 3.75*player.effectiveLevel() + mainhandDmg*multiplier + 1.5*player.totalBonus()[2]
        else: # dual wield or swapping
            # mainhand + offhand = total
            # multiplier = 1 for fastest speed
            abilityDmg = (2.5*player.effectiveLevel() + mainhandDmg + player.totalBonus()[2]) 
                         + (1.25*player.effectiveLevel() + offhandDmg + 0.5*player.totalBonus()[2])

    return np.floor(abilityDmg)
