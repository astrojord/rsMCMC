# rsMCMC
Markov Chain Monte Carlo optimization of RuneScape 3 damage rotations, using the Metropolis-Hastings algorithm. 
The overall goal is to explore potentially high-damage sequences of casted abilities, perhaps different than the popular rotations made by the community.
These rotations have been built up over years of collaborative work, and there is potential for a more optimal sequence of abilities that we have collectively ignored, since we understandably stick with what we know.

## Assumptions:
- Player is level 99 in Attack, Strength, Ranged, and Magic
- Player is either limited to one of 2H/DW OR is willing to swap between the two as much as possible
- If player is using dual wield, both weapons are of the same tier
- Target is in range and damageable for entire duration
- Any non-damaging debuffs like Vulnerability or Smoke Cloud are pre-applied
- Magic auto attacks are Exsanguinate
- Ranged auto attacks use non-specific enchanted bakriminel bolts
- Melee auto attacks are average speed if 2H, fastest speed if DW, and use T92 damage

## To do:
- Abilities:
    - Expand the list of supported special attack weapons
- Player and gear parameters: 
    - Melee auto attack damage scales properly with weapon tier 
    - 4-8 boosted damage from effective levels past 99 + effects from perks (https://runescape.wiki/w/Ability_damage#Boosting_ability_damage)
    - Magic spell selection
    - Effects on successful casts of Concentrated Blast, Fury, Dazing Shot, and Needle Strike
    - Greater (ability) codexes: Barge, Flurry, Fury, Ricochet, Dazing Shot/Salt the Wound, Chain
    - Essence of Finality-stored special attack weapons
    - 4TAA
    - Cancelled channeled thresholds (namely Rapid Fire, Asphyxiate, Assault, Destroy, and Flurry)
    - Dark Shard and Sliver of Leng weapon and set effects
    - Exsanguinate and enchanted bakriminel bolt effects
    - Strength skillcape effect
    - Trimmed Masterwork Spear effect
    - Damage- or accuracy-boosting glove effects (Gloves of Passage, Nightmare Gauntlets, and Kerapac's Wristwraps)
    - Damage- or accuracy-boosting ring effects (ASR, reaver ring, etc.)
    - Cross style accuracy penalty
    - Incense sticks (kwuarm, others?)
    - Weapon poison and cinderbane gloves
- Target parameters: 
    - Smoke Cloud
    - Pre-applied affinity stacks
    - Affinity changes upon ability use (Quake, Guthix Staff, SWH, Bandos godbook etc.)
    - Flanking availability
    - Stun status and immunity (for Wrack/Piercing Shot/Slice boosted damage)
- Code/performance:
    - `args`/`kwargs` in class constructors
    - MCMC performance optimization?
    - Accuracy calculation optimization


RuneScape and its content are the copyright and trademark property of Jagex.