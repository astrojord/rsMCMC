import numpy as np 

def makeAbilities(vigour):
    # inputs: ?
    # Ability constructor: Ability(name, style, weaponReq, dmg, adrenReq, adrenChange, duration=1, cooldown=25, isBleed=False, isFlank=False)
    # 1 tick = 0.6 seconds // 17 ticks = 10.2 seconds // 25 ticks = 15 seconds // 50 ticks = 30 seconds
    # comments next to abilities denote things that need to eventually be implemented

    ultAdrenCost = -90 if vigour else -100
    abilities = np.empty(0)

    # MISSING, NEEDS ADDED: concentrated blast, forced autos
    # MISSING AND WON'T ADD: punish, kick, pulverise, frenzy

    # magic
    abilities.append(Ability("wrack", "magic", "both", np.array([18.8,94.], 0, 8, 1, 5, False, False))) # wrack and ruin + bound damage
    abilities.append(Ability("impact", "magic", "both", np.array([20.,100.], 0, 8, 1, 25, False, True))) 
    abilities.append(Ability("dragon breath", "magic", "both", np.array([37.,188.], 0, 8, 1, 17, False, False)))
    abilities.append(Ability("sonic wave", "magic", "2h", np.array([31.,157.], 0, 8, 1, 9, False, False))) # 6% accuracy buff to next hit
    abilities.append(Ability("shock", "magic", "both", np.array([20.,100.], 0, 8, 1, 5, False, False)))
    abilities.append(Ability("combust", "magic", "both", np.array([20.*5,37.*5], 0, 8, 1, 25, True, False))) # walked damage
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
    abilities.append(Ability("sunshine", "magic", "both", np.array([0.,0.], 100, ultAdrenCost, 1, 100, False, False))) # 50% dmg buff to magic for 37.8s (planted feet)

    # ranged
    abilities.append(Ability("piercing shot", "ranged", "both", np.array([18.8,94.]), 0, 8, 1, 5, False, False)) # bound damage
    abilities.append(Ability("binding shot", "ranged", "both", np.array([20.,100.]), 0, 8, 1, 25, False, True))
    abilities.append(Ability("snipe", "ranged", "both", np.array([125.,219.]), 0, 8, 3, 17, False, False))
    abilities.append(Ability("dazing shot", "2h", "both", np.array([31.,157.]), 0, 8, 1, 5, False, False)) # greater dazing shot
    abilities.append(Ability("demoralise", "ranged", "both", np.array([20.,100.]), 0, 8, 1, 25, False, False))
    abilities.append(Ability("needle strike", "ranged", "dw", np.array([18.8,94.]), 0, 8, 1, 9, False, False)) # 7% damage buff to next hit (need to look up how many hits exactly)
    abilities.append(Ability("frag shot", "ranged", "both", np.array([20.*5,37.*5]), 0, 8, 1, 5, True, False)) # walked damage
    abilities.append(Ability("corruption shot", "ranged", "both", np.array([33.*5,100.*5]), 0, 8, 1, 25, True, False)) 
    abilities.append(Ability("ricochet", "ranged", "both", np.array([20.,100.]), 0, 8, 1, 17, False, False)) 
    abilities.append(Ability("greater ricochet", "ranged", "both", np.array([20.*2,100.*2]), 0, 8, 1, 17, False, False)) # caroming - each extra hit adds 10-50%

    abilities.append(Ability("rapid fire", "ranged", "both", np.array([150.,752.], 50, -15, 8, 34, False, False))) # premature cancel, crits on individual hits (18.8-94% each)
    abilities.append(Ability("snap shot", "ranged", "both", np.array([200.,330.], 50, -15, 1, 34, False, False))) # crits on individual hits (100-120 and 100-210%)
    abilities.append(Ability("tight bindings", "ranged", "both", np.array([40.,200.], 50, -15, 1, 25, False, True)))
    abilities.append(Ability("bombardment", "ranged", "both", np.array([43.,219.], 50, -15, 1, 50, False, False)))
    abilities.append(Ability("shadow tendrils", "ranged", "both", np.array([66.,500.], 50, -15, 1, 75, False, False)))

    abilities.append(Ability("unload", "ranged", "dw", np.array([380.,840.], 100, ultAdrenCost, 8, 100, False, False))) # crits on individual hits
    abilities.append(Ability("incendiary shot", "ranged", "2h", np.array([250.,350.], 100, ultAdrenCost, 1, 100, False, False))) # crit buff - 10% extra adren for 30s
    abilities.append(Ability("deadshot", "ranged", "both", np.array([37.+62.*5,188.+62.*5], 100, ultAdrenCost, 1, 100, True, False)))
    abilities.append(Ability("death's swiftness", "ranged", "both", np.array([0.,0.], 100, ultAdrenCost, 1, 100, False, False))) # 50% dmg buff to ranged for 37.8s (planted feet)
    
    # melee
    abilities.append(Ability("slice", "melee", "both", np.array([30.,120.]), 0, 8, 1, 5, False, False)) # bound damage
    abilities.append(Ability("backhand", "melee", "both", np.array([20.,100.]), 0, 8, 1, 25, False, True))
    abilities.append(Ability("havoc", "melee", "dw", np.array([31.,157.]), 0, 8, 1, 17, False, False))
    abilities.append(Ability("smash", "melee", "2h", np.array([31.,157.]), 0, 8, 1, 17, False, False))
    abilities.append(Ability("barge", "melee", "both", np.array([25.,125.]), 0, 8, 1, 34, False, False))
    abilities.append(Ability("greater barge", "melee", "both", np.array([25.+80.,125.+80.]), 8, 8, 1, 34, False, False)) # assumes 4.8 second off time, needs bled channel effects
    abilities.append(Ability("sever", "melee", "both", np.array([37.,188.]), 0, 8, 1, 25, False, False))
    abilities.append(Ability("dismember", "melee", "both", np.array([20.*5.,37.*5]), 0, 8, 1, 25, True, False))
    abilities.append(Ability("fury", "melee", "both", np.array([48.,246.]), 0, 8, 4, 9, False, False)) # premature cancel + crit buff
    abilities.append(Ability("greater fury", "melee", "both", np.array([31.,157.]), 0, 8, 1, 9, False, False)) # if this crits, next hit is guaranteed crit + 10% crit chance to next hit regardless
    abilities.append(Ability("cleave", "melee", "2h", np.array([37.,188.]), 0, 8, 1, 12, False, False))
    abilities.append(Ability("decimate", "melee", "2h", np.array([37.,188.]), 0, 8, 1, 12, False, False))

    abilities.append(Ability("forceful backhand", "melee", "both", np.array([40.,200.]), 50, -15, 1, 25, False, True))
    abilities.append(Ability("slaughter", "melee", "both", np.array([20.*5,50.*5]), 50, -15, 1, 25, True, False)) # walked damage
    abilities.append(Ability("flurry", "melee", "both", np.array([40.,200.]), 50, -15, 6, 34, False, False)) # premature cancel, crits on individual hits
    abilities.append(Ability("greater flurry", "melee", "both", np.array([125.,628.]), 50, -15, 6, 34, False, False)) # premature cancel, crits on individual hits
    abilities.append(Ability("hurricane", "melee", "2h", np.array([66.,219.]), 50, -15, 1, 34, False, False)) # shared cd with destroy, crits on individual hits
    abilities.append(Ability("destroy", "melee", "dw", np.array([148.,752.]), 50, -15, 7, 34, False, False)) # premature cancel, crits on individual hits, barge effects, shared cd with hurricane
    abilities.append(Ability("blood tendrils", "melee", "2h", np.array([18.*6.,90.*6]), 50, -15, 1, 75, False, False)) # crits on individual hits
    abilities.append(Ability("quake", "melee", "2h", np.array([43.,219.]), 50, -15, 1, 34, False, False)) # 2 affinity stacks
    abilities.append(Ability("assault", "melee", "both", np.array([172.,876.]), 50, -15, 9, 50, False, False)) # premature cancel, crits on individual hits, barge effects

    abilities.append(Ability("berserk", "melee", "both", np.array([0.,0.], 100, ultAdrenCost, 1, 100, False, False))) # 100% dmg buff to melee for 19.8s
    abilities.append(Ability("meteor strike", "melee", "2h", np.array([250.,350.], 100, ultAdrenCost, 1, 100, False, False))) # crit buff - 10% extra adren for 30s

    return abilities