import numpy as np

class TargetParam:
    def __init__(self, affinity=np.full(3, 40, dtype=int), armorRating, hitMode="avg", vulnerability=False, smokeCloud=False):
        self._affinity = affinity
        self._armorRating = armorRating # int -
        self._hitMode = hitMode # string - determines which end of each ability's range to take: max, min, or avg
        self._vulnerability = vulnerability # bool - is vulnerability applied? if yes, damage increase
        self._smokeCloud = smokeCloud # bool - is smoke cloud applied? if yes, hit cap increase and critical damage increase