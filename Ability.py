import numpy as np

class Ability:
    def __init__(self, name, style, weaponReq, dmg, adrenReq, adrenChange, castTime):
        self._name = name # string - ability name
        self._style = style # string - magic, ranged, or melee
        self._weaponReq = weaponReq # string - two handed or dual wield
        self._dmg = dmg # np.array[int] - [% low end, % high end]
        self._adrenReq = adrenReq # int - how much adrenaline is required to use the ability
        self._adrenChange = adrenChange # int - how much adrenaline is gained/lost on ability usage
        self._castTime = castTime # np.array[int] - instances that damage is applied to target, in terms of ticks after ability cast time

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