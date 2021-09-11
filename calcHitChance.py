import numpy as np
from SelfParam import SelfParam
from TargetParam import TargetParam

def calcHitChance(player, target):
    # inputs: SelfParam player, TargetParam target
    
    # STEP 1: calculate player accuracy
    def F(level):
        # F(a) listed at https://runescape.wiki/w/Hit_chance
        return np.floor(.0008*(level**3) + 4*level + 40)

    # combine bonuses from effective level, weapon tier, and accuracy-boosting auras
    accuracy = np.floor(F(player.effectiveLevel()) + 2.5*F(player.weaponTier()))
    if (player.aura() == "berserker" || player.aura() == "accuracy"):
        accuracy *= np.floor(1.1)

    # STEP 2: determine affinity on target based on player style
    if (player.weaponStyle == "magic"):
        effectiveAffinity = target.affinity[0]
    if (player.weaponStyle == "ranged"):
        effectiveAffinity = target.affinity[1]
    if (player.weaponStyle == "melee"):
        effectiveAffinity = target.affinity[2]

    # STEP 3: calculate effective armor rating
    effectiveAR = F(target.level) + target.armorRating

    # STEP 4: math + apply various bonuses
    hitChance = effectiveAffinity * accuracy / effectiveAR
    # track said various bonuses later :)

    return hitChance 