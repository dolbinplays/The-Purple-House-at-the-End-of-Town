The Purple House at the End of Town
v0.26.06.16.1447 - Witch Debug Viewer

Patch focus:
- Adds a toggleable Witch Model Debug Viewer for inspecting the current assembled witch model while playing.
- Adds a Witch Debug button in the floating button group near Rumor Board and Journal.
- The viewer opens in the lower-left corner of the game screen and closes when the same button is clicked again.
- The viewer uses a separate 280x280 canvas with a plain white background.
- It renders the current cached assembled witch model at approximately 2x normal gameplay size.
- It updates live while the witch idles, blinks, walks, and changes facing state.
- It shows status text for facing direction, moving true/false, speed, animation step, and frame.
- It includes a faint baseline/centerline to help screen recordings show foot grounding and sliding.

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
- The viewer reflects the current stable front-facing cached witch model. It does not create new side/back witch art.
- The debug panel is intentionally a development aid and may overlap lower-left gameplay if left open.
