The Purple House at the End of Town
v0.26.06.16.1042 - Modular Witch Rig Alignment Fix

Patch focus:
- Focused rigging/alignment fix for the modular witch avatar.
- Adds a centralized WITCH_PART_LAYOUT table for easier tuning.
- Tightens hat, hair, and face into a single coherent head group.
- Reduces the oversized skirt/cloak impact so boots and grounding are clearer.
- Keeps boots closer to the ground point and uses smaller foot shifts.
- Reduces walking bob, body sway, and secondary hat/hair motion.
- Keeps wand subtle and hides it while walking to avoid floating/dangling.
- Uses the older procedural directional witch renderer for left/right/up movement until true modular side/back poses are created.
- Preserves the previous procedural renderer as a safe fallback if sprite parts fail to load.

Preserved systems:
- Movement controls and interaction detection
- Familiar switching and animated familiars
- Helpful garden, poisonous garden, graveyard, and Spirit Offering Plate
- Ghost favor/debt/prepayment
- Potion brewing, usable potions, potion shelf/sell extras
- Villager requests, relationship memory, and follow-up rumors
- Attic Divination, Village Signpost exploration, Old Well
- Expanded Journal/Rumor Board and tabs
- Audio mixer, music/SFX toggles/sliders, music crossfade, WebAudio SFX
- Save/load migration

Known limitation:
- The modular art is still a front/down-facing rig. Side and up movement currently fall back to the older procedural witch until dedicated modular side/back poses are made.
