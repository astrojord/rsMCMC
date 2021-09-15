import numpy as np

def getInputs():
    # all of this needs error handling :)
    
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

    s = input("swapping vigour for ults? (y or n) ")
    vigour = True if (s.lower() == "y") else False

    s = input("grimoire on? (y or n) ")
    grimoire = True if (s.lower() == "y") else False

    s = input("cancelling fury/concentrated blast after 1st hit? (y or n) ")
    cancelledChannels = True if (s.lower() == "y") else False

    # get TargetParam info from user
    # (level, armorRating, size, affinity=np.full(3, 40, dtype=int), hitMode="avg", vulnerability=False, smokeCloud=False)
    level = int(input("target's level: (number)"))
    armorRating = int(input("target's armor rating: (number) "))
    size = int(input("target's size: (number, ex: Vorago = 5) "))

    affinity = np.zeros(3)
    affinity[0] = int(input("target's magic affinity: (nummber) "))
    affinity[1] = int(input("target's ranged affinity: (nummber) "))
    affinity[2] = int(input("target's melee affinity: (nummber) "))

    hitMode = input("hit mode: (max, min, or avg): ")

    s = input("is vulnerability applied? (y or n) ")
    vulnerability = True if (s.lower() == "y") else False 

    s = input("is smoke cloud applied? (y or n) ")
    smokeCloud = True if (s.lower() == "y") else False 

    playerInfo = [weaponStyle,  weaponTier, weaponType, totalBonus, perks, curse, aura, overloadType, activeAbilities, vigour, grimoire, cancelledChannels]
    targetInfo = [level, armorRating, size, affinity, hitMode, vulnerability, smokeCloud]

    return playerInfo, targetInfo
           