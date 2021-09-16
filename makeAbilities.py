import numpy as np 

def makeAbilities(vigour):
    # inputs: ?
    # Ability constructor: Ability(name, style, weaponReq, dmg, adrenReq, adrenChange, duration=1, cooldown=25, isBleed=False, isFlank=False)
    # 1 tick = 0.6 seconds // 17 ticks = 10.2 seconds // 25 ticks = 15 seconds // 50 ticks = 30 seconds
    # comments next to abilities denote things that need to eventually be implemented

    ultAdrenCost = 90 if vigour else 100
    abilities = np.empty(0)

    # magic
    # MISSING ENTIRELY: concentrated blast, forced autos
    abilities.append(Ability("wrack", "magic", "both", np.array([18.8,94.], 0, 8, 1, 5, False, False))) # wrack and ruin + bound damage
    abilities.append(Ability("impact", "magic", "both", np.array([20.,100.], 0, 8, 1, 25, False, True))) 
    abilities.append(Ability("dragon breath", "magic", "both", np.array([37.,188.], 0, 8, 1, 17, False, False)))
    abilities.append(Ability("sonic wave", "magic", "2h", np.array([31.,157.], 0, 8, 1, 9, False, False))) # 6% accuracy buff to next hit
    abilities.append(Ability("shock", "magic", "both", np.array([20.,100.], 0, 8, 1, 5, False, False)))
    abilities.append(Ability("combust", "magic", "both", np.array([20.*5,37.*5], 0, 8, 1, 25, True, False)))
    abilities.append(Ability("shock", "magic", "both", np.array([20.,100.], 0, 8, 1, 25, False, False)))
    abilities.append(Ability("chain", "magic", "both", np.array([20.,100.], 0, 8, 1, 17, False, False))) # greater chain, caroming
    abilities.append(Ability("corruption blast", "magic", "both", np.array([33.*5,100.*5], 0, 8, 1, 25, True, False)))
    abilities.append(Ability("asphyxiate", "magic", "both", np.array([150.,752.], 50, -15, 7, 34, False, False))) # premature cancel
    abilities.append(Ability("deep impact", "magic", "both", np.array([40.,200.], 50, -15, 1, 25, False, True)))
    abilities.append(Ability("wild magic", "magic", "both", np.array([50.+50.,165.+215.], 50, -15, 1, 34, False, False)))
    abilities.append(Ability("smoke tendrils", "magic", "both", np.array([115.,575.], 50, -15, 10, 75, False, False))) # premature cancel + all hits are considered crit regardless of dmg
    abilities.append(Ability("detonate", "magic", "both", np.array([100.,350.], 50, -15, 4, 50, False, False))) # option w/o deto boots? + release w/ autos or other abilities
    abilities.append(Ability("omnipower", "magic", "both", np.array([200.,400.], 100, ultAdrenCost, 1, 100, False, False)))
    abilities.append(Ability("tsunami", "magic", "both", np.array([200.,300.], 100, ultAdrenCost, 1, 100, False, False))) # crit buff - 10% extra adren for 30s
    abilities.append(Ability("metamorphosis", "magic", "both", np.array([0.,0.], 100, ultAdrenCost, 1, 100, False, False))) # 62% dmg buff to magic for 15s
    abilities.append(Ability("sunshine", "magic", "both", np.array([0.,0.], 100, ultAdrenCost, 1, 5, False, False))) # 50% dmg buff to magic for 37.8s (planted feet)
  # ranged

  # melee
  
  return abilities