The Purple House at the End of Town
v0.26.06.16.1626 - Witch Hand Visibility and Silhouette Polish

Patch focus:
- Improves hand visibility and arm readability on the cached witch composite.
- Keeps sleeve/base-arm sprites partly behind the coat for depth.
- Adds a front hand/cuff overlay pass after the coat/skirt so both hands remain readable.
- Makes the player-left / witch-right hand clearly visible instead of buried behind clothing.
- Makes the player-right / witch-left hand more readable while still partly tucked into the silhouette.
- Strengthens walkA/walkB arm contribution with small counter-swing deltas.
- Keeps the subdued wand treatment so it does not clutter the silhouette.
- Adds hand and shoulder markers to the Witch Debug Viewer when markers are enabled.
- Preserves the stable cached composite model and current cozy movement feel.

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
- The hands are canvas-drawn overlay shapes rather than true separated painted hand sprites.
- True premium side/back movement will still need dedicated directional art or separate cached directional composites later.
