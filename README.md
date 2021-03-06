# rsMCMC
Markov Chain Monte Carlo optimization of RuneScape 3 damage rotations, using the Metropolis-Hastings algorithm. 

The game's community has done a lot of work over the years optimizing dynamic rotations of abilities, and collaboratively working to maximize the amount of damage dealt to a particular boss or monster. However, I've always wondered if there's some sort of bias in those conversations, and if we're so confident in what we've accomplished that we might be missing a better solution that we just haven't thought of yet. The goal of this work is to generate and explore new options for ability rotations in an effort to spur the imagination of the community, and introduce new ideas for discussion.

## Assumptions:
- All rotations are against a single target with no nearby secondary targets
- All rotations start at 100% adrenaline
- Player is level 99 in Attack, Strength, Ranged, and Magic
- Player is either limited to one of 2H/DW OR is willing to swap between the two as much as possible
- If player is using dual wield, both weapons are of the same tier
- Target is in range and damageable for entire duration
- Any non-damaging debuffs like Vulnerability or Smoke Cloud are pre-applied
- Magic auto attacks are Exsanguinate
- Ranged auto attacks use non-specific enchanted bakriminel bolts
- Melee auto attacks are average speed if 2H, fastest speed if DW, and use T92 damage
- All flankable abilities are flanked at the same tier as main weapons and without loss of Aftershock stacks
- All Sunshine and Death's Swiftness uses are done with a Planted Feet switch without loss of Aftershock stacks

## To do:
- Abilities:
    - Expand the list of supported special attack weapons
    - Natural and forced auto attacks
- Player and gear parameters: 
    - Melee auto attack damage scales properly with weapon tier 
    - 4-8 boosted damage from effective levels past 99 + effects from perks (https://runescape.wiki/w/Ability_damage#Boosting_ability_damage)
    - Effects on successful casts of Concentrated Blast, Fury, Dazing Shot, and Needle Strike
    - Greater (ability) codexes: Barge, Flurry, Fury, Ricochet, Dazing Shot/Salt the Wound, Chain
    - Essence of Finality-stored special attack weapons
    - Magic spell selection
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
    - Start at adrenaline lower than 100% (or up to 110%)
- Target parameters: 
    - Pre-applied affinity stacks
    - Affinity changes upon ability use (Quake, Guthix Staff, SWH, Bandos godbook etc.)
    - Flanking availability
    - Stun status and immunity (for Wrack/Piercing Shot/Slice boosted damage)
- Code/performance:
    - `args`/`kwargs` in class constructors
    - MCMC performance optimization?
    - Accuracy calculation optimization
    - Should average damage calculations be seeded for reproducibility?


RuneScape and its content are the copyright and trademark property of Jagex.