The Purple House at the End of Town
v0.26.06.16.1352 - Stable Witch Model and Walk Speed Fix

Patch focus:
- Stabilizes the witch by building a cached composite sprite from the modular part PNGs.
- Draws the assembled witch as one coherent character during gameplay instead of animating many loose paper-doll pieces.
- Keeps eyelid-overlay blinking as the only part-level runtime overlay.
- Removes independent hat, hair, cape, arm, boot, squash, and strong direction transforms during walking.
- Reduces movement acceleration and increases damping so the witch walks at a slower cozy pace.
- Slows the walk-step timer and footstep cadence so the animation better matches travel speed.
- Preserves the old procedural witch renderer only as emergency fallback if modular sprite assets fail to load.

Preserved systems:
- Movement controls and interaction detection
- Familiar switching and animated familiars
- Helpful garden, poisonous garden, graveyard gathering, and Spirit Offering Plate
- Ghost favor/debt/prepayment
- Potion brewing, usable potions, potion shelf/sell extras
- Villager requests, relationship memory, and follow-up rumors
- Attic Divination, Village Signpost exploration, Old Well
- Expanded Journal/Rumor Board and journal tabs
- Audio mixer, music/SFX toggles/sliders, music crossfade, WebAudio SFX
- Save/load migration

Known limitations:
- The witch still uses a front-facing assembled model for all directions until true side/back modular artwork is available.
- This patch prioritizes a stable readable character over advanced walk-cycle limb animation.
