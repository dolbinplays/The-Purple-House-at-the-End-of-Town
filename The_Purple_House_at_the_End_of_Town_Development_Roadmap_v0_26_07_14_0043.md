**THE PURPLE HOUSE  
AT THE END OF TOWN**

**Development Roadmap**

*Phased implementation plan from current prototype to finished cozy-spooky witch life-sim*

Document version: v0.26.07.14.0043 \| Current playable build reference: v0.26.06.16.1842 - Roadmap Gameplay Expansion Pass \| Prepared July 14, 2026

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Roadmap Strategy</strong></p>
<p>Build reusable area, relationship, reverberation, and ending infrastructure before scaling content. Prefer one complete vertical slice per system before multiplying locations.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 1. Current Starting Point

This roadmap assumes the current playable baseline is v0.26.06.16.1842 - Roadmap Gameplay Expansion Pass, with an already-functional hub, movement, witch model, familiars, gardens, graveyard, potions, villager requests, divination, signpost exploration, well, journal/rumor board, audio, and save/load.

# 2. Production Principles

- Preserve the single-file HTML prototype style until the systems outgrow it or an engine migration is deliberately chosen.

- Keep every patch playable and versioned.

- Build one polished example of each new system before scaling content.

- Prioritize systems that make the game more replayable: areas, minigames, relationships, reverberation, and endings.

- Avoid large rewrites unless a feature needs a new architecture.

- Keep save migration in every patch that adds state fields.

- Preserve cutscene hooks for every Recent Story entry so text-first content can later become staged scenes or illustrated vignettes.

- Build toward a fully mapped explorable village and a long-term cast of up to roughly 100 individual villagers without sacrificing depth.

# 3. Roadmap Overview

| **Phase** | **Name**                           | **Primary Goal**                                                                                                        |
|-----------|------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| 0         | Stabilize Current Build            | Verify latest roadmap expansion patch, save/load, potions, exploration, and day loop.                                   |
| 1         | Area Framework                     | Create reusable system for moving between hub, house interior, gardens, graveyard, well scenes, and signpost locations. |
| 2         | House Interior Vertical Slice      | Make the Purple House interior playable and visually meaningful.                                                        |
| 3         | Garden Minigame Vertical Slice     | Turn one garden into a playable ingredient minigame, then expand to both gardens.                                       |
| 4         | Graveyard Spirit Minigame          | Make grave gathering/offering a playable spirit-risk activity.                                                          |
| 5         | Old Well Cinematic Prototype       | Build the signature well camera sequence and omen system.                                                               |
| 6         | Shifting Forest Walk               | Create a replayable forest minigame with procedural-feeling path changes.                                               |
| 7         | Relationship Story Arcs            | Turn villagers into multi-step branching story paths.                                                                   |
| 8         | World Reverberation                | Make magic visibly/audibly/narratively alter the world.                                                                 |
| 9         | Nature Pushback Endgame            | Introduce escalating land resistance and final philosophy choices.                                                      |
| 10        | Endings + Post-Ending Play         | Implement endings, low-magic echoes, and high/balanced-magic continuation hooks.                                        |
| 11        | Polish, Balance, Content Expansion | Scale assets, audio, UI, content, tuning, QA, and release presentation.                                                 |

# Phase 0: Stabilize Current Build

- Test load/old save migration, movement, interaction, Witch Debug Viewer, audio toggles/sliders, journal, and end-day loop.

- Test all old and new potion recipes: Kind Remedy, Minor Hex, Balanced Charm, Trickster Tonic, River-Calming Draught, Moonlit Ward, Honeyed Tongue, Spirit Lantern Oil, Witching Ink, and Gravekind Salve.

- Play at least eight in-game days, then save, refresh, load, and play two more days.

- Fix any missing button handlers, impossible ingredient requirements, inventory negatives, broken journal tabs, or dead-end request choices.

| **Exit Criteria**                           | **Notes**                                             |
|---------------------------------------------|-------------------------------------------------------|
| No blank screens or console-breaking errors | Core patch stability confirmed.                       |
| Save/load works across refresh              | State migration is safe enough for next feature pass. |
| All main systems still accessible           | No regression from roadmap patch.                     |

# Phase 1: Area Framework

Goal: stop treating all places as menu-only interactions and create a reusable area/scene system that can power future levels.

- Add \`currentArea\` state: hub, houseInterior, helpfulGarden, poisonousGarden, graveyard, wellView, signpost location, etc.

- Add transitions: enter area, exit to hub, return to house, end scene.

- Create basic camera/background/layout handling per area.

- Allow area-specific interaction spots, prompts, and UI overlays.

- Store discovered/visited area data in save state.

- Prototype using simple painted/placeholder backgrounds before custom art is ready.

| **Deliverable**                                | **Test**                                                                   |
|------------------------------------------------|----------------------------------------------------------------------------|
| Player can enter/exit at least three areas     | House interior placeholder, garden placeholder, and graveyard placeholder. |
| No current systems removed                     | House menus, potions, journal, familiar switching still work.              |
| Save remembers current/discovered areas safely | Reload returns to safe default if needed.                                  |

# Phase 2: House Interior Vertical Slice

- Create playable Purple House interior area.

- Represent cauldron, shop counter, attic stairs/mirror, bed, familiar nook, basement door, and journal/memory wall as visible interaction points.

- Show house upgrades visually as unlocked props or room changes.

- Keep existing house menu functions as interaction outcomes from objects, not side-panel-only buttons.

- Add small ambience: candle glow, creaks, cauldron bubbles, familiar idle spots.

| **Priority Object** | **Function**                                          |
|---------------------|-------------------------------------------------------|
| Cauldron            | Brew menu and future potion minigame entry.           |
| Shop Counter        | Serve daily visitor.                                  |
| Attic Mirror        | Divination and future unrealized-possibility doorway. |
| Bed                 | End day and summary.                                  |
| Potion Shelf        | Sell extras and inspect inventory.                    |
| Journal Desk        | Journal/Rumor Board.                                  |
| Basement Door       | Forbidden magic and later endgame pressure.           |

# Phase 3: Garden Minigame Vertical Slice

Goal: replace instant garden gathering with a fun, short, repeatable minigame that affects ingredient quantity and quality.

- Implement first garden minigame in Helpful Garden.

- Use timing, identification, or pathing mechanics that work with mouse/keyboard and touch.

- Score outcomes: poor, good, excellent, rare.

- Use familiar bonuses: Toad improves plant reading, Black Cat warns of bad picks, Fox finds alternate harvests, Raven sees omens, Bat helps night plants.

- Expand later to Poisonous Garden with higher risk/reward and power consequences.

| **Outcome** | **Reward Pattern**                                             |
|-------------|----------------------------------------------------------------|
| Poor        | Small ingredient yield, possible damaged plant or wasted time. |
| Good        | Normal ingredient yield.                                       |
| Excellent   | Extra quantity or better quality.                              |
| Rare        | Rare ingredient plus journal note or reverberation clue.       |

# Phase 4: Graveyard Spirit Minigame

- Create playable graveyard area with spirit-safe gathering.

- Add a ritual/minigame around reading symbols, following whispers, or matching offerings to graves.

- Let ghost favor, debt, Bat familiar, Spirit Lantern Oil, Moonlit Ward, and Ward Fence affect difficulty/outcomes.

- Failure can increase ghost debt, cause overnight trouble, create haunting rumors, or attract nature pushback.

- Success can grant Bone Dust, Ghostcap, Spirit Thread, Grave Soil, ghost clues, or spirit relationship paths.

# Phase 5: Old Well Cinematic Prototype

- Build a two-view well scene: player looking down, then inside-well camera looking up after a coin toss.

- Animate or simulate coin falling toward the camera.

- Use the result to deliver rumors, omens, lost items, ghost contact, or alternate-world hints.

- Use low/high magic state to change how much the well reveals.

- Foreshadow post-ending possibility without fully explaining it too early.

| **Magic State** | **Well Behavior**                                                      |
|-----------------|------------------------------------------------------------------------|
| Low             | Reflection flickers, almost reveals another witch, then fades.         |
| Balanced        | Shows omens, warnings, and negotiated paths.                           |
| High            | Opens deeper views, rifts, alternate witch glimpses, or doorway hints. |

# Phase 6: Shifting Forest Walk

Goal: make the forest one of the game’s signature replayable systems.

- Create a branching path/minigame structure with short nodes: sign, sound, clearing, creature, herb, hazard, landmark, exit.

- Generate forest walks from weighted tables influenced by witch tendencies, world reverberation, ghost favor/debt, town mood, familiar, and relationship flags.

- Add route memory: choices can reveal landmarks or unlock shortcuts, but the forest can still move things around.

- Create outcomes: ingredients, rare encounters, story flags, lost time, rumors, creature sightings, or nature pushback escalation.

- Make the forest visually and narratively reflect the player’s magic flavor.

| **Forest Flavor** | **Example Nodes**                                                      |
|-------------------|------------------------------------------------------------------------|
| Kind              | Firefly path, healing moss, gentle doe, helpful spirit child.          |
| Power             | Thorn gate, wolf howl, bat crossing, black root cache.                 |
| Mischief          | False signpost, goblin bargain, laughing mushrooms, looping path.      |
| Spirit            | Ghost lantern, pale footprints, ancestor whisper, grave bell in trees. |
| Greed             | Coin-eyed crow, glittering shortcut, debt shrine, locked chest.        |
| Balance           | Crossroads stone, mirrored flowers, twin moon puddle, neutral watcher. |

# Phase 7: Relationship Story Arcs

- Pick 3 anchor villagers for first multi-step arcs, such as Mara the Baker, Tessa the Widow, and Mayor Puddlewick.

- Add relationship thresholds that unlock new requests, confessions, visits, locations, or rival events.

- Create different branches for trust, fear, debt, suspicion, gratitude, and resentment.

- Ensure arcs can feed ending paths and nature pushback.

- Add relationship journal summaries that explain why new scenes are available.

| **Arc State**   | **Possible Trigger**                                             |
|-----------------|------------------------------------------------------------------|
| Trust Path      | Villager asks for personal help or confesses hidden truth.       |
| Fear Path       | Villager obeys but may inform the mayor or seek protection.      |
| Debt Path       | Villager offers or demands a favor.                              |
| Suspicion Path  | Villager tests the witch or investigates strange events.         |
| Resentment Path | Villager spreads rumors or becomes opposition.                   |
| Gratitude Path  | Villager brings gifts, testimony, or unlocks a private location. |

# Phase 8: World Reverberation System

- Add hidden or visible reverberation scores by magic flavor.

- Trigger ambient changes in hub and areas: fireflies, bats, wolf howls, fairy rumors, goblin sightings, ghost lights, coin-crows.

- Use Rumor Board and end-day summary to surface reverberation.

- Let reverberation change minigame tables, area appearance, villager requests, and available story paths.

- Add a “world state” summary that feels poetic rather than purely statistical.

| **Implementation Layer** | **Example**                                                                   |
|--------------------------|-------------------------------------------------------------------------------|
| Visual                   | Bats hang around the roof after repeated dark magic.                          |
| Audio                    | Wolf howls at night when power magic and unrest are high.                     |
| Rumor                    | Villagers report fairies, elves, gremlins, trolls, or goblins in the shadows. |
| Gameplay                 | Mischief increases trick nodes in the forest.                                 |
| Story                    | High spirit reverberation unlocks ghost relationship paths.                   |

# Phase 9: Nature Pushback / Restoring Order

- Add a late-game pressure meter or narrative flag representing the natural order pushing back.

- Escalate based on total reverberation, unbalanced tendencies, ghost debt, village unrest, and major magical choices.

- Manifest pushback in changing areas: blocked forest paths, strange seasons, wells failing to reflect, restless spirits, animals avoiding town.

- Introduce story events where the player learns the land is reacting, not merely being haunted.

- Prepare three endgame philosophies: force magic to stay, restore old order, or bind balance.

| **Pushback Level** | **Gameplay Signs**                                                       |
|--------------------|--------------------------------------------------------------------------|
| Low                | Odd rumors, small ambient changes, flickering omens.                     |
| Medium             | Area mutations, more dangerous minigames, villagers notice patterns.     |
| High               | Blocked routes, shared dreams, unstable magic, forced endgame decisions. |

# Phase 10: Endings and Post-Ending Play

- Implement ending eligibility based on witch tendencies, relationships, town mood, ghost state, reverberation, pushback, and major choices.

- Each archetype should face the same central question through its own final struggle.

- Create Low-Magic, Balanced-Magic, and High-Magic post-ending states.

- Low-Magic endings should provide bittersweet closure with faint hints of unrealized possibilities.

- Balanced-Magic endings should allow continued stewardship of the changed world.

- High-Magic endings may unlock rifts, mirror/well portals, alternate witch worlds, and New Game+ style possibility travel.

| **Post-Ending Type**          | **Required Design Work**                                                                        |
|-------------------------------|-------------------------------------------------------------------------------------------------|
| Low-Magic Closure             | Final scenes, subtle mirror/well/house hints, optional final journal line.                      |
| Balanced Stewardship          | Continue world with pact maintenance, altered areas, relationship epilogues.                    |
| High-Magic Possibility Travel | Portal framework, alternate-world selectors, alternate witch variants, unrealized path content. |

# Phase 11: Polish, Balance, and Release Presentation

- Tune economy, ingredient availability, potion value, daily pacing, and minigame rewards.

- Commission or generate final environment art for hub, interiors, gardens, graveyard, well, forest, and signpost areas.

- Replace placeholder tracks with finalized soundtrack: Moonlit Hearth, Haunted Herbarium, Crystal Cauldron, Familiars Footsteps, Rain on Spellbook, Midnight Market, and future area themes.

- Add accessibility options: readable text scale, reduced motion, audio sliders, input remapping if possible, high contrast prompts.

- Build store-page mockups, screenshots, trailer beats, capsule art, and demo build packaging.

- Create testing matrix for endings, save migration, minigames, relationship arcs, and post-ending states.

# 4. Recommended Next Patch

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Best Next Build Target</strong></p>
<p>Do not try to implement every new vision element at once. The next strong patch should build the reusable Area Framework and one playable vertical slice, preferably the Purple House Interior or Helpful Garden minigame.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| **Candidate**                   | **Why It Is Good Next**                                                             | **Risk**                                          |
|---------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------|
| Area Framework + House Interior | Creates reusable architecture and makes upgrades/progression emotionally visible.   | Medium: touches scene rendering and interactions. |
| Helpful Garden Minigame         | Turns a core daily action into gameplay and creates reusable minigame reward logic. | Medium-low: can be self-contained.                |
| Old Well Cinematic              | High-impact signature moment and strong identity feature.                           | Medium: needs camera/scene presentation work.     |
| Shifting Forest Prototype       | Very exciting replay system, but benefits from area framework first.                | Medium-high: more design/balance uncertainty.     |

# 5. Testing Checklist by Patch Type

| **Patch Type**         | **Must Test**                                                                             |
|------------------------|-------------------------------------------------------------------------------------------|
| Save/state changes     | Old save load, refresh/load, new fields initialized, no state loss.                       |
| Area changes           | Enter/exit all areas, input still works, near prompts correct, no soft locks.             |
| Minigame changes       | Poor/good/excellent/rare outcomes, rewards, familiar modifiers, failure cases.            |
| Potion/content changes | Ingredient requirements, brew/sell/use, request matching, inventory never negative.       |
| Relationship changes   | Threshold triggers, journal notes, duplicate scenes, branch persistence.                  |
| Reverberation changes  | World state appears in ambience, rumors, minigames, and summaries without feeling random. |
| Ending changes         | Eligibility, final choices, post-ending state, low-magic hints, no accidental lockouts.   |

# 6. Milestone Definition of Done

- Feature is playable without console-breaking errors.

- Feature saves and loads safely.

- Feature has at least one clear UI/journal explanation.

- Feature supports at least one familiar or relationship hook where appropriate.

- Feature creates story feedback through rumors, day summary, or world changes.

- Feature can be extended data-first instead of requiring a rewrite.

- Feature has been tested for at least a short multi-day play session.

# 7. Long-Term Content Targets

| **Content Category**  | **Initial Target**                                  | **Fuller Target**                                                                                                                     |
|-----------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Villager arcs         | 3 multi-step anchor arcs                            | A large recurring cast, eventually supporting up to about 100 individual villagers with clustered and archetype-sensitive storylines. |
| Playable areas        | House, one garden, graveyard, forest                | A fully mapped explorable village, all signpost destinations, connected wilderness, and post-ending realms.                           |
| Minigames             | Garden, graveyard, forest                           | Potion, market, well, ritual, and relationship scenes.                                                                                |
| Endings               | 3 philosophy endings                                | 10 archetype endings with variants.                                                                                                   |
| Post-game             | Low/balanced/high magic state prototypes            | Alternate witch worlds and unrealized path travel.                                                                                    |
| Cutscenes / vignettes | Cutscene hooks and placeholders for key story beats | An associated cutscene, vignette, or staged scene for every Recent Story entry.                                                       |
| Audio tracks          | 6 current loop replacements                         | Area, minigame, ending, and reverberation variants.                                                                                   |

# 8. Content Scaling Order

1.  Deepen 3 anchor villagers into complete multi-step arcs.

2.  Expand to 10-15 recurring villagers across the first fully explorable village district.

3.  Add additional districts, households, professions, and social clusters only after the relationship framework is stable.

4.  Grow toward the long-term population target of up to roughly 100 villagers through reusable data-driven story structures.

5.  Convert Recent Story entries into associated cutscenes or vignettes in priority order, beginning with major relationship turns, world reverberation events, and ending-path scenes.

*End of Development Roadmap*
