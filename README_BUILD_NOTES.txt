The Purple House at the End of Town
v0.26.06.16.1518 - Witch Composite Pose and Cozy Walk Tuning

Patch focus:
- Retunes the cached assembled witch composite so the face is less buried by the hat.
- Moves/reduces the hat slightly and keeps hair/face connected.
- Reduces wand visibility and adds tiny baked gold/body accents to improve readability at map scale.
- Replaces heavy eyelid PNG blink with a simple canvas-drawn curved-line blink.
- Adds stable cached walk frames: normal, blink, walkA, and walkB.
- Uses tiny boot/arm offsets in walkA/walkB to reduce skating without returning to loose paper-doll animation.
- Slows cozy walking by reducing acceleration, adding a max velocity clamp, and reducing step advancement.
- Retunes footstep cadence so it should feel less skittery.
- Updates the Witch Debug Viewer status to show zoom and cached frame mode.

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
- Witch Debug Viewer

Known limitations:
- The witch still uses a front-facing cached model for all directions.
- True side/back motion will need dedicated side/back artwork or separate directional composites later.
