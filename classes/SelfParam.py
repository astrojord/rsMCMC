import numpy as np

class SelfParam:
    def __init__(self, weaponStyle, weaponTier, weaponType, totalBonus=np.zeros(3), perks=np.zeros(5), curse=0, aura="none", overloadType='none', activeAbilities=np.empty(0, dtype=str), vigour=True, grimoire=True, cancelledChannels=True):
        self._weaponStyle = weaponStyle # string - magic, ranged, or melee (needed to track cross-style accuracy penalties and affinities)
        self._weaponTier = weaponTier # int - level tier of equipped weapon, 1 to 99
        self._weaponType = weaponType # string - two handed only, dual wield only, or both (swapping when needed)
        self._totalBonus = totalBonus # np.array[int] - user-supplied total bonus from the armor and jewelry worn: [magic, ranged, melee]
        self._perks = perks # np.array[int] - levels of certain key perks: [aftershock, biting, precise, equilibrium, flanking]
        self._curse = curse # int - tier of the active curse: 0, 95, or 99
        self._aura = aura # string - type of active aura: none, berserker, or accuracy
        self._overloadType = overloadType # string - type of overload currently active on self: none, normal, supreme, or elder
        self._activeAbilities = activeAbilities # array - list of active damage boosting abilities (sunshine, death's swiftness, berserk + weapon specs: ZGS, ECB, and FSoA)
        self._vigour = vigour # bool - is ring of vigour equipped for ultimate abilities? if true, 10% adrenaline retained after usage
        self._grimoire = grimoire # bool - is erethdor's grimoire turned on? if true, extra crit chance
        self._cancelledChannels = cancelledChannels # bool - are concentrated blast and regular fury cancelled after the first hit?

    # calculate effective attack style skill level from various bonuses
    self._effectiveLevel = 99 # assume the player is level 99 in attack, strength, magic, and ranged
    if (player.overloadType() == "normal"):
        self._effectiveLevel += 17
    if (player.overloadType() == "supreme"):
        self._effectiveLevel += 19
    if (player.overloadType() == "elder"):
        self._effectiveLevel += 21
    
    if (player.curse() == 95):
        self._effectiveLevel += 10
    if (player.curse() == 99):
        self._effectiveLevel += 12
    
    if (player.aura() == "berserker"):
        self._effectiveLevel += 10

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
    def effectiveLevel(self):
        return self._effectiveLevel