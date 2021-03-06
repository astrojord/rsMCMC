import numpy as np

class TargetParam:
    def __init__(self, level, armorRating, size, affinity=np.full(3, 40, dtype=int), hitMode="avg", vulnerability=False, smokeCloud=False):
        self._level = level # int - combat level
        self._affinity = affinity # np.array(int) - affinity level for each style [magic, ranged, melee]
        self._size = size # int - number of game tiles occupied per side of the target square. example: a value of 3 means the target is a 3x3 square, or 9 tiles total
        self._armorRating = armorRating # int - user-supplied sum of defence level and armor bonuses. example: Vorago's armor rating = 2178 = 90 (level) + 2088 (bonuses)
        self._hitMode = hitMode # string - determines which end of each ability's range to take: max, min, or avg
        self._vulnerability = vulnerability # bool - is vulnerability applied? if yes, damage increase
        self._smokeCloud = smokeCloud # bool - is smoke cloud applied? if yes, hit cap increase and critical damage increase

    @property
    def level(self):
        return self._level

    @property
    def affinity(self):
        return self._affinity
    
    @property
    def size(self):
        return self._size

    @property
    def armorRating(self):
        return self._armorRating

    @property
    def hitMode(self):
        return self._hitMode

    @property
    def vulnerability(self):
        return self._vulnerability

    @property
    def smokeCloud(self):
        return self._smokeCloud