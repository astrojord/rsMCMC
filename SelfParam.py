import numpy as np

class SelfParam:
    def __init__(self, weaponTier, weaponType, totalBonus=np.zeros(3), perks=np.zeros(5), curse=0, aura="none", overloadType='none', activeAbilities=np.empty(0, dtype=str), vigour=True, grimoire=True, cancelledChannels=True):
        self._weaponTier = weaponTier # int - level tier of equipped weapon, 1 to 99
        self._weaponType = weaponType # string - two handed only, dual wield only, or both (swapping when needed)
        self._totalBonus = totalBonus # np.array[int] - user calculated total bonus from the armor and jewelry worn: [magic, ranged, melee]
        self._perks = perks # np.array[int] - levels of certain key perks: [aftershock, biting, precise, equilibrium, flanking]
        self._curse = curse # int - tier of the active curse: 0, 95, or 99
        self._aura = aura # string - type of active aura: none, berserker, or accuracy
        self._overloadType = overloadType # string - type of overload currently active on self: none, normal, supreme, or elder
        self._activeAbilities = activeAbilities # array - list of active damage boosting abilities (sunshine, death's swiftness, berserk + weapon specs: ZGS, ECB, and FSoA)
        self._vigour = vigour # bool - is ring of vigour equipped for ultimate abilities? if true, 10% adrenaline retained after usage
        self._grimoire = grimoire # bool - is erethdor's grimoire turned on? if true, extra crit chance
        self._cancelledChannels = cancelledChannels # bool - are concentrated blast and regular fury cancelled after the first hit?
    
    # calculate player accuracy, assuming player is level 99 in attack, strength, magic, and ranged
    def __F(level):
        # F(a) listed at https://runescape.wiki/w/Hit_chance
        return np.floor(.0008*(level**3) + 4*level + 40)

    # calculate effective attack style skill level from various bonuses
    __effectiveLevel = 99
    if (overloadType == "normal"):
        __effectiveLevel += 17
    if (overloadType == "supreme"):
        __effectiveLevel += 19
    if (overloadType == "elder"):
        __effectiveLevel += 21
    
    if (_curse == 95):
        __effectiveLevel += 10
    if (_curse == 99):
        __effectiveLevel += 12
    
    if (_aura == "berserker"):
        __effectiveLevel += 10

    # combine bonuses from effective level, weapon tier, and accuracy-boosting auras
    self._accuracy = np.floor(__F(__effectiveLevel) + 2.5*__F(_weaponTier))
    if (_aura == "berserker" || _aura == "accuracy"):
        self._accuracy *= np.floor(1.1)


    @property
    def weaponTier(self):
        return self._weaponTier

    @property
    def weaponType(self):
        return self._weaponType

    @property
    def totalBonus(self):
        return self._totalBonus

    @property
    def perks(self):
        return self._perks

    @property
    def curse(self):
        return self._curse

    @property
    def aura(self):
        return self._aura

    @property
    def overloadType(self):
        return self._overloadType

    @property
    def activeAbilities(self):
        return self._activeAbilities

    @property
    def vigour(self):
        return self._vigour

    @property
    def grimoire(self):
        return self._grimoire

    @property
    def cancelledChannels(self):
        return self._cancelledChannels

    @property
    def accuracy(self):
        return self._accuracy