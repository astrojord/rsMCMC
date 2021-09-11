import numpy as np
from SelfParam import SelfParam
from TargetParam import TargetParam

def generateSequence(n, abilities, player, target):
    # inputs: int n, array of Ability abilities, SelfParam player, TargetParam target
    # returns n length array of validated abilities

    adren = 100 # asssumes start at 100% adrenaline
    