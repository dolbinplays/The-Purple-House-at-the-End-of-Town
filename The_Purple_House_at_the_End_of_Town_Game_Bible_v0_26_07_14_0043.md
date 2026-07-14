**THE PURPLE HOUSE  
AT THE END OF TOWN**

**Game Bible**

*Cozy-spooky witch life-sim design bible and source-of-truth direction*

Document version: v0.26.07.14.0043 \| Current playable build reference: v0.26.06.16.1842 - Roadmap Gameplay Expansion Pass \| Prepared July 14, 2026

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Design Thesis</strong></p>
<p>The player does not simply live in a magical world. The player makes the world magical, watches it reverberate, and then must answer for what it becomes.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 1. High Concept

The Purple House at the End of Town is a cozy-spooky witch life-sim about a witch who inherits a crooked purple house at the edge of a strange village. Through potions, favors, gardens, ghosts, familiars, rumors, divination, bargains, and moral choices, the player gradually shapes both the town and the wider magical world.

The game should feel approachable and charming on the surface, with a deeper fairy-tale consequence engine underneath. It should support everyday cozy play while slowly revealing that magic changes the land itself.

# 2. Player Fantasy

- Live as the village witch in a crooked purple house at the edge of town.

- Brew potions, gather strange ingredients, manage a familiar, tend gardens, and answer villager requests.

- Become a beloved healer, feared hag, gray bargain-maker, trickster, spirit-keeper, curse-breaker, merchant witch, witch queen, exile, or something stranger.

- See the village remember choices and react through rumors, relationships, ghost ledgers, and changing world ambience.

- Eventually confront whether the awakened magic should remain, be sealed away, or be balanced with the old natural order.

# 3. Tone and Aesthetic

- Cozy-spooky, not horror. The world can be eerie, haunted, and morally complicated, but should still feel inviting.

- Aspirational target: a Dreamlight Valley-style sense of place and returnability, filtered through a cozy indie witch game.

- Palette: warm purples, moonlit blues, candle gold, moss green, soft off-white highlights, and gentle supernatural glow.

- Visual language: painterly / illustrated indie style, readable at gameplay scale, whimsical but emotionally grounded.

- Music: premium cozy witch soundtrack with magical home, garden, cauldron, familiar, rain, and midnight market themes.

# 4. Current Implemented Foundation

| **System**           | **Current Role**                                                                     |
|----------------------|--------------------------------------------------------------------------------------|
| Village hub          | Isometric-style hub centered on the Purple House and nearby interaction spots.       |
| Witch avatar         | Stable cached witch model with movement, walk feel, blink, and debug viewer.         |
| Familiars            | Selectable Black Cat, Raven, Toad, Bat, and Fox with flavor/bonus hooks.             |
| Gardens              | Helpful and poisonous gardens provide ingredients and moral/resource texture.        |
| Graveyard            | Spirit gathering, ghost favor/debt, prepayment, and offerings.                       |
| Potions              | Brewable prepared potions, usable in villager choices or sold from shelf.            |
| Villager requests    | Named villagers with good/dark/gray/mischief solutions and consequences.             |
| Relationships        | Trust/fear/debt/gratitude/resentment/suspicion memory per villager.                  |
| Attic Divination     | Mirror reveals hidden truths and consequence hints.                                  |
| Signpost exploration | Text/event exploration to village and wilderness destinations.                       |
| Old Well             | Wishes, rumors, and spirit-related mystery.                                          |
| Journal/Rumor Board  | Categorized archive of rumors, villagers, ghosts, visions, exploration, and potions. |
| Audio                | Music/SFX controls, randomized crossfading soundtrack, WebAudio SFX.                 |
| Save/load            | Versioned save with migration defaults.                                              |

# 5. Core Gameplay Loop

1.  Wake in the Purple House and review the village mood, rumors, potion needs, ghost ledger, and available exploration.

2.  Choose a familiar or keep the current one based on the day’s plan.

3.  Gather ingredients from gardens, graveyard, forest, market, river, or other locations.

4.  Brew prepared potions or save ingredients for on-the-spot solutions.

5.  Serve a villager request with a good, dark, gray, or mischief solution.

6.  Deal with spirits, offerings, debt, or divination when needed.

7.  Explore a location or advance a relationship/story branch.

8.  End the day and watch rumors, ghost consequences, town mood, and magical reverberations surface overnight.

# 6. Witch Tendencies and Archetypes

| **Archetype / Tendency**   | **Core Fantasy**                                        | **Typical World Effect**                                                                          |
|----------------------------|---------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Kindness / Beloved Witch   | Healing, protection, mercy, community trust.            | Warm lanterns, magical fireflies, glowing herbs, villagers become hopeful but may grow dependent. |
| Power / Feared Hag         | Curses, intimidation, domination, dangerous competence. | Bats, thorns, wolf howls, cold moonlight, fearful whispers.                                       |
| Balance / Gray Witch       | Bargains, boundaries, pacts, careful compromise.        | Crossroads omens, mirrored flowers, strange but stable rituals.                                   |
| Greed / Merchant Witch     | Contracts, prices, favors, magical economy.             | Coin-eyed crows, debt spirits, locked doors, gold glints in puddles.                              |
| Mischief / Trickster Witch | Pranks, loopholes, chaos, playful justice.              | Gremlins, goblins, shifting signs, laughing mushrooms, impossible rumors.                         |
| Spirit-Keeper              | Respecting and negotiating with the dead.               | Blue candle flames, ghost lanterns, grave bells, clearer spirit activity.                         |
| Curse-Breaker              | Undoing harm and transforming old pain.                 | Protective wards, softened curses, old scars becoming safeguards.                                 |
| Witch Queen                | Shaping the world openly through will and authority.    | Magic becomes organized around the witch; the land may kneel or rebel.                            |
| Vanishing House            | Threshold magic, liminality, refuge, departure.         | Doors, mirrors, wells, and house rooms become crossings between possibilities.                    |

# 7. Potions and Ingredients

Prepared potions should make the daily planning loop more satisfying. They can solve villager requests directly, create bonuses, support exploration, and eventually affect minigames and area traversal.

| **Potion**            | **Ingredients**               | **Use**                                                    |
|-----------------------|-------------------------------|------------------------------------------------------------|
| Kind Remedy           | Sunmint + Lantern Moss        | Healing, comfort, gentle fixes, good-witch solutions.      |
| Minor Hex             | Thornroot + Grave Soil        | Curses, punishment, intimidation, dark-witch solutions.    |
| Balanced Charm        | Dewberries + Spirit Thread    | Bargains, fair trades, compromise, gray-witch solutions.   |
| Trickster Tonic       | Whisper Mold + Moon Chamomile | Pranks, irony, loopholes, mischief-witch solutions.        |
| River-Calming Draught | River Pearl + Sunmint         | Soothing water, restless sleep, river-whispers.            |
| Moonlit Ward          | Lantern Moss + Moon Chamomile | Protective charms for homes, paths, cradles, and promises. |
| Honeyed Tongue        | Honey Ash + Dewberries        | Bargains, sales, apologies, suspicious proposals.          |
| Spirit Lantern Oil    | Ghostcap + Spirit Thread      | Revealing ghosts, old debts, and half-truths.              |
| Witching Ink          | Whisper Mold + River Pearl    | Rumors, contracts, omens, words that will not stay quiet.  |
| Gravekind Salve       | Bone Dust + Sunmint           | Sorrow, hauntings, and old injuries.                       |

# 8. Familiars

| **Familiar** | **Role**                                          | **Future Expansion**                                                     |
|--------------|---------------------------------------------------|--------------------------------------------------------------------------|
| Black Cat    | Detects lies and softens suspicious villagers.    | Truth-sense, trust recovery, hidden motive clues.                        |
| Raven        | Finds secrets, omens, and graveyard clues.        | Divination upgrades, forest landmark memory, omen translation.           |
| Toad         | Improves brewing and sometimes saves ingredients. | Potion minigame leniency, rare herb identification, cauldron stability.  |
| Bat          | Helps with night gathering and ghosts.            | Well/cave navigation, ghost debt mitigation, nocturnal ingredient bonus. |
| Fox          | Unlocks clever mischief and gray solutions.       | Bargain loopholes, shifting forest tricks, alternate route discovery.    |

# 9. Villagers, Requests, and Relationship Memory

Villagers should become long-running story anchors instead of disposable request generators. Their relationship stats should unlock branch paths and alter how they approach the witch.

| **Relationship Axis** | **Meaning**                                            | **Potential Unlocks**                                    |
|-----------------------|--------------------------------------------------------|----------------------------------------------------------|
| Trust                 | The villager believes the witch means well.            | Personal confessions, gifts, gentler story paths.        |
| Fear                  | The villager believes the witch is dangerous.          | Coercive options, secret resistance, fearful obedience.  |
| Debt                  | The villager owes the witch or the witch has leverage. | Favors, bargains, merchant paths, resentment risk.       |
| Gratitude             | The villager remembers genuine help.                   | Rare rewards, invitations, protective testimony.         |
| Resentment            | The villager feels wronged or used.                    | Rival storylines, sabotage, exile pressure.              |
| Suspicion             | The villager doubts the witch or investigates her.     | Mayor/church opposition, rumor escalation, hidden tests. |

# 10. Living Areas and Playable Locations

The current hub should evolve into a connected set of playable areas. Entering a place should feel like crossing into a distinct mini-level, not merely opening a menu.

| **Area**              | **Long-Term Design**                                                                                                                                 |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Purple House Interior | Playable interior with cauldron room, shop counter, attic mirror, bedroom, familiar nook, basement, journal/memory wall, and visual upgrade changes. |
| Helpful Garden        | Playable garden minigame focused on careful harvesting, glowing herbs, timing, identification, and gentle magical stewardship.                       |
| Poisonous Garden      | Playable garden minigame focused on risky harvests, cursed weeds, hostile plants, rare dangerous ingredients, and power consequences.                |
| Spirit Graveyard      | Playable spirit area with grave-symbol reading, offerings, whispers, safe gathering, ghost bargaining, and debt risk.                                |
| Old Well              | Cinematic well interaction: player looks down into the well; coin toss cuts to camera inside the well looking up as the coin falls.                  |
| Town Square           | Social area for villager arcs, rumor discovery, market pressure, reputation events, and public consequences.                                         |
| Whispering Woods      | Replayable shifting forest minigame where paths and encounters change based on the witch and world state.                                            |
| Lantern Lane          | Neighborhood/social path for quiet relationship scenes, nighttime rumors, and atmospheric world changes.                                             |
| Moonlit Market        | Trading, contracts, merchant witch paths, rare goods, and strange bargain creatures.                                                                 |
| River Steps           | Well/river magic, reflections, lost things, water spirits, alternate-world hints.                                                                    |
| Chapel Ruins          | Curse-breaking, old village history, nature pushback, and moral reckoning.                                                                           |

# 11. Shifting Forest Walk

The forest should become a replayable minigame and one of the primary long-term expression systems. It should feel like the forest has a mind of its own.

- Each visit can rearrange paths, signs, sounds, landmarks, clearings, and encounters.

- The forest reflects the player’s witch flavor, town mood, ghost ledger, and world reverberation level.

- Kindness may create safe paths and glowing herbs; Power may create thorns, wolves, and rare dark shortcuts; Mischief may create loops and trick signs; Spirit magic may create ghost lanterns; Greed may create tempting treasure and debt spirits.

- Forest success can grant ingredients, lore, relationship triggers, and alternate path discoveries. Failure can create lost time, wrong ingredients, ghost debt, injury flavor, or rumors.

# 12. World Reverberation

World Reverberation is the system where magic visibly and narratively changes the world. The village, woods, gardens, graveyard, animals, rumors, and ambient details should respond to the kinds of magic the player repeatedly unleashes.

| **Magic Flavor**   | **Reverberation Signs**                                                                           |
|--------------------|---------------------------------------------------------------------------------------------------|
| Kind / Restorative | Magical fireflies, glowing herbs, warm lanterns, friendly spirits, hopeful dreams.                |
| Dark / Power       | Bats around rooftops, wolf howls, thorn growth, cold moonlight, fearful whispers, moving shadows. |
| Mischief           | Gremlins, goblins, rearranged signs, laughing mushrooms, impossible village rumors.               |
| Spirit             | Ghost lanterns, blue candle flames, grave bells, pale footprints, whispered names.                |
| Greed / Bargain    | Coin-eyed crows, locked doors, gold glints in puddles, debt spirits, contract rumors.             |
| Balance / Gray     | Twin reflections, mirrored flowers, crossroads symbols, neutral spirits, stable omens.            |

# 13. Nature Pushback and Restoring Order

As magical reverberation grows, the natural order should eventually push back. The land is not passive. The more the witch changes the world, the more the world reacts.

- Paths close overnight or trees move to block roads.

- Wells stop reflecting faces correctly.

- Seasons behave strangely.

- Animals avoid certain places or gather in unnatural numbers.

- Spirits become restless.

- The village shares dreams.

- Magic starts answering wishes too literally.

- The forest begins testing the witch.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Central Endgame Question</strong></p>
<p>What should the witch do with the world they have awakened: force the new magical world to stay, restore the old natural order, or bind a balance between old and new?</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 14. Ending Framework

| **Ending Philosophy**         | **Theme**                                                                             | **Typical Outcome**                                                            |
|-------------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Force the New World to Stay   | The old world was small, fearful, and asleep. Let it wake up, even if it grows teeth. | High-magic or domination endings; wonder remains but costs rise.               |
| Restore the Old Natural Order | Wonder is beautiful, but not if it consumes the people who live beside it.            | Low-magic closure endings; peace and safety return but impossible doors close. |
| Bind a Balance                | The world need not be what it was, but it should not belong entirely to the witch.    | Stewardship endings where village, nature, spirits, and magic form a pact.     |

| **Witch Ending**               | **Final Struggle**                                                                                                               |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Beloved Witch                  | Protect everyone forever, teach the village to live responsibly with magic, or seal most magic away.                             |
| Feared Hag                     | Dominate the land, break the curses and lose power, or become the feared guardian who saves the village from worse things.       |
| Gray Witch / Necessary Monster | Enforce a strict pact, let old debts collapse, or become the neutral judge between village, spirits, nature, and magic.          |
| Trickster Witch                | Let the world become wonderfully strange, play one final trick to reset it, or teach chaos rules so it becomes livable.          |
| Merchant Witch                 | Own the magical economy, forgive the debts and lose an empire, or create fair bargain laws.                                      |
| Spirit-Keeper                  | Open the boundary and let spirits remain, close it and say goodbye, or become guardian of the threshold.                         |
| Curse-Breaker                  | Absorb curses, return them to the wild earth, or transform them into protective magic.                                           |
| Exiled Witch                   | Leave the village, save them anyway, or build a new magical domain beyond town.                                                  |
| Witch Queen                    | Conquer the old order, rule as protector instead of tyrant, or step down before power consumes the changed world.                |
| Vanishing House                | Let the house vanish with excess magic, anchor it and change the town, or turn it into a wandering refuge for impossible things. |

# 15. Post-Ending Play and Unrealized Possibilities

Some endings can continue after the ending if enough magic remains in the world. The witch may continue exploring the world they shaped or discover doorways to alternate possibilities.

| **Post-Ending State** | **Meaning**                                                                                                                                                               |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Low Magic             | The world is peaceful, quieter, and safer. Post-game travel is limited or unavailable because the magic that would open deeper doors has been sealed, restored, or spent. |
| Balanced Magic        | The witch can continue stewarding a pact between village, nature, spirits, and magic. Post-game remains grounded in the shaped world.                                     |
| High Magic            | Rifts, portals, wells, mirrors, or the house itself can open to alternate worlds, unrealized choices, and other witch variants.                                           |

Potential doorways include the Attic Divination Mirror, the Old Well, the Purple House itself, rifts in the forest, or familiar-led crossings.

# 16. Low-Magic Ending Echoes

Low-magic endings should be meaningful bittersweet closure endings, not lesser endings. The witch may have restored or quieted the world so thoroughly that the mirror, well, or rift cannot fully open. However, the game should still hint that something more almost existed.

- A faint voice calls from the magic mirror, too thin to understand.

- An alternate witch’s hand touches the glass from the other side, then fades.

- The well reflects the player witch, but not quite: different hat, expression, or familiar.

- A coin hangs in darkness before vanishing without a splash.

- The Purple House creaks as if an unseen door opened somewhere inside.

- Fireflies form a doorway, then scatter before it opens.

- The final journal page writes one extra line by itself: “There was another path, once.”

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Low-Magic Design Rule</strong></p>
<p>Peace and safety were gained, but the impossible was closed off. This creates a replay hook without undermining closure.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 17. Village Scale, Cast, and Cutscene Direction

The finished game should grow beyond a small request roster into a fully mapped, explorable village with a large recurring cast. The content plan should support up to roughly 100 individual villagers over the life of the project, while keeping the first production milestones focused on a smaller set of deeply developed anchor characters.

| **Content Goal**    | **Direction**                                                                                                                                      |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Village map         | Eventually replace abstract destination menus with a coherent, fully mapped explorable village and connected wilderness areas.                     |
| Villager population | Long-term target of up to about 100 individual villagers, introduced in manageable districts, families, professions, factions, and story clusters. |
| Anchor characters   | Prioritize a smaller core cast with deep multi-step arcs before expanding the total population.                                                    |
| Story presentation  | Every Recent Story entry should eventually have an associated cutscene, vignette, illustrated moment, or in-world staged scene.                    |
| Replay structure    | Different relationship branches and witch flavors should reveal different subsets of the village and its stories across playthroughs.              |

Current named villager foundation: Mara the Baker, Old Bram, Lina the Tailor, Mayor Puddlewick, Tessa the Widow, Nib the Goat-Herder, Orin the Clerk, Pippa from the Lane, Sable the Chandler, Edwin the Ferryman, Violet the Schoolmistress, Rowan the Gravedigger, Juniper the Midwife, Corvin the Peddler, Hetty the Beekeeper, and Moss the Archivist.

# 18. Content Pillars for Future Production

- Every new area should provide gameplay, story, and world-state feedback.

- Every relationship should be capable of becoming a multi-step story path.

- Every moral tendency should eventually have visual, audio, rumor, and ending consequences.

- Every familiar should matter in at least one area, one minigame, and one story context.

- Every ending should answer the same core question through a different witch flavor.

# 19. Non-Goals / Guardrails

- Do not turn the tone into horror. Spooky-cute, haunted, and morally weighty are allowed; jump-scare horror is not the target.

- Do not make morality a simple good/evil meter. Use flavor, consequence, relationships, and world change.

- Do not let menus replace the long-term plan for playable places. Menus can prototype systems, but the destination is explorable areas.

- Do not make post-ending multiverse content available for every ending; access should depend on how much magic remains.

*End of Game Bible*
