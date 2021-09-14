import numpy as np 

def makeAbilities():
  # inputs: ?
  # Ability constructor: Ability(name, style, weaponReq, dmg, adrenReq, adrenChange, duration=3, cooldown=6, isBleed=False, isFlank=False)
  abilities = np.empty(0)

  abilities.append(Ability("wrack", "magic", "both", np.array([18.8,94.], 0, 8, 1, 5, False, False))) # wrack and ruin + bound damage
  # repeat until all the abilities are in the array
  
  return abilities