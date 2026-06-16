The Purple House at the End of Town
v0.26.06.16.0955 - Modular Witch Sprite Assembly and Movement Animation

Patch focus:
- Adds a modular player witch renderer using the cut-up PNG sprite parts.
- Includes all witch sprite part PNGs under assets/sprites/witch_parts/.
- Adds layered rendering, idle breathing, walking bob/sway, random blink, look-around, and pocket-watch-style fidget animation.
- Keeps the previous procedural witch drawing as a safe fallback if sprite parts fail to load.
- Preserves current movement, interactions, familiar switching, expanded journal/rumor board, audio mixer, music crossfade, SFX toggles, potion system, ghost system, attic divination, village exploration, and save/load migration.

Install:
- Copy index.html into the project root.
- Copy the assets/sprites/witch_parts folder into the project, preserving the relative paths.
- Existing audio/background/familiar assets should remain where they already are in the project.
