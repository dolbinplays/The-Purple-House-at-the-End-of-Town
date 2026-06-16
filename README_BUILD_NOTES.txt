The Purple House at the End of Town
v0.26.06.16.1124 - Modular Witch Direction and Blink Polish

Patch focus:
- Removes the visible art-style pop caused by falling back to the old procedural witch during left/right/up movement.
- Keeps the modular painterly witch renderer active for idle and all movement directions.
- Adds subtle direction cues for side/up movement using tiny lean, tiny x-scale shift, head offset, and foot offsets instead of switching sprites.
- Replaces ordinary full-face blink swapping with eyelid-overlay blinking using eyelid_left.png and eyelid_right.png.
- Reserves face_closed_o_mouth.png for rare sleepy/watch idle moments only.
- Improves boot/leg connection by moving boots slightly upward, strengthening the leg connector, and keeping the shadow/feet as the ground point.
- Keeps arm motion subtle and keeps the wand idle-only so it does not float while walking.
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

Known limitation:
- The witch still uses a front-facing modular rig for all directions. This is intentionally smoother than switching art styles, but true side/back modular poses should be a future art pass.
