import numpy as np

class Ability:
    def __init__(self, name, style, weaponReq, dmg, adrenReq, adrenChange, castTime, duration=3 isBleed=False, isFlank=False):
        self._name = name # string - ability name
        self._style = style # string - magic, ranged, or melee
        self._weaponReq = weaponReq # string - two handed or dual wield
        self._dmg = dmg # np.array[float] - [low end, high end]
        self._adrenReq = adrenReq # int - how much adrenaline is required to use the ability
        self._adrenChange = adrenChange # int - how much adrenaline is gained/lost on ability usage
        self._castTime = castTime # np.array[int] - instances that damage is applied to target, in terms of ticks after ability cast time
        self._duration = duration # int - number of ticks that it takes to fully cast the ability without cancellation
        self._isBleed = isBleed # bool - is the ability considered a bleed? if yes, no crit can occur
        self._isStun = isStun # bool - is the ability able to be flanked? if yes, flanking can apply

    @property
    def name(self):
        return self._name
    
    @property
    def style(self):
        return self._style

    @property
    def weaponReq(self):
        return self._weaponReq

    @property
    def dmg(self):
        return self._dmg

    @property
    def adrenReq(self):
        return self._adrenReq

    @property
    def adrenChange(self):
        return self._adrenChange

    @property
    def castTime(self):
        return self._castTime
    
    @property
    def isBleed(self):
        return self._isBleed

    @property
    def isFlank(self):
        return self._isFlank