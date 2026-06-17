The Purple House at the End of Town
v0.26.06.16.1718 - Witch Sleeve Anchor Hand Alignment

Patch focus:
- Refactors the canvas hand overlays to use explicit sleeve-mouth and hand-center anchors.
- Retunes normal/blink hand positions so both hands sit inward/upward into the sleeve openings.
- Retunes walkA/walkB hand anchors so hands follow sleeve-mouth positions instead of drifting away.
- Replaces the chunky cuff block with a sleeve-mouth connector:
  - purple sleeve extension/shadow
  - gold cuff ring
  - hand skin shape
  - subtle finger detail
  - top sleeve lip drawn over the wrist
- Updates Witch Debug Viewer markers:
  - shoulder markers remain purple
  - sleeve-mouth markers are gold rings
  - hand-center markers are green rings
  - a line connects each sleeve mouth to its hand center
- Preserves the current movement speed, max speed clamp, walk cadence, canvas blink, face/hat readability, and front-facing cached model approach.

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
- Witch Debug Viewer and controls

Known limitations:
- Hands/cuffs are still canvas-drawn overlays rather than dedicated painted hand/cuff sprites.
- True premium directional movement will still need side/back art or separate directional cached composites later.
