import numpy as np
from SelfParam import SelfParam
from TargetParam import TargetParam

def calcHitChance(player, target):
    # inputs: SelfParam player, TargetParam target
    
    # STEP 1: calculate player accuracy
        # F(a) listed at https://runescape.wiki/w/Hit_chance
        return np.floor(.0008*(level**3) + 4*level + 40)

    # calculate effective attack style skill level from various bonuses
    effectiveLevel = 99 # assume the player is level 99 in attack, strength, magic, and ranged
    if (player.overloadType() == "normal"):
        effectiveLevel += 17
    if (player.overloadType() == "supreme"):
        effectiveLevel += 19
    if (player.overloadType() == "elder"):
        effectiveLevel += 21
    
    if (player.curse() == 95):
        __effectiveLevel += 10
    if (player.curse() == 99):
        effectiveLevel += 12
    
    if (player.aura() == "berserker"):
        effectiveLevel += 10

    # combine bonuses from effective level, weapon tier, and accuracy-boosting auras
    accuracy = np.floor(F(effectiveLevel) + 2.5*F(player.weaponTier()))
    if (player.aura() == "berserker" || player.aura() == "accuracy"):
        accuracy *= np.floor(1.1)

    # STEP 2: