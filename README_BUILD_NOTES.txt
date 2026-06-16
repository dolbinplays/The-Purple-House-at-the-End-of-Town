The Purple House at the End of Town
v0.26.06.16.1548 - Premium Witch Walk Feel

Patch focus:
- Retunes the cached witch composite so the hat is slightly higher/smaller and the face has more breathing room.
- Strengthens stable walkA/walkB frame differences while keeping the cached model coherent.
- Adds tiny whole-sprite weight transfer: small side shift, gentle settle, and reduced float.
- Keeps movement speed responsive while syncing step cadence better to the walk frames.
- Polishes canvas blink timing and line weight.
- Upgrades the Witch Debug Viewer:
  - wider/taller panel
  - 300x300 canvas
  - pause debug animation
  - frame-step button
  - 2x/3x zoom toggle
  - origin/foot-contact/bounding-box markers toggle
  - clearer cached-frame status readout

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
- The witch still uses a front-facing cached composite for all directions.
- Premium side/back movement will eventually need dedicated directional art or separate cached directional composites.
