#!/usr/bin/env python3
"""Generate Minimal Mistakes encyclopedia pages from structured data."""

from pathlib import Path

from extra_entries import write_extra_characters, write_extra_locations, write_extra_events

ROOT = Path(__file__).resolve().parents[1]


def md(collection, slug, title, excerpt, tags, epithet, era, overview, typ, origins, affiliations, role, history, connections, legacy):
    tags_yaml = "\n".join(f"  - {t}" for t in tags)
    hist = "\n".join(history)
    conn = "\n".join(
        f"- **[{name}]({{{{ '{url}' | relative_url }}}}):** {note}"
        for name, url, note in connections
    )
    excerpt_q = excerpt.replace('"', '\\"')
    body = f"""---
title: "{title}"
excerpt: "{excerpt_q}"
tags:
{tags_yaml}
---

*{epithet}* · {era}

## Overview & Essence

{overview}

## Key Characteristics & Attributes

- **Type/Category:** {typ}
- **Origins/Creation:** {origins}
- **Key Affiliations/Associations:** {affiliations}
- **Primary Role/Purpose:** {role}

## Detailed History & Narrative Arc

{hist}

## Notable Connections & Relationships

{conn}

## Legacy & Significance

{legacy}
"""
    out = ROOT / f"_{collection}" / f"{slug}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")


def main():
    C, L, E, P = "/characters", "/locations", "/events", "/people"

    # --- Characters ---
    md("characters", "frodo-baggins", "Frodo Baggins",
       "A hobbit of the Shire who inherits the One Ring and bears it to Mordor, where it is destroyed at the cost of wounds that do not fully heal in Middle-earth.",
       ["hobbit", "fellowship", "ring-bearer"], "Ring-bearer of the Shire", "Third Age",
       "Frodo Baggins is a Hobbit of Bag End, heir of Bilbo Baggins, and the principal Ring-bearer of the War of the Ring. In Tolkien’s legendarium he is charged with taking the One Ring to Orodruin so that it can be unmade. His significance lies less in martial prowess than in endurance, pity, and the decision to carry a burden that magnifies the will to dominate.",
       "Character (Hobbit)",
       "Born in the Shire in T.A. 2968; orphaned young and adopted by Bilbo Baggins of Bag End.",
       "The Shire; Bilbo; Samwise Gamgee; the Fellowship of the Ring; Gandalf; Gollum; the One Ring.",
       "To remove the Ring from the Shire and convey it to the only fire in which it can be destroyed.",
       [
           "- **Inheritance and departure.** Frodo inherits Bag End and, unknown to him at first, the One Ring. After Gandalf confirms its identity, he leaves the Shire with Sam, Merry, and Pippin rather than let the hunt of the Nazgûl fall on his homeland.",
           "- **The Road and Rivendell.** Wounded by the Witch-king on Weathertop, he is brought to Rivendell. At the Council of Elrond he offers to take the Ring to Mordor; the Fellowship is formed around that choice.",
           "- **The breaking and the East.** After Moria and Lothlórien, Boromir’s attempt to seize the Ring drives Frodo to continue with Sam alone. Gollum is bound as a guide. At Cirith Ungol Frodo is stung by Shelob and captured; Sam recovers him.",
           "- **Mount Doom and after.** At the Crack of Doom Frodo claims the Ring. Gollum seizes it and falls, completing the Quest. Honored in Gondor and the Shire, Frodo does not recover from wound, sting, and the Ring’s burden; in T.A. 3021 he sails West from the Grey Havens.",
       ],
       [
           ("Samwise Gamgee", f"{C}/samwise-gamgee/", "Gardener and companion who keeps the Quest alive when Frodo’s strength fails."),
           ("Gollum", f"{C}/gollum/", "Former bearer and guide whose last seizure of the Ring unmakes it."),
           ("The One Ring", f"{P}/one-ring/", "The artefact Frodo inherits, bears, and cannot willingly cast away at the end."),
           ("The Shire", f"{L}/the-shire/", "Homeland he leaves to save and cannot fully re-enter in spirit."),
           ("Mount Doom", f"{L}/mount-doom/", "Place of the Ring’s forging and destruction."),
       ],
       "Frodo’s story is the narrative spine of *The Lord of the Rings*. Canonically, the Quest succeeds through pity shown to Gollum as much as through Frodo’s own will. He is remembered in-universe as a Ring-bearer granted passage into the West, and in the framing device as the author of much of the Red Book’s account of the War.")

    md("characters", "samwise-gamgee", "Samwise Gamgee",
       "Frodo’s gardener and closest companion, whose loyalty and practical courage sustain the Quest through Cirith Ungol and Mordor.",
       ["hobbit", "fellowship"], "Gardener of Bag End", "Third Age",
       "Samwise Gamgee is a Hobbit of Hobbiton, son of Hamfast Gamgee, and Frodo’s servant and friend. He is the only companion who remains with Frodo all the way into Mordor. Within the legendarium he embodies steadfast loyalty and a love of growing things set against Sauron’s barren will.",
       "Character (Hobbit)",
       "Born in the Shire in T.A. 2980; raised in a working family of gardeners attached to Bag End.",
       "Frodo Baggins; the Fellowship; Rosie Cotton; the Shire; briefly the One Ring.",
       "To accompany and protect the Ring-bearer, including bearing the Ring for a short time without claiming lordship.",
       [
           "- **From garden to Road.** Overhearing Gandalf, Sam is set as Frodo’s companion. He leaves with packs, cooking gear, and Elven rope as seriously as others bear swords.",
           "- **Cirith Ungol and Mordor.** He fights Shelob, believes Frodo dead, takes the Ring to keep it from Sauron’s servants, then rescues Frodo from the Tower of Cirith Ungol. In Mordor he shares the last of their food and hope.",
           "- **Return.** After the War he marries Rosie Cotton, helps restore the Shire, and becomes Mayor. Late in life he is said to have sailed West, an honor rarely given to one who was not a long-term Ring-bearer in the same sense as Frodo.",
       ],
       [
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Master and friend; Sam’s primary loyalty."),
           ("The Shire", f"{L}/the-shire/", "Home he leaves and later helps heal."),
           ("Cirith Ungol", f"{L}/cirith-ungol/", "Pass where he fights Shelob and recovers Frodo."),
           ("Gollum", f"{C}/gollum/", "Rival for the Ring and uneasy fellow-traveler."),
       ],
       "In the book, Sam is indispensable to the Quest’s completion. His brief possession of the Ring shows that even a Hobbit can feel its lure, yet he surrenders it back to Frodo. His later life in the Shire is the canon’s image of victory as planting and ordinary peace.")

    md("characters", "aragorn", "Aragorn",
       "Chieftain of the Dúnedain of the North who, after decades in exile, claims the thrones of Arnor and Gondor as King Elessar at the end of the Third Age.",
       ["man", "dunadan", "fellowship", "king"], "Heir of Isildur, King Elessar", "Third Age",
       "Aragorn II is a Man of the Dúnedain, heir of Isildur, known in the wild as Strider and later crowned King Elessar Telcontar. He is a Ranger, captain, and healer whose return closes the long vacancy of Gondor’s throne. His significance is the restoration of the united kingdoms of the Dúnedain after the War of the Ring.",
       "Character (Man; Dúnadan)",
       "Born T.A. 2931; raised in Rivendell under the name Estel after his father’s death.",
       "Arwen Undómiel; Elrond; the Rangers of the North; the Fellowship; Rohan; Gondor; Andúril (Narsil reforged).",
       "To contest Sauron as Isildur’s heir, aid the Ring-bearer, and restore the kingship of Arnor and Gondor.",
       [
           "- **Exile and service.** He serves in Rohan and Gondor under other names, then as Strider in Eriador, guarding the Shire’s borders without the Hobbits’ knowledge.",
           "- **War of the Ring.** He joins the Fellowship at Rivendell. After its breaking he hunts Merry and Pippin’s captors, fights at Helm’s Deep, walks the Paths of the Dead, and arrives at the Pelennor in the captured Corsair fleet. He leads the host to the Black Gate as a diversion.",
           "- **Kingship.** Crowned in Minas Tirith, he marries Arwen, restores the North-kingdom in measure, and rules into the Fourth Age. The palantír of Orthanc and the healing of the wounded (including Faramir, Éowyn, and Merry) belong to this same royal office in the book.",
       ],
       [
           ("Arwen Undómiel", f"{C}/arwen/", "Evenstar of her people; his wife, who chooses a mortal life."),
           ("Rivendell", f"{L}/rivendell/", "Foster-home and place where Narsil’s shards were kept."),
           ("Gondor", f"{L}/gondor/", "South-kingdom he claims as king."),
           ("The Paths of the Dead", f"{E}/paths-of-the-dead/", "Road by which he summons the oath-breakers."),
       ],
       "Aragorn’s reign marks the start of the Fourth Age of Men in the West. Tolkien presents his kingship as earned through long service rather than seized at the first opportunity. Andúril, the Sword-that-was-Broken reforged, is the visible token of that claim.")

    md("characters", "gandalf", "Gandalf",
       "An Istar sent to contest Sauron by counsel; he dies fighting the Balrog in Moria and returns as Gandalf the White to lead the resistance in the West.",
       ["maia", "wizard", "fellowship"], "Mithrandir; Grey, then White", "Third Age",
       "Gandalf is one of the Istari (Wizards), a Maia in mortal form, known to Elves as Mithrandir. He is the principal counsellor of the Free Peoples in the War of the Ring. After his fall in Moria he is sent back with greater authority as Gandalf the White, replacing Saruman as head of the Order in function if not in Saruman’s own conceit.",
       "Character (Maia / Istar)",
       "Came to Middle-earth about T.A. 1000 with the other Istari; Círdan gave him Narya, the Ring of Fire.",
       "The Istari; the White Council; Frodo and the Shire; the Fellowship; Rohan; Gondor; eagles as occasional allies.",
       "To kindle resistance to Sauron without dominating the peoples of Middle-earth by force of his native power.",
       [
           "- **Investigation of the Ring.** He identifies Bilbo’s ring as the One, urges Frodo to leave, and is delayed by Saruman’s imprisonment in Orthanc (book: he escapes with Gwaihir’s aid after the palantír confrontation’s prelude at Isengard).",
           "- **Fellowship and Moria.** He leads the company until the Bridge of Khazad-dûm, where he falls with Durin’s Bane.",
           "- **The White.** Returning, he heals Théoden, directs the defence of the West, and organizes the march to the Morannon to draw Sauron’s eye from Orodruin. At the end of the Third Age his task is complete and he sails West.",
       ],
       [
           ("Saruman", f"{C}/saruman/", "Fellow Istar who falls into rivalry with Sauron and is broken."),
           ("Moria", f"{L}/moria/", "Place of his death and of the Balrog-fight."),
           ("The Shire", f"{L}/the-shire/", "Region he long watched and whose Hobbits he trusts."),
           ("The Istari", f"{P}/istari/", "The order of Wizards to which he belongs."),
       ],
       "Gandalf is the legendarium’s model of limited, lawful intervention: power used to advise and hearten rather than to rule. His return as the White is canonical in *The Two Towers*. Narya’s association with him is attested in the wider legendarium (e.g. the appendices and related texts).")

    md("characters", "legolas", "Legolas",
       "An Elf of the Woodland Realm who joins the Fellowship; his friendship with Gimli is a notable reconciliation of Elf and Dwarf in the Third Age.",
       ["elf", "fellowship"], "Prince of the Woodland Realm", "Third Age",
       "Legolas is a Sindarin Elf of Mirkwood, son of Thranduil. He comes to Rivendell with news of Gollum’s escape and leaves as one of the Nine Walkers. He is a bowman and scout whose later friendship with Gimli is treated as exceptional in the history of the two kindreds.",
       "Character (Elf)",
       "Born in the Woodland Realm of Mirkwood in the Third Age (exact date not given in the main narrative).",
       "Thranduil’s people; the Fellowship; Gimli; later Ithilien.",
       "To represent the Elves in the Fellowship and to contest Sauron’s war in the North and South as it unfolds.",
       [
           "- **Fellowship.** He travels the Road, Moria, Lothlórien, and the Anduin with the company. After the breaking he accompanies Aragorn and Gimli in the hunt and the war in Rohan and Gondor.",
           "- **After the War.** He brings Elven settlers to Ithilien. In time he builds a ship and sails West, taking Gimli with him—an ending stated in the appendices, rare for a Dwarf.",
       ],
       [
           ("Gimli", f"{C}/gimli/", "Dwarf companion who becomes his closest friend among the Fellowship."),
           ("Mirkwood", f"{L}/mirkwood/", "His home forest, darkened by Dol Guldur."),
           ("The Fellowship of the Ring", f"{E}/fellowship-of-the-ring/", "The company he joins in Rivendell."),
       ],
       "Legolas’s canon role is martial and companionate rather than political. The book does not send a Lórien army to Helm’s Deep; Legolas fights there as one of the Three Hunters. His sailing with Gimli is appendix-canon, not a film invention.")

    md("characters", "gimli", "Gimli",
       "A Dwarf of Erebor who joins the Fellowship, fights in Rohan and Gondor, and becomes an Elf-friend through Galadriel and Legolas.",
       ["dwarf", "fellowship"], "Son of Glóin", "Third Age",
       "Gimli is a Dwarf of Durin’s Folk, son of Glóin of Erebor. He represents his people at the Council of Elrond and in the Fellowship. He is a warrior of the axe whose reverence for Galadriel and friendship with Legolas mark a late healing of older grudges.",
       "Character (Dwarf)",
       "Born in the Third Age among Durin’s Folk; his father Glóin was one of Thorin’s companions in *The Hobbit*.",
       "Erebor; the Fellowship; Legolas; Galadriel; later the Glittering Caves of Aglarond.",
       "To aid the Quest and, after the War, to found a Dwarf colony in the caves behind Helm’s Deep.",
       [
           "- **Moria and Lórien.** He enters Khazad-dûm with hope and leaves with grief. In Lothlórien he asks a hair of Galadriel and receives three, a gift with First Age echoes (compare Fëanor’s request, which she refused).",
           "- **War.** He fights at the Hornburg and on the Pelennor, keeping a grim count of foes with Legolas.",
           "- **Fourth Age.** He becomes Lord of the Glittering Caves. The appendices record that he sailed West with Legolas.",
       ],
       [
           ("Legolas", f"{C}/legolas/", "Elf of Mirkwood; later inseparable companion."),
           ("Moria", f"{L}/moria/", "Ancestral mansion seen as a tomb in the late Third Age."),
           ("Lothlórien", f"{L}/lothlorien/", "Where Galadriel’s gift changes his view of Elves."),
           ("Helm’s Deep", f"{L}/helms-deep/", "Battle and later site of his colony at Aglarond."),
       ],
       "Gimli is the Dwarves’ chief face in the War of the Ring. His story in the book stays with the Three Hunters after Parth Galen; it does not follow a separate northern plot except by implication of Erebor’s own war, mentioned in the appendices.")

    md("characters", "boromir", "Boromir",
       "Heir of Denethor and captain of Gondor whose desire to use the Ring as a weapon breaks the Fellowship, and whose last stand for Merry and Pippin restores his honor.",
       ["man", "gondor", "fellowship"], "Captain of Gondor", "Third Age",
       "Boromir is a Man of Gondor, elder son of Steward Denethor II. He comes to Rivendell seeking interpretation of a prophetic dream and leaves as a member of the Fellowship. He is brave and open-handed, but the Ring exploits his fear for Minas Tirith. His death at Amon Hen is the Fellowship’s first irreversible loss among the Walkers.",
       "Character (Man of Gondor)",
       "Born in Minas Tirith; raised as heir to the Stewardship in a city long at war.",
       "Denethor; Faramir; Gondor; the Fellowship; the One Ring as temptation.",
       "To obtain aid for Gondor; he argues for using the Ring as a weapon and fails that test.",
       [
           "- **Council.** He reports the dream of Imladris and the Sword that was Broken, and doubts the plan of destruction.",
           "- **Parth Galen.** He tries to take the Ring from Frodo, then repents. Orcs attack; he dies defending Merry and Pippin. Aragorn, Legolas, and Gimli give him a boat-burial on the Anduin.",
       ],
       [
           ("Faramir", f"{C}/faramir/", "Younger brother who later rejects the Ring when he has the chance to seize it."),
           ("Gondor", f"{L}/gondor/", "The realm whose peril shapes his judgment."),
           ("The Breaking of the Fellowship", f"{E}/breaking-of-the-fellowship/", "The hour of his fall and death."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Ring-bearer he assaults, then dies trying to amend."),
       ],
       "Boromir’s arc is a canonical warning: love of a city can be twisted into a claim on the Ring. The book treats his last fight as a recovery of honor, not as erasure of the attempt on Frodo.")

    md("characters", "meriadoc-brandybuck", "Meriadoc Brandybuck",
       "A Hobbit of Buckland who rides to war with Rohan and, with Éowyn, brings down the Witch-king on the Pelennor Fields.",
       ["hobbit", "fellowship"], "Merry of Buckland", "Third Age",
       "Meriadoc Brandybuck is a Hobbit of Brandy Hall, cousin and friend of Frodo. He is one of the four Hobbits of the Fellowship. His decisive canonical act in the War is the blow that helps slay the Witch-king, in fulfilment of Glorfindel’s prophecy that the wraith-lord would not fall by the hand of man.",
       "Character (Hobbit)",
       "Born in Buckland in the Shire’s Eastfarthing march; a Brandybuck of the leading family there.",
       "Pippin; Frodo; the Fellowship; Théoden and Éowyn; Rohan.",
       "Companion on the Quest; later esquire of Rohan and a principal actor on the Pelennor.",
       [
           "- **Conspiracy and capture.** Merry helps Frodo leave the Shire, is taken by Uruk-hai after Parth Galen, and escapes into Fangorn with Pippin.",
           "- **Rohan.** He swears service to Théoden. Forbidden the ride to Minas Tirith, he goes nonetheless as Dernhelm’s passenger (Éowyn in disguise).",
           "- **Pelennor and after.** He stabs the Witch-king behind the knee; Éowyn kills the wraith. After the War he is Master of Buckland and a writer of herblore in the Red Book tradition.",
       ],
       [
           ("Peregrin Took", f"{C}/peregrin-took/", "Closest friend among the four; fellow captive of the Uruk-hai."),
           ("Éowyn", f"{C}/eowyn/", "Shieldmaiden with whom he slays the Witch-king."),
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Field of his most famous deed."),
           ("Rohan", f"{L}/rohan/", "Kingdom he serves as esquire."),
       ],
       "Merry’s role shows that the prophecy about the Witch-king is fulfilled without contradiction: no *man* slays him. The book, not the films, is the source for Merry’s wound by the Black Breath and his healing in Minas Tirith.")

    md("characters", "peregrin-took", "Peregrin Took",
       "The youngest of the four Hobbits; his palantír-glance draws Sauron’s attention, and his warning saves Faramir from Denethor’s pyre.",
       ["hobbit", "fellowship"], "Pippin, Guard of the Citadel", "Third Age",
       "Peregrin Took is a Hobbit of the Took family, Thain’s line, and the youngest of the four Travellers. Recklessness and growth define his arc: a stone dropped in Moria has consequences; service in Gondor has more. He is canonically a Guard of the Citadel and later Thain of the Shire.",
       "Character (Hobbit)",
       "Born in the Shire in T.A. 2990; a Took of Great Smials.",
       "Merry; Frodo; Treebeard; Denethor; Gondor; the Fellowship.",
       "Companion on the Quest; later a soldier of Gondor whose actions affect both palantír-war and the Steward’s last hours.",
       [
           "- **Moria to Fangorn.** His well-stone in Moria alerts foes. Captured with Merry, he meets Treebeard; the Ents’ march on Isengard follows their news.",
           "- **Palantír.** He looks into the Orthanc-stone; Sauron misreads the sight. Gandalf takes him to Minas Tirith.",
           "- **Gondor.** He swears to Denethor, then fetches Gandalf when the Steward would burn Faramir. He fights at the Black Gate and returns a figure of note in the Shire’s later years.",
       ],
       [
           ("Meriadoc Brandybuck", f"{C}/meriadoc-brandybuck/", "Fellow conspirator, captive, and friend."),
           ("Denethor II", f"{C}/denethor/", "Steward he serves and whose despair he interrupts."),
           ("Minas Tirith", f"{L}/minas-tirith/", "City of his service."),
           ("Treebeard", f"{C}/treebeard/", "Ent who takes in the two Hobbits."),
       ],
       "Pippin’s canon function includes the palantír incident (book: he, not Aragorn, first uses the recovered stone) and the saving of Faramir. Both are structurally important to the War’s last days.")

    md("characters", "gollum", "Gollum",
       "Once Sméagol of hobbit-kind, twisted by centuries with the Ring; he guides Frodo toward Mordor and, seizing the Ring at the Crack of Doom, falls with it into the fire.",
       ["stoor", "ring"], "Sméagol; the Trailer", "Third Age",
       "Gollum is a creature formerly named Sméagol, of Stoor Hobbit-kind, who murdered Déagol for the One Ring and fled into the Misty Mountains. The Ring lengthens his life and splits his personality. He is both traitor and, unintentionally, the agent of the Ring’s destruction.",
       "Character (Stoor / Ring-victim)",
       "A Stoor of the Gladden Fields region in the early Third Age; the Ring came to him c. T.A. 2463 after Isildur’s loss.",
       "The One Ring; Frodo and Sam; Shelob; Sauron’s earlier hunt for “Baggins.”",
       "To recover the Precious; the narrative uses him as guide, tempter, and the hand that takes the Ring into the fire.",
       [
           "- **The murder and the dark.** He kills Déagol, is driven out, and lives under the Mountains until Bilbo takes the Ring (T.A. 2941).",
           "- **Hunt and capture.** He leaves the Mountains, is captured in Mordor, and later held by Thranduil; he escapes, which Legolas reports at Rivendell.",
           "- **Guide and betrayal.** Oath-bound to Frodo, he leads the Hobbits through the Dead Marshes and Ithilien. On the stairs of Cirith Ungol he betrays them to Shelob.",
           "- **Orodruin.** He attacks at the Crack of Doom, bites the Ring from Frodo’s hand, and falls. The book frames this as the consequence of earlier mercy, not as Gollum’s repentance.",
       ],
       [
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Bearer he serves, hates, and finally robs."),
           ("The One Ring", f"{P}/one-ring/", "Object of his identity and desire."),
           ("Mount Doom", f"{L}/mount-doom/", "Place of his death and the Ring’s unmaking."),
           ("Bilbo Baggins", f"{C}/bilbo-baggins/", "Who took the Ring in the dark and spared his life."),
       ],
       "Gollum is central to Tolkien’s theme of pity. Bilbo’s and Frodo’s refusals to kill him leave him alive to complete what the Ring-bearer cannot do at the end. That reading is explicit in the book’s moral structure.")

    md("characters", "galadriel", "Galadriel",
       "Noldorin lady of Lothlórien who refuses the One Ring when Frodo offers it, passing the last test of her long exile in Middle-earth.",
       ["elf", "noldor", "ring-bearer"], "Lady of Lothlórien", "First Age to Third Age",
       "Galadriel is one of the greatest of the Noldor remaining in Middle-earth in the Third Age, wife of Celeborn and keeper of Nenya, the Ring of Water. She tests the Fellowship in Lothlórien and refuses the One Ring. Her departure over Sea after Sauron’s fall marks the fading of Lórien’s preserved spring.",
       "Character (Elf; Noldo)",
       "Born in Valinor in the Years of the Trees; came to Middle-earth in the rebellion of the Noldor (wider legendarium; *The Lord of the Rings* treats her as ancient and powerful without rehearsing every First Age episode).",
       "Celeborn; Lothlórien; Elrond and the White Council; Nenya; the Fellowship as guests.",
       "To preserve a realm against the Shadow and to resist the temptation of the One Ring.",
       [
           "- **Lórien.** She shelters the Fellowship after Moria, shows visions in her Mirror, and gives gifts that later matter (cloaks, lembas, the Phial for Frodo).",
           "- **The test.** When Frodo offers her the Ring, she speaks the temptation and refuses, accepting diminution rather than a tyrannical queenship.",
           "- **Departure.** With the One destroyed, the Three lose their power to preserve. She sails from the Grey Havens with the other Ring-bearers of the Third Age’s end.",
       ],
       [
           ("Lothlórien", f"{L}/lothlorien/", "The Golden Wood held by her power and Celeborn’s rule."),
           ("Elrond", f"{C}/elrond/", "Kinsman and fellow-keeper of one of the Three."),
           ("Celeborn", f"{C}/celeborn/", "Her husband and co-lord of the Wood."),
           ("The One Ring", f"{P}/one-ring/", "Offered to her; she will not take it."),
       ],
       "Galadriel’s refusal is a canonical climax of *The Fellowship of the Ring*. Film expansions of her wars and a green, watery ‘dark Galadriel’ vision are adaptations; the book’s test is spoken in her own voice in Lórien.")

    md("characters", "elrond", "Elrond",
       "Half-elven lord of Rivendell who chose the kindred of the Eldar, kept Vilya, and hosted the Council that launched the Quest of Mount Doom.",
       ["half-elven", "ring-bearer"], "Master of Rivendell", "First Age to Third Age",
       "Elrond Half-elven is lord of Imladris, brother of Elros (first king of Númenor), and bearer of Vilya. He is a healer, lore-master, and political host rather than a field-king in the War of the Ring. The Council of Elrond is his great act in that war: a place where the Free Peoples choose destruction of the Ring over use or hiding.",
       "Character (Half-elven)",
       "Born at the end of the First Age; after the War of Wrath he chose to be counted among Elves. Founded Rivendell in the Second Age.",
       "Rivendell; Arwen; Aragorn (as foster-son); Gil-galad in the Last Alliance; Vilya; the White Council.",
       "To preserve memory and refuge, and to counsel the Quest without claiming the Ring.",
       [
           "- **Last Alliance.** He was Gil-galad’s herald; he later recounts Isildur’s refusal to destroy the Ring.",
           "- **Third Age.** He raises Aragorn, keeps the shards of Narsil, and calls the Council in T.A. 3018.",
           "- **Departure.** At the end of the Age he sails West; Arwen remains, having chosen a mortal life.",
       ],
       [
           ("Rivendell", f"{L}/rivendell/", "His hidden valley and house of healing."),
           ("Arwen Undómiel", f"{C}/arwen/", "Daughter who does not take ship with him."),
           ("The Council of Elrond", f"{E}/council-of-elrond/", "Gathering he convenes."),
           ("Aragorn", f"{C}/aragorn/", "Estel, fostered in his house."),
       ],
       "Elrond represents continuity from the First Age into the Fourth. His choice of the Eldar and Arwen’s opposite choice are both canonical. He does not go to war in the South in *The Lord of the Rings* itself.")

    md("characters", "arwen", "Arwen Undómiel",
       "Daughter of Elrond who chooses a mortal life with Aragorn, binding the fading of the Elves to the renewal of the Dúnedain kingdoms.",
       ["half-elven"], "Evenstar of her people", "Third Age",
       "Arwen Undómiel is the daughter of Elrond and Celebrían, called Evenstar. In the book she is largely off-stage during the War: her choice, modelled on Lúthien’s, is to become mortal and marry Aragorn. She rides to Minas Tirith after the victory for her wedding.",
       "Character (Half-elven)",
       "Born in the Third Age in Rivendell (and associated also with Lórien, where she spent time with Galadriel).",
       "Elrond; Aragorn; Rivendell; later the court of Gondor.",
       "To wed the restored king and accept the Gift of Men, leaving the Elven fate of her father.",
       [
           "- **The choice.** As Half-elven in Elrond’s line, her fate is tied to that choice. She waits in Rivendell while Aragorn walks the wild.",
           "- **After the War.** She marries Aragorn in Minas Tirith. The appendices record her later death in Lórien after his passing.",
       ],
       [
           ("Aragorn", f"{C}/aragorn/", "Husband and King Elessar."),
           ("Elrond", f"{C}/elrond/", "Father who sails without her."),
           ("Rivendell", f"{L}/rivendell/", "Home of her youth."),
           ("Minas Tirith", f"{L}/minas-tirith/", "City of her marriage."),
       ],
       "The book does not place Arwen at Helm’s Deep or on the Pelennor; those are film additions. Her canonical importance is dynastic and thematic: the joining of Elven and human lines at the opening of the Fourth Age.")

    md("characters", "sauron", "Sauron",
       "A Maia of Aulë’s people who became Morgoth’s lieutenant, forged the One Ring, and spent the Third Age as a returning Dark Lord until the Ring’s destruction unmade his power.",
       ["maia", "dark-lord"], "The Dark Lord of Mordor", "Second Age to Third Age",
       "Sauron is a Maia, originally of Aulë’s following, who served Melkor/Morgoth and later sought dominion in his own right. He forged the One Ring to rule the other Rings of Power. In the Third Age he is the Necromancer of Dol Guldur and then the Lidless Eye of Barad-dûr—will and surveillance more than a walking tyrant on the battlefield of *The Lord of the Rings*.",
       "Character (Maia; Dark Lord)",
       "Ainur of the world’s making; corrupted in the deep past; master of Mordor in the Second Age after Númenor’s fall destroyed his fair form.",
       "The One Ring; Mordor; the Nazgûl; Orcs and subject nations; formerly Annatar in Eregion.",
       "To order Middle-earth by owning it, especially through the Rings and through war.",
       [
           "- **Second Age.** As Annatar he taught ring-craft; he made the One in Orodruin. He was taken to Númenor, corrupted it, and went down in its ruin, thereafter unable to appear fair. The Last Alliance overthrew him; Isildur took the Ring.",
           "- **Third Age.** He rebuilt in secret, was driven from Dol Guldur, and returned openly to Mordor. He could not imagine that his enemies would try to destroy the Ring rather than use it.",
           "- **Fall.** When the Ring is unmade, the greater part of his native power, invested in it, is lost; Barad-dûr collapses and he is reduced to an impotent shadow.",
       ],
       [
           ("The One Ring", f"{P}/one-ring/", "Repository of much of his power and the key to his return."),
           ("Mordor", f"{L}/mordor/", "His fenced realm."),
           ("Barad-dûr", f"{L}/barad-dur/", "The Dark Tower, bound to the Ring’s existence."),
           ("The Nazgûl", f"{P}/nazgul/", "Enslaved kings, his chief servants."),
       ],
       "Sauron’s defeat is the end of the Third Age’s defining evil. Tolkien’s text distinguishes him from Morgoth: Sauron is a tyrant of order and knowledge, not a nihilist of the same scale. He does not appear as a duelling figure in the War of the Ring’s last battle.")

    md("characters", "saruman", "Saruman",
       "Chief of the Istari who studies the Enemy in order to rival him, turning Isengard into a war-industry and his voice into a weapon, and who dies in the Shire after his staff is broken.",
       ["maia", "wizard"], "Curunír of Isengard", "Third Age",
       "Saruman the White is an Istar, head of the Order and of the White Council, who falls through pride and ring-lore. He occupies Orthanc, breeds armies, and bargains with Mordor. After the Ents break Isengard, Gandalf casts him from the Order. In the book he dies at Bag End during the Scouring of the Shire, killed by Gríma Wormtongue.",
       "Character (Maia / Istar)",
       "Came to Middle-earth with the Istari; settled at Isengard with Gondor’s leave.",
       "Isengard; Orthanc; the palantír; Wormtongue; the White Council (formerly); ruffians in the Shire.",
       "Originally to contest Sauron by counsel; later to obtain the Ring or a counterfeit power of his own.",
       [
           "- **Fall.** Study of ring-lore and use of the palantír align him with Sauron’s pressure. He imprisons Gandalf and makes war on Rohan.",
           "- **Defeat.** Ents flood Isengard; Théoden’s host and Gandalf confront him at Orthanc; his staff is broken.",
           "- **Sharkey.** He goes west and industrializes the Shire in petty tyranny. After the Battle of Bywater he is killed by Wormtongue on the doorstep of Bag End (book canon; the theatrical film omits this, though the extended edition restores a related death at Orthanc).",
       ],
       [
           ("Isengard", f"{L}/isengard/", "His fortress-vale, unmade by Ents."),
           ("Treebeard", f"{C}/treebeard/", "Ent who besieges him."),
           ("Gandalf", f"{C}/gandalf/", "Who breaks his staff and takes his office in the West’s war."),
           ("The Scouring of the Shire", f"{E}/scouring-of-the-shire/", "His last, diminished kingdom."),
       ],
       "Saruman illustrates the Istari’s charter broken: domination instead of encouragement. The Scouring is canonical in the novel and thematically closes the War at home.")

    md("characters", "eowyn", "Éowyn",
       "Shieldmaiden of Rohan who rides to Minas Tirith in disguise and slays the Witch-king, then chooses a living future with Faramir rather than a sought-for death in battle.",
       ["human", "rohan"], "Shieldmaiden of Rohan", "Third Age",
       "Éowyn is a woman of the House of Eorl, sister of Éomer and niece of King Théoden. Confined by duty and by Wormtongue’s influence at Edoras, she seeks the honour of arms. On the Pelennor she reveals herself and, with Merry, destroys the Lord of the Nazgûl. In the Houses of Healing she turns from despair toward marriage with Faramir and a life in Ithilien.",
       "Character (Woman of Rohan)",
       "Born in Rohan; raised in the king’s household as the realm declines under Gríma’s counsel.",
       "Théoden; Éomer; Merry; Faramir; Rohan; later Ithilien.",
       "To fight for the Mark; she also fulfils, with Merry, the doom of the Witch-king.",
       [
           "- **Edoras.** She is left in charge when the king rides, then disguises herself as Dernhelm.",
           "- **Pelennor.** She defends the fallen Théoden, answers the Witch-king’s boast, and slays him after Merry’s stroke.",
           "- **Healing.** Recovered from the Black Breath, she chooses Faramir and the restoration of Ithilien over a death-wish.",
       ],
       [
           ("Théoden", f"{C}/theoden/", "Uncle and king whose fall she avenges in part."),
           ("Meriadoc Brandybuck", f"{C}/meriadoc-brandybuck/", "Hobbit who strikes the Witch-king with her."),
           ("Faramir", f"{C}/faramir/", "Steward-prince she marries."),
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Field of her victory."),
       ],
       "Éowyn’s slaying of the Witch-king is book-canon and turns on the word *man* in the prophecy. Her healing with Faramir is likewise canonical, not a film-only romance plot.")

    md("characters", "theoden", "Théoden",
       "King of Rohan who is aged and bent by Wormtongue’s counsel until Gandalf restores him; he dies in splendor on the Pelennor Fields.",
       ["human", "rohan", "king"], "King of the Mark", "Third Age",
       "Théoden Ednew is King of Rohan in the War of the Ring. Under Gríma Wormtongue he is enfeebled; Gandalf’s coming returns him to command. He holds Helm’s Deep, answers Gondor’s need, and is killed by the Witch-king’s beast in the charge of the Rohirrim.",
       "Character (Man of Rohan; King)",
       "Born to the royal house of the Mark; king in the late Third Age during Saruman’s and Sauron’s wars.",
       "Éowyn; Éomer; Rohan; Gandalf; Gondor as ally.",
       "To lead the Riders in defence of the Mark and in aid of Minas Tirith.",
       [
           "- **The hall.** Wormtongue’s policy isolates him. Gandalf exposes Gríma; Théoden arms and rides.",
           "- **Helm’s Deep.** He withstands Saruman’s host until dawn and reinforcements.",
           "- **Pelennor.** He leads the charge that breaks the first terror of the siege and dies under the Witch-king’s attack.",
       ],
       [
           ("Éowyn", f"{C}/eowyn/", "Niece who rides in his host in disguise."),
           ("Éomer", f"{C}/eomer/", "Sister-son and heir as king after him."),
           ("Helm’s Deep", f"{L}/helms-deep/", "Fortress of his stand against Isengard."),
           ("Edoras", f"{L}/edoras/", "Seat of the Golden Hall."),
       ],
       "Théoden’s death is the heroic king-death of the Rohirrim in the book. His revival from Wormtongue’s shadow is a major movement of *The Two Towers*.")

    md("characters", "faramir", "Faramir",
       "Younger son of Denethor who understands the Ring’s danger, spares Frodo, and survives to become Steward under the King and Prince of Ithilien.",
       ["human", "gondor"], "Captain of Gondor; later Steward and Prince", "Third Age",
       "Faramir is a Man of Gondor, younger son of Denethor II, captain of Rangers in Ithilien. Unlike Boromir, he rejects the Ring when it is within his power. Wounded and nearly burned in his father’s despair, he lives to yield the Stewardship to Aragorn and to marry Éowyn.",
       "Character (Man of Gondor)",
       "Born in Minas Tirith; trained as captain and as a man of lore, in tension with Denethor’s preference for Boromir.",
       "Boromir; Denethor; Frodo and Sam; Éowyn; Ithilien; Gondor.",
       "To defend Gondor’s eastern marches and to judge the Ring rightly when he finds it.",
       [
           "- **Henneth Annûn.** He captures Frodo and Sam, hears their errand, and lets them go, asking that they remember Gondor as more than a grasping hand. (The film alters this encounter substantially; the book’s Faramir does not drag them to Osgiliath as a first impulse of ambition.)",
           "- **Retreat and pyre.** Wounded in the retreat from the Rammas, he is laid for burning by Denethor; Pippin and Gandalf save him.",
           "- **Peace.** He becomes Steward in the King’s name and Prince of Ithilien with Éowyn.",
       ],
       [
           ("Boromir", f"{C}/boromir/", "Brother whose failure with the Ring he does not repeat."),
           ("Denethor II", f"{C}/denethor/", "Father whose palantír-despair nearly kills him."),
           ("Ithilien", f"{L}/ithilien/", "Land he loves and later rules."),
           ("Éowyn", f"{C}/eowyn/", "Wife after the Houses of Healing."),
       ],
       "Faramir is Tolkien’s counter-example to Boromir: Gondor’s need does not justify taking the Ring. Readers should prefer the book scene at Henneth Annûn over the film’s more suspicious captain.")

    md("characters", "denethor", "Denethor II",
       "Steward of Gondor who contends with Sauron through the palantír, reads defeat in its true but selective visions, and dies by fire rather than yield to a returning king.",
       ["human", "gondor"], "Steward of Gondor", "Third Age",
       "Denethor II is the last ruling Steward of Gondor before Aragorn’s coronation. He is intelligent, proud, and long at war. The palantír of Minas Tirith shows him real armies and a real Dark Lord; it does not show him the Quest. He attempts to burn himself and the wounded Faramir; Faramir is saved, Denethor is not.",
       "Character (Man of Gondor; Steward)",
       "Born to the House of the Stewards in Minas Tirith; ruled in the name of absent kings.",
       "Boromir; Faramir; Minas Tirith; the palantír; Sauron as unseen antagonist in the stone.",
       "To hold Gondor; he fails when despair is mistaken for complete knowledge.",
       [
           "- **The stone.** He uses the palantír and is matched by Sauron, who cannot wholly daunt him at first but can bias what he sees.",
           "- **Sons.** Boromir’s death and Faramir’s wounding break his remaining hope.",
           "- **The tombs.** He lights a pyre in the House of the Stewards. Gandalf and Pippin save Faramir; Denethor dies in the flames.",
       ],
       [
           ("Faramir", f"{C}/faramir/", "Son he would burn with him."),
           ("Boromir", f"{C}/boromir/", "Preferred heir, already dead in the North."),
           ("Minas Tirith", f"{L}/minas-tirith/", "City of his rule."),
           ("Sauron", f"{C}/sauron/", "Enemy who shapes the palantír’s lessons."),
       ],
       "Denethor is not a simple coward in the book: he is a capable ruler destroyed by pride and by incomplete truth. The film heightens his instability; the novel keeps him formidable until the end.")

    md("characters", "treebeard", "Treebeard",
       "Eldest of the Ents still active in the narrative; he leads the last march of his people against Isengard after Merry and Pippin bring news of Saruman’s treachery.",
       ["ent"], "Fangorn; eldest of the Ents", "Elder Days to Third Age",
       "Treebeard (Fangorn) is an Ent, a shepherd of trees, among the oldest beings still walking in Middle-earth in the Third Age. Slow speech hides a capacity for wrath. The Entmoot decides for war; Isengard is unmade by water and growing things rather than by conventional siege engines.",
       "Character (Ent)",
       "Awoke with the Ents in the Elder Days when the trees first needed shepherds (legendarium; *The Two Towers* presents him as immemorially old).",
       "Fangorn Forest; Merry and Pippin; the Entmoot; Saruman as enemy.",
       "To protect the remaining forests and to answer Saruman’s felling and orc-industry.",
       [
           "- **Meeting the Hobbits.** He takes Merry and Pippin in, learns of the wider war, and calls the Entmoot.",
           "- **Isengard.** The Ents break the ring of Isengard and flood the pits. Orthanc itself they cannot split.",
           "- **After.** He keeps Saruman confined for a time, then lets him go—a decision that leads to the wizard’s later crimes in the Shire.",
       ],
       [
           ("Fangorn Forest", f"{L}/fangorn/", "His home and remnant wood."),
           ("Isengard", f"{L}/isengard/", "Target of the Ents’ march."),
           ("Peregrin Took", f"{C}/peregrin-took/", "Hobbit guest who helps stir him."),
           ("Ents", f"{P}/ents/", "His dwindling people."),
       ],
       "Treebeard’s march is the War’s strangest army: landscape taking a side. The loss of the Entwives, mentioned in the book, explains the Ents’ lack of a future in kind.")

    md("characters", "bilbo-baggins", "Bilbo Baggins",
       "Hobbit of the Shire whose adventure under Erebor brought the One Ring west, and whose pity for Gollum left the creature alive to decide the Third Age.",
       ["hobbit", "ring-bearer"], "Burglar of Erebor; uncle of Frodo", "Third Age",
       "Bilbo Baggins is a Hobbit of Bag End, protagonist of *The Hobbit*, and the finder of the One Ring in Gollum’s cave. He bequeaths the Ring to Frodo and retires to Rivendell. His mercy in the dark is treated in *The Lord of the Rings* as a hinge of later history.",
       "Character (Hobbit)",
       "Born in the Shire in T.A. 2890; of Belladonna Took’s line as well as Baggins respectability.",
       "Frodo; Gandalf; Thorin’s company (earlier); Rivendell in old age; the One Ring.",
       "Finder and long-term keeper of the Ring; later a poet and source of lore in Imladris.",
       [
           "- **The finding.** In T.A. 2941 he takes the Ring; he does not kill Gollum.",
           "- **The birthday.** In T.A. 3001 he leaves the Shire, passing the Ring to Frodo with difficulty and Gandalf’s help.",
           "- **Rivendell and the Havens.** He lives in Elrond’s house, offers verses and Sting’s cousin-sword context, and sails West with Frodo in 3021.",
       ],
       [
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Heir of Bag End and of the Ring."),
           ("Gollum", f"{C}/gollum/", "From whom he took the Ring and whom he spared."),
           ("The Shire", f"{L}/the-shire/", "Home of his long peace after Erebor."),
           ("Rivendell", f"{L}/rivendell/", "His last home in Middle-earth."),
       ],
       "Bilbo connects *The Hobbit* to the War of the Ring. The narrator of *The Lord of the Rings* treats his pity as providential. He is a Ring-bearer permitted to sail West though he did not complete Frodo’s errand.")

    md("characters", "witch-king", "The Witch-king of Angmar",
       "Chief of the Nazgûl, once a king of Men, who breaks the gate of Minas Tirith and is slain by Éowyn and Merry on the Pelennor.",
       ["nazgul", "wraith"], "Lord of the Nazgûl", "Second Age to Third Age",
       "The Witch-king is the lord of the Ringwraiths, a Man who took a Ring of Power and faded into Sauron’s service. He destroyed the North-kingdom in the wars of Angmar, wounded Frodo at Weathertop, and commanded the assault on Minas Tirith. He falls on the Pelennor Fields.",
       "Character (Nazgûl; wraith)",
       "A king of Men in the Second Age who accepted a Ring from Sauron; his mortal name is not given in *The Lord of the Rings*.",
       "The Nine; Sauron; Angmar (earlier); Minas Morgul; the Pelennor.",
       "To hunt the Ring and to break Gondor’s strength as Sauron’s chief captain.",
       [
           "- **Angmar and the North.** He waged war on Arnor until that kingdom fell.",
           "- **Weathertop.** He stabs Frodo with a Morgul-knife.",
           "- **Pelennor.** He breaks the gate, kills Théoden’s horse and king in the charge’s crisis, and is destroyed by Éowyn and Merry. The other Nazgûl continue until the Ring itself is unmade.",
       ],
       [
           ("The Nazgûl", f"{P}/nazgul/", "The Nine, of whom he is chief."),
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Place of his destruction."),
           ("Éowyn", f"{C}/eowyn/", "Who slays him after Merry’s blow."),
           ("Minas Tirith", f"{L}/minas-tirith/", "City whose gate he breaks."),
       ],
       "Glorfindel’s prophecy that not by the hand of man would he fall is fulfilled without trickery of translation: a woman and a hobbit slay him. His identity as a former human king is canonical; a specific national origin is not named in the main text.")

    md("characters", "eomer", "Éomer",
       "Third Marshal of the Mark who is briefly exiled from Théoden’s poisoned court, leads Rohan’s riders in the War, and becomes king after Théoden’s death.",
       ["human", "rohan"], "Third Marshal, then King of the Mark", "Third Age",
       "Éomer son of Éomund is sister-son of Théoden, a marshal of the Riders. He aids Aragorn’s company against orders, is imprisoned, and is freed when the king wakes. He fights at Helm’s Deep and the Pelennor and succeeds to the throne of Rohan.",
       "Character (Man of Rohan; King)",
       "Born in Rohan; of the royal house through Théodwyn, Théoden’s sister.",
       "Théoden; Éowyn; Aragorn; Rohan; later alliance with the Reunited Kingdom.",
       "To command Rohan’s arms in the field and then to rule the Mark in the Fourth Age.",
       [
           "- **The Wold.** He meets the Three Hunters, lends horses, and is arrested at Gríma’s instance.",
           "- **War.** Restored, he fights through the Hornburg and the Pelennor, where he thinks Éowyn dead before she is found living.",
           "- **Kingship.** He is crowned after Théoden’s funeral and remains Aragorn’s ally.",
       ],
       [
           ("Éowyn", f"{C}/eowyn/", "Sister, thought slain on the field."),
           ("Théoden", f"{C}/theoden/", "Uncle and predecessor as king."),
           ("Rohan", f"{L}/rohan/", "His land."),
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Battle he helps to finish."),
       ],
       "Éomer is Rohan’s war-leader in the book after Théoden’s restoration. His kingship in the Fourth Age is appendix-canon.")

    md("characters", "celeborn", "Celeborn",
       "Sindarin lord of Lothlórien, husband of Galadriel, who arms the Fellowship with boats and warnings and remains in Middle-earth for a time after she sails.",
       ["elf", "sindar"], "Lord of Lothlórien", "First Age to Fourth Age",
       "Celeborn is an Elf of Sindarin kindred (in the published *Lord of the Rings* account), co-ruler of Lothlórien with Galadriel. He is a counsellor and host rather than a wanderer in the southern war. After the War he dwells for a while in East Lórien before taking the West in his own time.",
       "Character (Elf; Sinda)",
       "Of the Sindar of Doriath in the wider legendarium; *The Lord of the Rings* presents him as an ancient lord of the Golden Wood.",
       "Galadriel; Lothlórien; the Fellowship as guests; later East Lórien.",
       "To govern Lórien and to speed the Fellowship down Anduin with counsel about the River and the wood.",
       [
           "- **The Fellowship.** He provides boats, supplies, and caution about the Anduin and Fangorn.",
           "- **After Sauron.** With Lórien’s power fading, he remains longer than Galadriel; the appendices place his eventual departure.",
       ],
       [
           ("Galadriel", f"{C}/galadriel/", "His wife and co-ruler."),
           ("Lothlórien", f"{L}/lothlorien/", "Their realm."),
       ],
       "Celeborn’s later chronology is sketched in the appendices rather than in the main narrative. He should not be confused with film-silent extras; in the book he speaks and judges at the departure from Lórien.")

    md("characters", "elendil", "Elendil",
       "Leader of the Faithful who escaped Númenor's ruin and founded the kingdoms of Arnor and Gondor, father of Isildur and Anárion.",
       ["man", "dunadan", "king"], "High King of the Dúnedain in exile", "Second Age",
       "Elendil is a Man of Númenor, lord of the Faithful who refused Sauron's domination of the isle. When Númenor is drowned he escapes to Middle-earth with his sons and founds the Realms in Exile: Arnor in the North and Gondor in the South. He is the ancestor of Aragorn's claim and the figure in whose name the Last Alliance marches against Sauron.",
       "Character (Man; Dúnadan; King)",
       "Born in Númenor before its fall; descended from Elros, first King of Númenor, through the line of the Lords of Andúnië.",
       "Isildur; Anárion; Arnor; Gondor; Gil-galad; the Last Alliance; Narsil.",
       "To preserve the Faithful and establish the Dúnedain kingdoms in Middle-earth against Sauron's return.",
       [
           "- **The Faithful.** Elendil's house resists Sauron's corruption of Númenor and survives the Downfall in ships.",
           "- **Realms in Exile.** He rules as High King from Arnor; his sons build Gondor in the South. Minas Ithil and Minas Anor are raised in their names.",
           "- **Last Alliance.** He marches with Gil-galad against Sauron and falls on the slopes of Orodruin. Isildur takes up Narsil and cuts the Ring from Sauron's hand.",
       ],
       [
           ("Isildur", f"{C}/isildur/", "Eldest son who takes the Ring after Sauron's fall."),
           ("Aragorn", f"{C}/aragorn/", "Heir many generations later of his northern line."),
           ("The Last Alliance", f"{E}/last-alliance/", "War in which he dies and Sauron is overthrown."),
           ("Gondor", f"{L}/gondor/", "South-kingdom founded by his sons."),
       ],
       "Elendil is the root of the Dúnedain claim in the West. The shards of Narsil, his sword broken when Sauron struck him down, pass down to Aragorn as Andúril reforged.")

    md("characters", "isildur", "Isildur",
       "Eldest son of Elendil who cut the One Ring from Sauron's hand at the Last Alliance and kept it, beginning the long interval of the Third Age.",
       ["man", "dunadan", "ring-bearer"], "King of Gondor; Isildur's Bane", "Second Age to Third Age",
       "Isildur is a Man of the Dúnedain, son of Elendil, who with Anárion founded Gondor's citadels in the South. At the Last Alliance he takes up the hilt-shard of Narsil and cuts the One Ring from Sauron. He refuses Elrond's counsel to destroy it in Orodruin. His death in the Gladden Fields loses the Ring for nearly three millennia.",
       "Character (Man; Dúnadan; Ring-bearer)",
       "Born in Númenor or on the voyage to Middle-earth; eldest son of Elendil; co-founder of Gondor with Anárion.",
       "Elendil; Anárion; Elrond; the One Ring; Arnor and Gondor; the Last Alliance.",
       "To rule Gondor and the North-kingdom after his father; his failure is keeping the Ring as weregild.",
       [
           "- **Gondor's builder.** He plants the White Tree from Nimloth and raises Minas Ithil and the tower of Orthanc (wider legendarium).",
           "- **The cutting.** With Narsil's shard he takes the Ring; Elrond and Círdan urge him to cast it into the fire. He will not.",
           "- **The Gladden Fields.** Ambushed by Orcs, he puts on the Ring to escape and is shot in the Anduin. The Ring is lost until Déagol finds it.",
       ],
       [
           ("Elendil", f"{C}/elendil/", "Father, High King slain before Orodruin."),
           ("Elrond", f"{C}/elrond/", "Who counsels destruction of the Ring at the Sammath Naur."),
           ("The One Ring", f"{P}/one-ring/", "Taken as weregild and lost in the river."),
           ("Aragorn", f"{C}/aragorn/", "Heir of his line through the Chieftains of the Dúnedain."),
           ("The Last Alliance", f"{E}/last-alliance/", "War that ends with his fateful choice."),
       ],
       "Isildur's refusal is the hinge of the Third Age. Tolkien treats him not as a villain but as a man who errs at the moment of victory. Aragorn's kingship is the long-delayed fulfilment of what Isildur's house was meant to be.")

    md("characters", "elros", "Elros",
       "Twin brother of Elrond who chose mortality and became the first King of Númenor, ancestor of Elendil and all the Dúnedain kings.",
       ["half-elven", "man", "king"], "First King of Númenor", "First Age to Second Age",
       "Elros is the son of Eärendil and Elwing, twin brother of Elrond Half-elven. At the end of the First Age the Valar grant him and his brother the choice of kindred. Elros chooses to be counted among Men and is granted a life many times longer than ordinary Men. He founds the line of Númenórean kings that leads through Elendil to Aragorn.",
       "Character (Half-elven; Man by choice)",
       "Born at the end of the First Age; son of Eärendil and Elwing; brother of Elrond.",
       "Elrond; Eärendil; Elwing; Númenor; Elendil (descendant); the Valar's gift of long life.",
       "To rule Númenor as its first king and to begin the line of the Dúnedain.",
       [
           "- **The choice.** Where Elrond chooses the Eldar, Elros accepts the Gift of Men with extended span—a fate Arwen will later mirror in reverse.",
           "- **Númenor.** He rules the isle in its early glory before Sauron's later corruption.",
           "- **Descent.** Through his line come Elendil, Isildur, and eventually Aragorn Telcontar.",
       ],
       [
           ("Elrond", f"{C}/elrond/", "Twin who chose the Eldar instead."),
           ("Eärendil", f"{C}/earendil/", "Father, star-voyager of the Silmaril."),
           ("Elendil", f"{C}/elendil/", "Descendant who founds Arnor and Gondor."),
           ("Aragorn", f"{C}/aragorn/", "Heir of his line in the late Third Age."),
           ("Arwen Undómiel", f"{C}/arwen/", "Who relinquishes Elven immortality as he once accepted mortality."),
       ],
       "Elros binds the Half-elven line to the kingdoms of Men. His choice is the mirror of Elrond's and of Arwen's later renunciation. The encyclopedia treats him as genealogical anchor rather than as a figure in the War of the Ring itself.")

    md("characters", "eorl-the-young", "Eorl the Young",
       "Lord of the Éothéod who rode south to Gondor's aid and received Calenardhon as the land that became Rohan.",
       ["man", "rohan", "king"], "First King of the Mark", "Third Age",
       "Eorl the Young is the lord of the Éothéod, a people of the North related to the Rohirrim's ancestors. When Gondor calls for aid against the Balchoth, he leads his riders south in the great ride remembered in the Oath of Eorl. Cirion, Steward of Gondor, grants him Calenardhon, thereafter called Rohan. Every king of the Mark descends from him.",
       "Character (Man of the North; King)",
       "Born among the Éothéod beyond the Misty Mountains; came south in T.A. 2510 at Gondor's need.",
       "Cirion of Gondor; the Éothéod; Rohan; the Oath of Eorl; the Mering Stream.",
       "To answer Gondor's call and to establish his people in the granted land.",
       [
           "- **The Ride.** Eorl's host crosses the Anduin and turns the battle at the Field of Celebrant.",
           "- **The Gift.** Calenardhon is given in perpetual alliance; the Éothéod become the Rohirrim.",
           "- **The Oath.** Gondor and Rohan bind themselves: aid in need, mutual defence—a oath Théoden honours at the Pelennor.",
       ],
       [
           ("Rohan", f"{L}/rohan/", "The realm he founded."),
           ("Théoden", f"{C}/theoden/", "A late king of his line in the War of the Ring."),
           ("Éomer", f"{C}/eomer/", "Last king of the Third Age in his house."),
           ("Gondor", f"{L}/gondor/", "Ally whose need brought him south."),
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Where the Oath is fulfilled again."),
       ],
       "Eorl is Rohan's founding name. The book does not send him into the main narrative, but Théoden's ride and Éomer's kingship are unintelligible without him. The Oath of Eorl is living politics, not antique poetry.")

    md("characters", "earendil", "Eärendil",
       "Half-elven mariner who sailed to Valinor with a Silmaril and became the star Eärendil, father of Elrond and Elros.",
       ["half-elven"], "The Mariner; the Star", "First Age to all Ages",
       "Eärendil is the son of Tuor and Idril, husband of Elwing, and father of Elrond and Elros. He builds Vingilot and, bearing a Silmaril, passes the enchantments of the West and pleads before the Valar for aid against Morgoth. For this he is set in the heavens as the star the Elves hallow. His line is the bridge between Men, Elves, and the Half-elven choices that shape the Second and Third Ages.",
       "Character (Half-elven; Mariner)",
       "Born in Gondolin; wedded Elwing at the Mouths of Sirion; sailed West with a Silmaril at the end of the First Age.",
       "Elwing; Elrond; Elros; Tuor and Idril; the Silmarils; Valinor.",
       "To seek the Valar's mercy for Elves and Men against Morgoth; to become the star of hope.",
       [
           "- **The voyages.** He is a mariner of the Elder Days, seeking a path when Middle-earth lies under Morgoth's shadow.",
           "- **The Silmaril.** With Elwing he bears one of Fëanor's jewels to the West; the Valar receive him and set him in the sky.",
           "- **The sons.** Elrond and Elros are born before the War of Wrath; each will choose a different kindred.",
       ],
       [
           ("Elrond", f"{C}/elrond/", "Son who chose the Eldar."),
           ("Elros", f"{C}/elros/", "Son who chose Men and ruled Númenor."),
           ("Elwing", f"{C}/elwing/", "Wife who bore the Silmaril to him."),
           ("Lúthien", f"{C}/luthien/", "Ancestor through Elwing's line, model of mortal choice."),
           ("Aragorn", f"{C}/aragorn/", "Descendant through Elros and Elendil."),
       ],
       "Eärendil is named in *The Lord of the Rings* as the star Frodo and Sam see from the Morgai—a sign of hope. His genealogy explains why Elrond is Half-elven and why Aragorn's claim is also an Elven kinship claim.")

    md("characters", "elwing", "Elwing",
       "Daughter of Dior and Nimloth who bore the Silmaril to Eärendil and became mother of Elrond and Elros.",
       ["half-elven", "noldor"], "Keeper of the Silmaril", "First Age",
       "Elwing is the daughter of Dior and Nimloth, granddaughter of Lúthien and Beren. When the Sons of Fëanor assail her refuge at the Mouths of Sirion, she casts herself into the Sea with the Silmaril and is borne to Eärendil. Together they sail to Valinor. She is the link between Lúthien's mortal choice and the Half-elven line of Rivendell.",
       "Character (Half-elven)",
       "Born in the First Age; heir of Lúthien; wedded Eärendil; mother of Elrond and Elros.",
       "Eärendil; Elrond; Elros; Lúthien; the Silmaril; the Havens of Sirion.",
       "To preserve the Silmaril and unite her fate with Eärendil's voyage West.",
       [
           "- **Her heritage.** She carries the light of the Silmaril through Lúthien's line.",
           "- **The flight.** Pursued by the Sons of Fëanor, she escapes into the Sea and is reunited with Eärendil in bird-form (wider legendarium).",
           "- **The West.** She accompanies the plea that brings the Host of the West against Morgoth.",
       ],
       [
           ("Eärendil", f"{C}/earendil/", "Husband; star-voyager."),
           ("Elrond", f"{C}/elrond/", "Son who becomes lord of Rivendell."),
           ("Elros", f"{C}/elros/", "Son who becomes first King of Númenor."),
           ("Lúthien", f"{C}/luthien/", "Grandmother whose story echoes in Arwen's choice."),
           ("Galadriel", f"{C}/galadriel/", "Kinswoman of the Noldor, fellow survivor into the Third Age."),
       ],
       "Elwing does not appear in the main *Lord of the Rings* narrative, but her descent explains Elrond's authority and the Silmaril-light remembered in Eärendil's star.")

    md("characters", "luthien", "Lúthien",
       "An Elf who chose mortality for love of Beren, recovered a Silmaril from Morgoth's crown, and became ancestor of Elrond's line.",
       ["half-elven", "noldor"], "Tinúviel; the Morning Star of the Elves", "First Age",
       "Lúthien Tinúviel is the daughter of Thingol and Melian, beloved of the Man Beren. Together they wrest a Silmaril from Morgoth's iron crown—a deed no army achieved. She chooses mortality and dies with Beren, though both are briefly returned. Her choice is the archetype Arwen cites when she weds Aragorn and accepts the Gift of Men.",
       "Character (Half-elven by parentage; chose mortality)",
       "Born in Doriath in the First Age; daughter of Thingol and the Maia Melian; wedded Beren.",
       "Beren; Dior (son); Elwing (granddaughter); Elrond's line; Arwen's model.",
       "To prove that love and free will can achieve what force cannot; to bind Elf and Man in one line.",
       [
           "- **The Quest.** With Beren she enters Angband and takes a Silmaril from Morgoth's crown.",
           "- **The choice.** She renounces immortality for Beren's sake—the first such union of its kind.",
           "- **The line.** Through Dior and Elwing her blood runs to Elrond, Elros, and eventually Arwen.",
       ],
       [
           ("Elrond", f"{C}/elrond/", "Descendant many generations removed."),
           ("Arwen Undómiel", f"{C}/arwen/", "Who repeats her choice with Aragorn."),
           ("Elwing", f"{C}/elwing/", "Granddaughter who bore the Silmaril onward."),
           ("Aragorn", f"{C}/aragorn/", "Descendant through Elros and the Dúnedain."),
           ("Galadriel", f"{C}/galadriel/", "Contemporary of the First Age, kin of the same world."),
       ],
       "Arwen is called Undómiel in echo of Lúthien. The book treats Lúthien's story as legend living in the present: Elrond names it when he speaks of his daughter's choice.")

    md("characters", "celebrían", "Celebrían",
       "Daughter of Galadriel and Celeborn, wife of Elrond, and mother of Arwen; wounded by Orcs in the Redhorn Pass and later sailed West.",
       ["half-elven", "noldor"], "Lady of Rivendell", "Second Age to Third Age",
       "Celebrían is the daughter of Galadriel and Celeborn, wed to Elrond in the Second Age. She bears him Arwen and the twin sons Elladan and Elrohir (named in the wider legendarium). In T.A. 2509 she is waylaid by Orcs in the Redhorn Pass and wounded; though healed, she sails West, leaving Elrond to endure Middle-earth without her.",
       "Character (Half-elven)",
       "Born in the Second Age; daughter of Galadriel and Celeborn; wife of Elrond; mother of Arwen.",
       "Galadriel; Celeborn; Elrond; Arwen; Rivendell; Lothlórien.",
       "To unite two great Elven houses in marriage and to bear the next generation of Half-elven choice.",
       [
           "- **Marriage.** She weds Elrond, linking Lórien's lords to Imladris.",
           "- **Motherhood.** Arwen is born in the Third Age; Celebrían's fate shapes Elrond's later grief.",
           "- **The wounding.** Orc-assault in the mountains; she departs over Sea though Elrond remains.",
       ],
       [
           ("Galadriel", f"{C}/galadriel/", "Mother, Lady of Lórien."),
           ("Celeborn", f"{C}/celeborn/", "Father, co-lord of the Golden Wood."),
           ("Elrond", f"{C}/elrond/", "Husband, lord of Rivendell."),
           ("Arwen Undómiel", f"{C}/arwen/", "Daughter who chooses mortality."),
           ("Rivendell", f"{L}/rivendell/", "House she shared with Elrond."),
       ],
       "Celebrían does not walk in the War of the Ring, but her parentage explains Arwen's kinship with Galadriel and her upbringing between Lórien and Rivendell.")

    md("characters", "thranduil", "Thranduil",
       "Sindarin King of the Woodland Realm in northern Mirkwood, father of Legolas and captor (and loser) of Gollum before the War of the Ring.",
       ["elf", "sindar", "king"], "King of the Woodland Realm", "First Age to Fourth Age",
       "Thranduil is the Elvenking of Mirkwood, a Sindar who rules the Woodland Realm from underground halls in the forest's northern reaches. He is Legolas's father. His people capture Gollum after he leaves the Mountains; Gollum later escapes, news Legolas brings to the Council of Elrond. He fights in the War of the Ring against Dol Guldur (appendices).",
       "Character (Elf; Sinda; King)",
       "Son of Oropher (wider legendarium); migrated to Greenwood the Great; rules after his father's fall in the Last Alliance.",
       "Legolas; Mirkwood; Gollum (prisoner); the Elvenking's halls; Dol Guldur as neighbour-enemy.",
       "To guard his forest realm and to resist the Shadow spreading from southern Mirkwood.",
       [
           "- **The Hobbit.** He hosts and then imprisons Thorin's company; the dragon-slaying and the Battle of Five Armies touch his borders.",
           "- **Gollum.** His folk capture the creature; Legolas reports the escape at Rivendell.",
           "- **The War.** After Sauron's fall his realm is cleansed of Dol Guldur's influence (appendices).",
       ],
       [
           ("Legolas", f"{C}/legolas/", "Son, Fellowship member."),
           ("Mirkwood", f"{L}/mirkwood/", "His darkened forest realm."),
           ("Gollum", f"{C}/gollum/", "Prisoner who escapes his guard."),
           ("Galadriel", f"{C}/galadriel/", "Fellow Elf-lord of the age, ally in the wider war."),
       ],
       "Thranduil is more prominent in *The Hobbit* than in *The Lord of the Rings*, but Legolas's kingship and Gollum's escape are structurally important to the Quest.")

    md("characters", "durin", "Durin the Deathless",
       "First of the Fathers of the Dwarves, founder of Khazad-dûm, whose name and likeness recur in the line of Durin's Folk.",
       ["dwarf", "king"], "Durin I; the Deathless", "Elder Days",
       "Durin the Deathless is the eldest of the Seven Fathers of the Dwarves, awakened by Aulë and set to lead his kindred. He founds Khazad-dûm (Moria) beneath the Misty Mountains and rules long. Dwarven legend holds that he returns in later ages in the likeness of his descendants—hence Durin II, III, and so on, kings of Durin's Folk.",
       "Character (Dwarf; Father of the Folk)",
       "Awakened in the Elder Days; founder of Khazad-dûm; progenitor of Durin's Folk.",
       "Khazad-dûm; the Longbeards; Balin; Gimli; Thorin's line—all of Durin's Folk.",
       "To establish the greatest of the Dwarf-mansions and to begin the line that bears his name.",
       [
           "- **Khazad-dûm.** He delves the halls later called Moria, rich in mithril.",
           "- **The Deathless.** Dwarves say he sleeps rather than dies, and will return—a belief tied to look-alike kings.",
           "- **The Folk.** All Longbeards of the Third Age claim descent from him.",
       ],
       [
           ("Moria", f"{L}/moria/", "Khazad-dûm, his mansion."),
           ("Gimli", f"{C}/gimli/", "A Dwarf of his Folk in the War of the Ring."),
           ("Thorin Oakenshield", f"{C}/thorin-oakenshield/", "King under the Mountain of his line."),
           ("Balin", f"{C}/balin/", "Lord who attempted to refound Khazad-dûm."),
           ("Dwarves", f"{P}/dwarves/", "The kindred he fathered."),
       ],
       "Durin does not appear in the Third-Age narrative, but Gimli's pride in Moria and Balin's tomb inscription ('Durin's Folk') assume the reader knows his name.")

    md("characters", "thorin-oakenshield", "Thorin Oakenshield",
       "King under the Mountain who led the Quest of Erebor, reclaimed the Lonely Mountain from Smaug, and died in the Battle of Five Armies.",
       ["dwarf", "king"], "King under the Mountain", "Third Age",
       "Thorin II Oakenshield is a Dwarf of Durin's Folk, exiled king of Erebor, leader of the company in *The Hobbit*. He reclaims the Lonely Mountain from Smaug and dies defending his gains against Bolg's host at the Battle of Five Armies. His cousin Dáin succeeds him. The Arkenstone and his burial with Orcrist belong to the same tale that brings Bilbo—and the Ring—into the wider history.",
       "Character (Dwarf; King)",
       "Born in the Third Age; son of Thráin II; heir of Thrór; exiled long in the Blue Mountains before the Quest.",
       "Balin; Glóin; Dáin Ironfoot; Bilbo Baggins; Erebor; the Arkenstone.",
       "To reclaim Erebor and restore Durin's Folk in the Mountain.",
       [
           "- **Exile.** Smaug drove his people from Erebor; Thráin's madness and capture in Dol Guldur leave Thorin lord of a scattered folk.",
           "- **The Quest.** With Gandalf's counsel he hires Bilbo and twelve Dwarves; the dragon falls, treasure is disputed.",
           "- **The battle.** He dies on Ravenhill, reconciled with Bilbo; Dáin becomes King under the Mountain.",
       ],
       [
           ("Bilbo Baggins", f"{C}/bilbo-baggins/", "Burglar of the company; finder of the Ring."),
           ("Glóin", f"{C}/gloin/", "Companion; father of Gimli."),
           ("Balin", f"{C}/balin/", "Elder companion, later Lord of Moria."),
           ("Dáin Ironfoot", f"{C}/dain-ironfoot/", "Cousin and successor as king."),
           ("Erebor", f"{L}/erebor/", "The Mountain he reclaimed."),
       ],
       "Thorin connects *The Hobbit* to the legendarium's Dwarf-politics. Gimli is the son of his companion Glóin; Balin's later colony in Moria is a direct sequel to Thorin's company.")

    md("characters", "gloin", "Glóin",
       "Dwarf of Thorin's company, father of Gimli, who represents Erebor at the Council of Elrond with news of the Mountain's unease.",
       ["dwarf"], "Companion of Thorin; father of Gimli", "Third Age",
       "Glóin is a Dwarf of Durin's Folk, one of Thorin Oakenshield's twelve companions on the Quest of Erebor. He survives the Battle of Five Armies and lives to old age under Dáin's rule. In T.A. 3018 he comes to Rivendell with his son Gimli and messages from Dáin concerning Bilbo's Ring—setting Gimli on the road to the Fellowship.",
       "Character (Dwarf)",
       "Born in the Third Age; fought at Erebor; father of Gimli; messenger to the Council.",
       "Gimli; Thorin; Dáin; Erebor; Bilbo; the Fellowship by his son's membership.",
       "To serve the king under the Mountain and to carry Dáin's counsel to Elrond.",
       [
           "- **The Quest.** He walks to Erebor with Thorin and Bilbo.",
           "- **Peace.** He lives prosperously in Erebor until the War of the Ring.",
           "- **Rivendell.** He attends the Council with Gimli; his tale of Dain's wariness helps launch the Fellowship.",
       ],
       [
           ("Gimli", f"{C}/gimli/", "Son, Fellowship member."),
           ("Thorin Oakenshield", f"{C}/thorin-oakenshield/", "King he followed to Erebor."),
           ("Dáin Ironfoot", f"{C}/dain-ironfoot/", "King he serves in later years."),
           ("Bilbo Baggins", f"{C}/bilbo-baggins/", "Former companion of the Quest."),
           ("The Council of Elrond", f"{E}/council-of-elrond/", "Where he brings news from the North."),
       ],
       "Glóin is the genealogical link between *The Hobbit*'s company and the War of the Ring. The book introduces Gimli as Glóin's son at the Council—a detail easy to miss but structurally neat.")

    md("characters", "balin", "Balin",
       "Elder Dwarf of Thorin's company who later led a failed colony to refound Khazad-dûm, recorded in the tomb-book the Fellowship finds in Moria.",
       ["dwarf"], "Lord of Moria (briefly)", "Third Age",
       "Balin is a Dwarf of Durin's Folk, among the oldest of Thorin's companions. After Erebor's reclamation he prospers until, in T.A. 2989, he leads an expedition to Moria seeking to restore Khazad-dûm. The colony is destroyed by Orcs; Balin is slain. The Fellowship discovers his tomb and the record of the colony's five-year failure—Gimli's grief at the place.",
       "Character (Dwarf)",
       "Companion of Thorin; later colonist-lord of Moria; friend of Bilbo.",
       "Thorin; Glóin; Gimli; Moria; the Chamber of Mazarbul record.",
       "To refound the ancient mansion of Durin; to fail where Durin once thrived.",
       [
           "- **The Quest.** He is a trusted elder in Thorin's company.",
           "- **The colony.** He enters Moria with Ori and Óin among others; Orcs overrun them.",
           "- **The record.** 'We cannot get out'—the book the Fellowship reads in the tomb.",
       ],
       [
           ("Moria", f"{L}/moria/", "Mansion he tried to reclaim."),
           ("Gimli", f"{C}/gimli/", "Son of his companion Glóin; mourns at his tomb."),
           ("Thorin Oakenshield", f"{C}/thorin-oakenshield/", "King of the earlier Quest."),
           ("Durin the Deathless", f"{C}/durin/", "Founder of the halls Balin sought to reopen."),
           ("Gandalf", f"{C}/gandalf/", "Who leads the Fellowship through Balin's dead domain."),
       ],
       "Balin's colony explains why Moria is full of Orcs yet holds Dwarvish graves. Gimli's hope entering Moria is the hope of Durin's Folk to return—a hope the tomb-book crushes.")

    md("characters", "dain-ironfoot", "Dáin Ironfoot",
       "Dwarf-lord who slew Azog's heir at Azanulbizar, succeeded Thorin as King under the Mountain, and fell defending Erebor in the War of the Ring.",
       ["dwarf", "king"], "King under the Mountain", "Third Age",
       "Dáin II Ironfoot is a Dwarf of Durin's Folk, cousin of Thorin Oakenshield, renowned for killing Azog's son Náin at the Battle of Azanulbizar. He arrives with armed Dwarves at the Battle of Five Armies and becomes King under the Mountain when Thorin dies. In the War of the Ring he refuses to yield Sauron's messengers and dies at the gates of Erebor aged 252 (appendices).",
       "Character (Dwarf; King)",
       "Born in the Third Age; lord of the Iron Hills before Erebor; cousin and successor of Thorin.",
       "Thorin; Glóin; Gimli; Erebor; the Iron Hills; Brand of Dale as ally.",
       "To rule Erebor after Thorin and to hold the North against Sauron's northern assault.",
       [
           "- **Azanulbizar.** He avenges Náin and earns his name Ironfoot.",
           "- **Five Armies.** He turns the battle with Dwarves of the Iron Hills.",
           "- **The War.** He dies defending Erebor; his son Thorin III Stonehelm succeeds.",
       ],
       [
           ("Thorin Oakenshield", f"{C}/thorin-oakenshield/", "Cousin he succeeds."),
           ("Glóin", f"{C}/gloin/", "Subject and fellow veteran of the Quest."),
           ("Erebor", f"{L}/erebor/", "Kingdom he ruled."),
           ("Gimli", f"{C}/gimli/", "Subject who walks the southern war."),
       ],
       "Dáin's death in the North is appendix-canon but shows the War was not only Rohan and Gondor. Glóin's message at the Council comes from his court.")

    write_extra_characters(md, C, L, E, P)
    print("characters done")
    # locations, events, people continue in same function - split by calling more md() below
    write_locations(md, C, L, E, P)
    write_events(md, C, L, E, P)
    write_kindreds(md, C, L, E, P)
    print("all done")


def write_locations(md, C, L, E, P):
    md("locations", "the-shire", "The Shire",
       "A settled Hobbit-land in Eriador whose peace is what the Quest is meant to save, and which is itself occupied and then freed in the Scouring.",
       ["eriador", "homeland"], "Four Farthings of the Hobbits", "Third Age",
       "The Shire is the homeland of the Hobbits of the late Third Age, lying between the Brandywine and the Far Downs. It is agrarian, inward, and long protected by Rangers the Hobbits scarcely notice. The War reaches it late, in the Scouring, when Saruman’s ruffians fence, fell, and mill it into a petty industrial tyranny.",
       "Realm / homeland",
       "Settled by Hobbits coming from Bree-land and beyond in T.A. 1601 (Shire Reckoning year 1), with leave of the King at Fornost.",
       "Hobbits; Rangers of the North; later Sharkey (Saruman) and the four Travellers.",
       "To be a quiet country; narratively, the thing worth saving and the place where the epic must still be won at home.",
       [
           "- **Peace.** Bag End, Bywater, Buckland, and Michel Delving map an ordinary world beside the great wars.",
           "- **The Scouring.** Returning Hobbits find gates, rules, and felled Party Tree. The Battle of Bywater ends the occupation.",
           "- **Healing.** Sam’s use of Galadriel’s gift helps restore the land in the following year.",
       ],
       [
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Who leaves it so that it may remain."),
           ("The Scouring of the Shire", f"{E}/scouring-of-the-shire/", "Its own small war."),
           ("Hobbits", f"{P}/hobbits/", "Its people."),
       ],
       "The Shire is both idyll and argument: the book refuses to end at the Black Gate. Its spoiling and recovery are canonical in the novel.")

    md("locations", "rivendell", "Rivendell",
       "Elrond’s hidden valley, a refuge of lore and healing where the Council is held and the Fellowship is named.",
       ["elf-home", "eriador"], "Imladris; the Last Homely House", "Second Age to Third Age",
       "Rivendell (Imladris) is the refuge founded by Elrond in a hidden valley west of the Misty Mountains’ western approaches. It is a house of healing, song, and delayed endings rather than a Gondorian fortress. The Ford of Bruinen can rise against the Nazgûl. Here Narsil’s shards were kept and the Quest was planned.",
       "Elven refuge",
       "Founded in the Second Age during the war with Sauron in Eriador.",
       "Elrond; Arwen; Aragorn’s fostering; the Council; travellers of the West.",
       "To preserve lore and provide rest and counsel against the Shadow.",
       [
           "- **Refuge.** It is hard to find and defended by Elrond’s power and the river.",
           "- **War of the Ring.** Frodo is healed there; the Council meets; the Fellowship sets out.",
           "- **Fading.** When Elrond sails, the house’s Third-Age purpose is over.",
       ],
       [
           ("Elrond", f"{C}/elrond/", "Its master."),
           ("The Council of Elrond", f"{E}/council-of-elrond/", "Held in his house."),
           ("Aragorn", f"{C}/aragorn/", "Raised there as Estel."),
       ],
       "Rivendell is the last homely house east of the Sea in the famous phrase of *The Hobbit*, reused in spirit for the Quest. It is not the site of the Ring’s destruction or of the last battles.")

    md("locations", "lothlorien", "Lothlórien",
       "A mallorn-forest of the Galadhrim, held in a remembered spring by Nenya, which shelters the Fellowship after Moria and fades when the One Ring is gone.",
       ["elf-home"], "The Golden Wood", "Third Age",
       "Lothlórien is the woodland realm of Celeborn and Galadriel east of the Misty Mountains. Time is felt differently there because Nenya preserves. The Fellowship rests in Caras Galadhon after Moria. With the One destroyed, that preservation ends and the Wood’s enchantment thins.",
       "Elven realm",
       "A remnant of wider Silvan and Sindarin settlement in the Vales of Anduin; its Golden Age in the narrative is the late Third Age under the Ring of Water.",
       "Galadriel; Celeborn; the Galadhrim; the Fellowship as guests.",
       "To hide and preserve an Elven enclave against Dol Guldur and the changing world.",
       [
           "- **The Fellowship.** They are tested, gifted, and sent down Anduin in boats.",
           "- **After the War.** The power of the Three fails; Lórien does not remain as it was.",
       ],
       [
           ("Galadriel", f"{C}/galadriel/", "Lady of the Wood."),
           ("The Anduin", f"{L}/anduin/", "River of their departure."),
           ("The Fellowship of the Ring", f"{E}/fellowship-of-the-ring/", "Guests after Moria."),
       ],
       "Lórien in the book is closed, watchful, and not a military expeditionary power in Rohan. Gifts given there (especially the Phial and lembas) are plot-critical later.")

    md("locations", "moria", "Moria",
       "Khazad-dûm, greatest mansion of Durin’s Folk, ruined after the awakening of a Balrog and crossed in terror by the Fellowship.",
       ["dwarf-home", "misty-mountains"], "Khazad-dûm", "Elder Days to Third Age",
       "Moria is the Dwarvish name in common use for Khazad-dûm, the vast halls under the Misty Mountains, once rich in mithril. Durin’s Bane, a Balrog, drove the Dwarves out. In T.A. 3019 the Fellowship attempts the mines; Gandalf falls on the Bridge of Khazad-dûm.",
       "Dwarf-mansion / ruin",
       "Founded by Durin the Deathless in the Elder Days; abandoned in T.A. 1981 after the Balrog’s awakening (appendices).",
       "Durin’s Folk; Balin (brief, failed colony); the Fellowship; Orcs and the Balrog.",
       "Once a capital of Dwarven craft; in the Quest, a dark crossing and the place of Gandalf’s fall.",
       [
           "- **Glory and fall.** Mithril and pride; then Durin’s Bane.",
           "- **Balin’s tomb.** The Fellowship finds the record of a failed reoccupation.",
           "- **The Bridge.** Gandalf breaks the bridge and falls with the Balrog; later returns as the White.",
       ],
       [
           ("Gandalf", f"{C}/gandalf/", "Who falls here fighting the Balrog."),
           ("Gimli", f"{C}/gimli/", "For whom the halls are ancestral grief."),
           ("The Fellowship of the Ring", f"{E}/fellowship-of-the-ring/", "Who cross against counsel and need."),
       ],
       "Moria is the Quest’s underground night. Later Dwarvish hopes of return belong to the Fourth Age and are not completed in the main narrative.")

    md("locations", "rohan", "Rohan",
       "The Riddermark, a grassland kingdom of horsemen allied to Gondor, whose riders relieve Minas Tirith after holding Helm’s Deep.",
       ["kingdom", "men"], "The Riddermark", "Third Age",
       "Rohan is the realm of the Rohirrim, given to Eorl’s people by Gondor (Cirion and Eorl). It is a land of horses, meads, and the White Mountains’ northern feet. In the War it is assailed by Saruman, then rides to Gondor’s field.",
       "Kingdom of Men",
       "Granted in T.A. 2510 as Calenardhon to the Éothéod; thereafter the Mark.",
       "Théoden; Éomer; Éowyn; Gondor by oath; Isengard as enemy in 3019.",
       "To keep the horse-host of the North-west and to honour the Oath of Eorl.",
       [
           "- **Saruman’s war.** The Westfold burns; the people gather to the Hornburg.",
           "- **The Ride.** After Helm’s Deep and Isengard’s fall, Théoden answers the Red Arrow.",
           "- **Aftermath.** Éomer rules; the alliance with Elessar continues.",
       ],
       [
           ("Edoras", f"{L}/edoras/", "Capital and Golden Hall."),
           ("Helm’s Deep", f"{L}/helms-deep/", "Hold of last resort."),
           ("Théoden", f"{C}/theoden/", "King in the War."),
           ("Éomer", f"{C}/eomer/", "His successor."),
       ],
       "Without Rohan, the Pelennor is described as lost. The Rohirrim are not Númenórean; their courage is of a different northern stock, which the book is careful to distinguish.")

    md("locations", "edoras", "Edoras",
       "Hill-capital of Rohan below the White Mountains, where Théoden is restored and the Mark’s war-host is set in motion.",
       ["city", "rohan"], "Seat of the Golden Hall", "Third Age",
       "Edoras is the capital of Rohan, a town of thatch and wind on a hill, dominated by Meduseld, the Golden Hall. It is exposed on the plain and close in memory to Helm’s Deep. Gandalf’s confrontation with Wormtongue occurs here.",
       "City / royal seat",
       "Built as the Mark’s seat after the gift of Calenardhon; Meduseld is the king’s hall.",
       "Théoden; the royal house; Gandalf as guest and healer of the king.",
       "Political and symbolic centre of Rohan.",
       [
           "- **Decline.** Under Gríma the hall is a place of shadow.",
           "- **Waking.** Théoden rises, Gríma is expelled, and the war-host rides.",
       ],
       [
           ("Rohan", f"{L}/rohan/", "The kingdom it heads."),
           ("Théoden", f"{C}/theoden/", "Its king."),
           ("Gandalf", f"{C}/gandalf/", "Who restores the king in Meduseld."),
       ],
       "Edoras is the starting gate of Rohan’s war, not a siege-city on the scale of Minas Tirith.")

    md("locations", "helms-deep", "Helm’s Deep",
       "Gorge-fortress of the Hornburg where Rohan withstands Saruman’s host until dawn, Gandalf, Erkenbrand, and the Huorns turn the battle.",
       ["fortress", "battle"], "The Hornburg", "Third Age",
       "Helm’s Deep is a fortress in a gorge of the White Mountains, named for Helm Hammerhand. The Hornburg and Deeping Wall are Rohan’s answer to numbers. In March 3019 Saruman’s army nearly takes it; victory comes at dawn with Gandalf, Erkenbrand, and a wood of Huorns.",
       "Fortress",
       "An old hold of Rohan (and earlier peoples of the mountains); refuge in times of invasion.",
       "Théoden’s people; Aragorn, Legolas, and Gimli; Saruman’s Uruk-hai and Dunlendings.",
       "To shelter the Mark when the open plain cannot be held.",
       [
           "- **The night.** Blasting fire breaches the wall; sorties hold the keep.",
           "- **Dawn.** A charge from the keep, Gandalf’s riders, and Huorns destroy the host.",
           "- **Canon note.** The book does not bring an army of Lórien Elves to this battle; Legolas is present as one Elf of the Fellowship.",
       ],
       [
           ("Rohan", f"{L}/rohan/", "The realm it defends."),
           ("Saruman", f"{C}/saruman/", "Enemy whose host is broken here."),
           ("Aragorn", f"{C}/aragorn/", "Who fights on the wall and in the keep."),
           ("Gimli", f"{C}/gimli/", "Who later colonizes the Glittering Caves."),
       ],
       "Helm’s Deep is the first loud defeat of Isengard’s war-machine. It frees Théoden to ride south. Film choreography and Elven reinforcements should not be read back into the novel.")

    md("locations", "gondor", "Gondor",
       "The South-kingdom of the Dúnedain, diminished but unbroken, which takes the main blow of Sauron’s war and is restored under King Elessar.",
       ["kingdom", "men", "numenor"], "The South-kingdom", "Third Age",
       "Gondor is the realm in the south founded by the sons of Elendil after Númenor’s fall. In the late Third Age stewards rule in the name of kings who do not come. Osgiliath is ruined, Ithilien is a march, yet Minas Tirith still holds. The War of the Ring is, for Gondor, a war of existence.",
       "Kingdom of Men (Dúnedain)",
       "Founded S.A. 3320 by Isildur and Anárion; the line of kings failed in T.A. 2050, after which Stewards governed.",
       "Minas Tirith; Faramir; Aragorn as returning king; Rohan by oath; Mordor as enemy.",
       "To keep the remnant of Númenor in exile and to bar Sauron from the West.",
       [
           "- **Decline.** Kin-strife, plague, and the loss of Minas Ithil (Minas Morgul) shrink the realm.",
           "- **The War.** Siege, Pelennor, and the Captains of the West at the Morannon.",
           "- **Restoration.** Elessar’s coronation begins a second flourishing in the Fourth Age.",
       ],
       [
           ("Minas Tirith", f"{L}/minas-tirith/", "The White City, its capital."),
           ("Faramir", f"{C}/faramir/", "Captain and later Prince of Ithilien."),
           ("Aragorn", f"{C}/aragorn/", "King who returns."),
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Its greatest field-battle of the War."),
       ],
       "Gondor is the political prize of the southern war. The book’s Fourth Age is largely Gondor’s and Arnor’s restored peace, not a continued Elvish age.")

    md("locations", "minas-tirith", "Minas Tirith",
       "Seven-tiered capital of Gondor on the Hill of Guard, last great fortress of the West against Mordor in the War of the Ring.",
       ["city", "gondor"], "The White City; Tower of Guard", "Third Age",
       "Minas Tirith (formerly Minas Anor) is Gondor’s capital, a white city of seven levels on Mindolluin’s out-thrust hill, facing Mordor across the Pelennor. Its silent throne-room holds a Steward, not a king, until May 3019. The siege of 15 March is the War’s most visible crisis in the South.",
       "City / fortress",
       "Built as Minas Anor in the early Gondor of the Realms in Exile; renamed when Minas Ithil fell.",
       "Denethor; Faramir; Pippin as Guard; Aragorn’s crowning; the Houses of Healing.",
       "To guard the Anduin vale and embody Gondor’s remaining strength.",
       [
           "- **Siege.** The gate is broken by the Witch-king; the city is relieved by Rohan and by Aragorn’s captured fleet.",
           "- **Crowning.** Elessar is crowned; the White Tree is found again in the book’s symbolic restoration.",
       ],
       [
           ("Gondor", f"{L}/gondor/", "The realm it heads."),
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Fought before its walls."),
           ("Denethor II", f"{C}/denethor/", "Steward during the siege."),
           ("Aragorn", f"{C}/aragorn/", "Who is crowned there."),
       ],
       "Minas Tirith is the image of the West at bay. Its relief does not end the War; the Captains still march to the Black Gate so the Ring-bearer can move.")

    md("locations", "mordor", "Mordor",
       "Sauron’s fenced land of ash, fortresses, and slave-fields, entered by stealth when war draws its armies outward.",
       ["dark-realm"], "The Black Land", "Second Age to Third Age",
       "Mordor is the realm east of the Ephel Dúath and south of the Ered Lithui, walled on three sides, with the Morannon in the north. It contains Gorgoroth, Barad-dûr, Orodruin, and tributary farmlands in the south (Nurn). Frodo and Sam cross it in disguise while Sauron looks outward.",
       "Dark realm",
       "Occupied and fortified by Sauron in the Second Age; reoccupied in the Third after his secret return.",
       "Sauron; Orcs; the Nazgûl; Cirith Ungol; Mount Doom.",
       "Base of Sauron’s war and industrial evil; the only land where the Ring can be destroyed, at Orodruin.",
       [
           "- **Geography as prison.** Mountains, the Gate, and the pass of Cirith Ungol.",
           "- **The Quest.** Two Hobbits, overlooked, reach the Mountain.",
           "- **Collapse.** With the Ring gone, armies lose their centre and the towers fall.",
       ],
       [
           ("Mount Doom", f"{L}/mount-doom/", "Volcano of the Ring’s making and unmaking."),
           ("Barad-dûr", f"{L}/barad-dur/", "The Dark Tower."),
           ("Cirith Ungol", f"{L}/cirith-ungol/", "Pass of their entry."),
           ("Sauron", f"{C}/sauron/", "Its master."),
       ],
       "Mordor is the antagonistic landscape of the third volume. The book stresses barrenness, surveillance, and slave-economy rather than a single duel with a visible Dark Lord.")

    md("locations", "mount-doom", "Mount Doom",
       "Orodruin, the volcano where the One Ring was forged and the only fire in which it can be unmade.",
       ["mordor"], "Orodruin; Amon Amarth", "Second Age to Third Age",
       "Mount Doom is the volcano in Mordor bound to Sauron’s ring-craft. The Sammath Naur, the Chambers of Fire, is the place of the Ring’s forging. The Quest ends on its brink on 25 March T.A. 3019.",
       "Volcano / sacred-industrial site of the Enemy",
       "A mountain of Mordor used by Sauron in the Second Age for the One Ring; it wakes when he is active.",
       "Sauron; the One Ring; Frodo; Gollum; the Last Alliance on its slopes in the Second Age.",
       "To be the forge and the sole means of the Ring’s destruction.",
       [
           "- **Forging.** S.A. c. 1600, the One is completed here.",
           "- **Last Alliance.** Gil-galad and Elendil fall in the war that reaches this land; Isildur takes the Ring but does not cast it in.",
           "- **The Crack of Doom.** Frodo claims the Ring; Gollum falls with it; the mountain erupts in the Ring’s ending.",
       ],
       [
           ("The One Ring", f"{P}/one-ring/", "Made and unmade here."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Bearer who cannot cast it away."),
           ("Gollum", f"{C}/gollum/", "Who takes it into the fire."),
           ("The Destruction of the One Ring", f"{E}/destruction-of-the-ring/", "The event of 25 March 3019."),
       ],
       "Orodruin is both geographical fact and moral terminus. The date of the unmaking becomes Gondor’s New Year in the book’s reckoning.")

    md("locations", "isengard", "Isengard",
       "A ring of stone around Orthanc, turned by Saruman from a Gondorian guard-post into pits of war, then flooded by the Ents.",
       ["fortress"], "Angrenost; the Wizard’s Vale", "Third Age",
       "Isengard is a circular rampart in a vale at the southern Misty Mountains, with the tower of Orthanc at its centre. Granted to Saruman, it becomes a factory of Orcs, wolves, and felled trees. The Ents break the ring and drown the pits; Orthanc itself stands.",
       "Fortress-vale",
       "Númenórean work (Angrenost) held by Gondor, then by Saruman.",
       "Saruman; Orthanc; Treebeard; the palantír of Orthanc.",
       "Once to guard the Gap of Rohan; under Saruman, to wage war on the Mark and seek the Ring.",
       [
           "- **Industrialization.** Trees fall; fires and wheels fill the circle.",
           "- **The flood.** Ents divert the Isen; the ring becomes a lake with Orthanc as an island.",
           "- **Aftermath.** Keys pass ultimately toward the King; Saruman is expelled.",
       ],
       [
           ("Saruman", f"{C}/saruman/", "Its fallen warden."),
           ("Treebeard", f"{C}/treebeard/", "Who unmakes the circle."),
           ("Orthanc", f"{L}/orthanc/", "The unbreakable tower within."),
       ],
       "Isengard’s fall is the Ents’ victory and Rohan’s strategic relief. It is distinct from Orthanc, which cannot be torn by Ent-hands.")

    md("locations", "fangorn", "Fangorn Forest",
       "Ancient woodland on Rohan’s border, home of the Ents, which marches on Isengard and sends Huorns to Helm’s Deep.",
       ["forest"], "Home of the Ents", "Elder Days to Third Age",
       "Fangorn is a remnant forest older than the surrounding kingdoms, named for Treebeard (Fangorn). Men call it haunted. Merry and Pippin discover that trees have shepherds. The wood’s intervention in the War is local and decisive.",
       "Forest / Ent-realm",
       "A survival of wider woods from earlier Ages; dwindled by axes and time.",
       "Treebeard; Ents; Huorns; Merry and Pippin as guests.",
       "To shelter the Ents and, when roused, to avenge felling by Isengard.",
       [
           "- **The Hobbits.** They meet Treebeard and catalyse the Entmoot.",
           "- **War.** Ents ruin Isengard; Huorns appear as a sudden wood at Helm’s Deep (book).",
       ],
       [
           ("Treebeard", f"{C}/treebeard/", "Shepherd of the wood."),
           ("Ents", f"{P}/ents/", "Its people."),
           ("Isengard", f"{L}/isengard/", "Object of their wrath."),
       ],
       "Fangorn is not a general in Gondor’s war; it is a remaining wilderness that still has a voice. After the axes stop, the book lets it go still again.")

    md("locations", "ithilien", "Ithilien",
       "Fair land between Anduin and the Mountains of Shadow, a ranger-march in wartime and a princedom of healing afterward.",
       ["gondor"], "Garden of Gondor", "Third Age",
       "Ithilien is Gondor’s garden-province east of the Great River, long fought over and partly deserted. Faramir’s Rangers move through it. Henneth Annûn is a hidden refuge. After Sauron’s fall it is granted to Faramir and Éowyn; Legolas later brings Elven gardeners.",
       "Province / march",
       "Part of Gondor from the Realms in Exile; declined as Minas Morgul’s threat grew.",
       "Faramir; Gondor; Frodo and Sam as captives then guests; Éowyn after the War.",
       "To be Gondor’s eastern beauty and a screen against Mordor.",
       [
           "- **War.** Ranger warfare; the Forbidden Pool; the decision about the Ring.",
           "- **Peace.** Restoration as a princedom of the Fourth Age.",
       ],
       [
           ("Faramir", f"{C}/faramir/", "Its wartime captain and later prince."),
           ("Gondor", f"{L}/gondor/", "The kingdom it belongs to."),
           ("Éowyn", f"{C}/eowyn/", "Who comes to heal there."),
       ],
       "Ithilien is the book’s image of victory as orchards, not only crowns. Cross-adaptation note: Faramir’s kindness here is stronger in the novel than in Jackson’s film.")

    md("locations", "weathertop", "Weathertop",
       "Ruined watchtower of Amon Sûl on the East Road where Frodo is stabbed by the Witch-king.",
       ["eriador", "ruin"], "Amon Sûl", "Third Age",
       "Weathertop is the high hill of Amon Sûl, once a great tower of Arnor holding a palantír. In Frodo’s day it is wind and broken stone, visible to enemies. The camp there leads to the Morgul-wound that Rivendell can only slow.",
       "Ruin / former watchtower",
       "A chief fortress of the North-kingdom; destroyed in the wars with Angmar.",
       "The Nazgûl; Aragorn as guide; Frodo as victim.",
       "Once to watch the Road and house a seeing-stone; in the Quest, a dangerous skyline.",
       [
           "- **The attack.** The Witch-king wounds Frodo; the chase to the Ford follows.",
       ],
       [
           ("The Witch-king of Angmar", f"{C}/witch-king/", "Who stabs Frodo here."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Bearer marked by a Morgul-knife."),
           ("The Nazgûl", f"{P}/nazgul/", "Hunters on the Road."),
       ],
       "Weathertop is the first true mark of the Shadow on the Ring-bearer in *The Fellowship of the Ring*. The palantír of Amon Sûl was lost with the North, not present in 3018.")

    md("locations", "cirith-ungol", "Cirith Ungol",
       "High pass into Mordor guarded by an orc-tower and by Shelob, chosen by Gollum as a path of betrayal.",
       ["mordor", "pass"], "Pass of the Spider", "Third Age",
       "Cirith Ungol is a pass over the Ephel Dúath into Mordor, with stairs, tunnels, and the lair of Shelob, an ancient spider. A tower of Orcs watches the pass. Gollum leads Frodo and Sam this way; Sam fights Shelob and later rescues Frodo from the tower.",
       "Mountain pass / fortress",
       "A western entry to Mordor used and watched by Sauron’s servants; Shelob predates his current war as a neighbor-hunger.",
       "Gollum; Shelob; Sam and Frodo; Orcs of the tower.",
       "To enter Mordor unseen by the Morannon; in Gollum’s intent, to murder and reclaim the Ring.",
       [
           "- **The tunnel.** Shelob stings Frodo; Sam wounds her with Sting and the Phial.",
           "- **The tower.** Orcs carry Frodo; Sam follows; the Hobbits escape in orc-gear.",
       ],
       [
           ("Gollum", f"{C}/gollum/", "Who chooses this path to betray them."),
           ("Samwise Gamgee", f"{C}/samwise-gamgee/", "Who fights in the tunnel and tower."),
           ("Mordor", f"{L}/mordor/", "The land beyond the pass."),
       ],
       "Cirith Ungol is the Quest’s most desperate hour. Shelob is not simply Sauron’s pet; the book treats her as an older appetite he finds useful.")

    md("locations", "grey-havens", "The Grey Havens",
       "Elven port of Mithlond on the Gulf of Lune, from which the Ring-bearers take ship into the West at the end of the Third Age.",
       ["elf-home", "sea"], "Mithlond", "Second Age to Fourth Age",
       "The Grey Havens are the Elven harbour of Mithlond, kept by Círdan the Shipwright. At the end of T.A. 3021, Gandalf, Elrond, Galadriel, Frodo, and Bilbo board a white ship. Sam watches it diminish. The Fourth Age of Men is already beginning behind them.",
       "Elven port",
       "Founded in the Second Age as the Lindon haven of the Eldar remaining in Middle-earth.",
       "Círdan; the departing Ring-bearers; Elves of Lindon.",
       "To keep ships for the Straight Road and the leave-taking of the Eldar.",
       [
           "- **The last ship of the story.** The keepers of the Three and the Hobbit Ring-bearers depart.",
           "- **Sam.** He returns to the Shire; much later, tradition says he sails from the same Havens.",
       ],
       [
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Who is granted passage to heal."),
           ("Gandalf", f"{C}/gandalf/", "Whose task in Middle-earth is done."),
           ("Galadriel", f"{C}/galadriel/", "Who at last returns West."),
           ("Elrond", f"{C}/elrond/", "Who leaves Arwen behind by her choice."),
       ],
       "The Havens close the novel. The Sea here is permission to rest, not a new adventure. Film condensation of the departure still rests on this canonical scene.")

    md("locations", "barad-dur", "Barad-dûr",
       "Sauron’s Dark Tower, founded with the Ring’s power and collapsing when the Ring is destroyed.",
       ["fortress", "mordor"], "The Dark Tower", "Second Age to Third Age",
       "Barad-dûr is Sauron’s fortress in Mordor, raised in the Second Age with the One Ring’s strength and therefore unable to stand when that Ring is gone. From it the Eye searches. Its fall is seen from the Field of Cormallen as a weather of ruin.",
       "Fortress",
       "Building began in the Second Age after the One was forged; it was broken after the Last Alliance and rebuilt in the Third Age.",
       "Sauron; Mordor; the One Ring as foundation-bond.",
       "Seat of the Dark Lord’s will and command.",
       [
           "- **Binding.** Its foundations are tied to the Ring.",
           "- **Fall.** 25 March 3019: the Tower collapses; armies of Mordor lose their unifying mind.",
       ],
       [
           ("Sauron", f"{C}/sauron/", "Its master."),
           ("Mordor", f"{L}/mordor/", "The land it dominates."),
           ("The One Ring", f"{P}/one-ring/", "Without which it cannot endure."),
       ],
       "Barad-dûr is will given battlements. The ‘Eye’ is the book’s image of Sauron’s attention; it should not be reduced to a searchlight gadget at the expense of that metaphor, nor expanded into a walking Sauron on the Pelennor (a film choice).")

    md("locations", "erebor", "Erebor",
       "The Lonely Mountain, Dwarf-kingdom restored after Smaug’s fall, whose people send Gimli to Rivendell and fight their own war in the North.",
       ["dwarf-home"], "The Lonely Mountain", "Third Age",
       "Erebor is the Dwarf-kingdom under the Lonely Mountain, recovered in T.A. 2941 after the death of Smaug. By the War of the Ring it is a restored ally too far to march to the Pelennor. Dale and Erebor wage war against Easterlings while Gondor burns; the appendices record this northern front.",
       "Dwarf-kingdom",
       "Founded by Thráin I; lost to Smaug; restored after the Quest of Erebor.",
       "Durin’s Folk; Gimli; Dáin II in the War; Dale as neighbor.",
       "A northern centre of Dwarven power and a second battlefield of the same war.",
       [
           "- **The Hobbit’s mountain.** Already a recovered kingdom by 3018–19.",
           "- **War of the Ring.** Under attack in the North; not present on the Pelennor.",
       ],
       [
           ("Gimli", f"{C}/gimli/", "Sent from this people to Rivendell."),
           ("Bilbo Baggins", f"{C}/bilbo-baggins/", "Whose adventure restored the Mountain."),
           ("Dwarves", f"{P}/dwarves/", "Its kindred."),
       ],
       "Erebor reminds the reader that the darkness was not a single battlefield. The main text only glances north; the appendices fill the war there.")

    md("locations", "mirkwood", "Mirkwood",
       "Vast eastern forest, once Greenwood the Great, darkened by Dol Guldur; home of Thranduil’s realm and of Legolas before the Quest.",
       ["forest"], "Greenwood the Great, darkened", "Third Age",
       "Mirkwood is a great forest east of the Anduin. It took a new name when a Necromancer (Sauron) sat in Dol Guldur. Spiders, darkness, and a wary Elvenking define the tales that pass through it. In the War the wood is assailed and later cleansed in name and in part.",
       "Forest / Elven realm",
       "Ancient Greenwood; shadow spreads from Dol Guldur in the later Third Age.",
       "Thranduil; Legolas; Sauron as Necromancer (earlier); Silvan Elves.",
       "Home of the Woodland Realm; a northern theatre of the same Shadow.",
       [
           "- **Darkening.** Dol Guldur’s influence; spiders and fear.",
           "- **War.** Assaults on the Woodland Realm; after Sauron’s fall, a measure of cleansing (appendices).",
       ],
       [
           ("Legolas", f"{C}/legolas/", "Prince of this realm."),
           ("Sauron", f"{C}/sauron/", "Whose Necromancer-presence named the wood."),
           ("Elves", f"{P}/elves/", "Thranduil’s Silvan people."),
       ],
       "Mirkwood is more central to *The Hobbit* than to the southern marches of *The Lord of the Rings*, but it remains Legolas’s origin and a named front of the War.")

    md("locations", "anduin", "The Anduin",
       "The Great River, road and border of the Fellowship’s boats, in whose waters Isildur once lost the Ring.",
       ["river"], "The Great River", "All Ages",
       "Anduin is the long river of Wilderland, running from the north toward the Mouths in the south. Lórien stands on its banks; Gondor and the east-march later claim it. The Argonath mark the old northern gate of Gondor. Isildur was slain in the Gladden Fields; the Ring was lost in these waters until Déagol found it.",
       "River",
       "A primary watercourse of Middle-earth through all Ages of the stories here told.",
       "The Fellowship; Gollum as a log in the water; Isildur’s disaster; Gondor.",
       "Highway, border, and hiding-place of the Ring for centuries.",
       [
           "- **Fellowship.** Boats from Lórien to Parth Galen.",
           "- **Breaking.** The company dissolves on its western shore near Amon Hen.",
           "- **History.** The Ring slept in the river-mud of the Gladden.",
       ],
       [
           ("The Breaking of the Fellowship", f"{E}/breaking-of-the-fellowship/", "On its banks at Parth Galen."),
           ("The One Ring", f"{P}/one-ring/", "Lost here by Isildur."),
           ("Gondor", f"{L}/gondor/", "Whose old kings the Argonath still name."),
       ],
       "The Anduin ties Second Age failure to Third Age Quest. It is geography as memory.")

    md("locations", "orthanc", "Orthanc",
       "Unbreakable tower of four piers of black stone at Isengard’s centre, proof against Ent-wrath, later returning toward Gondor’s keeping.",
       ["tower"], "The unbreakable tower", "Early Third Age to Fourth Age",
       "Orthanc is a tower of Númenórean (or similarly ancient) black stone in the midst of Isengard. Ents cannot break it. Saruman argues from its roof and is mastered through its palantír. After the flood it remains a needle in a lake; keys pass, in the end, to the King.",
       "Tower",
       "Built as part of Gondor’s defence of the Gap; later occupied by Saruman.",
       "Isengard; Saruman; the palantír; Aragorn as later rightful holder of the keys.",
       "Stronghold and seeing-place; unlike the ring-wall, it survives the Ents.",
       [
           "- **Saruman’s seat.** Voice, palantír, and pride.",
           "- **After the flood.** Isolation; expulsion of the wizard; transfer of authority toward Gondor/the King.",
       ],
       [
           ("Isengard", f"{L}/isengard/", "The circle around it."),
           ("Saruman", f"{C}/saruman/", "Who rented it as a throne."),
           ("Gondor", f"{L}/gondor/", "Original and later keeper in the King’s name."),
       ],
       "Orthanc outlasts the villain who occupied it. That distinction—tower versus ring—is book-accurate and easy to blur in adaptation.")

    write_extra_locations(md, C, L, E, P)


def write_events(md, C, L, E, P):
    md("events", "council-of-elrond", "The Council of Elrond",
       "A gathering of the Free Peoples in Rivendell that hears the Ring’s history and chooses destruction over hiding, sending, or using it.",
       ["quest", "rivendell"], "Rivendell, 25 October T.A. 3018", "Third Age 3018",
       "The Council of Elrond is a meeting in Imladris at which Elves, Dwarves, Men, and a Hobbit hear the truth of the One Ring. Alternatives—use, burial, sending over Sea—are rejected. Frodo offers to take the Ring to Mordor; the Fellowship is composed as a guard for that errand.",
       "Event (council)",
       "Convened by Elrond after Frodo’s arrival and the gathering of messengers already bound for Imladris.",
       "Elrond; Frodo; Gandalf; Boromir; Gimli; Legolas; Aragorn; other counsellors of the West.",
       "To decide the fate of the Ring and to name a company for the southward road.",
       [
           "- **History rehearsed.** The Last Alliance, Isildur, Gollum, and Bilbo’s finding.",
           "- **Decision.** The Ring must be unmade in Orodruin.",
           "- **The Nine Walkers.** A Hobbit bearer with companions of several kindreds, matching the Nine Riders in number.",
       ],
       [
           ("Elrond", f"{C}/elrond/", "Host and convener."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Who accepts the burden."),
           ("Rivendell", f"{L}/rivendell/", "Place of the Council."),
           ("The One Ring", f"{P}/one-ring/", "Object of the debate."),
       ],
       "The Council is the Quest’s constitutional moment. It is not a battle; it is a choice that makes later battles possible. The film compresses speakers; the book’s argument with Boromir is fuller.")

    md("events", "fellowship-of-the-ring", "The Fellowship of the Ring",
       "The company of Nine Walkers named in Rivendell to escort the Ring south, broken at Parth Galen by treachery, death, and Frodo’s choice to go alone.",
       ["quest"], "Nine Walkers against Nine Riders", "Third Age 3018–3019",
       "The Fellowship of the Ring is the nine companions appointed at Rivendell: Frodo, Sam, Merry, Pippin, Aragorn, Boromir, Legolas, Gimli, and Gandalf. They are a living counter to the Nazgûl. The company fails as a single body and succeeds as a scattering of necessary errands.",
       "Event / company (quest)",
       "Formed at the Council of Elrond, 25 October 3018; broken 26 February 3019.",
       "Its nine members; Elrond as appointer; the Ring as secret.",
       "To protect the Ring-bearer on the road to Mordor.",
       [
           "- **The Road.** Caradhras fails them; Moria takes Gandalf; Lórien heals and tests; Anduin carries them south.",
           "- **Breaking.** Boromir falls to the Ring’s lure; Frodo leaves with Sam; Merry and Pippin are captured; the Three Hunters follow.",
       ],
       [
           ("The Breaking of the Fellowship", f"{E}/breaking-of-the-fellowship/", "Its dissolution."),
           ("The Council of Elrond", f"{E}/council-of-elrond/", "Its origin."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "The bearer at its centre."),
       ],
       "After Amon Hen the War has many fronts and no shared campfire. The book’s structure from that point is the proof that the breaking was also a strategy, intended or not.")

    md("events", "breaking-of-the-fellowship", "The Breaking of the Fellowship",
       "Boromir’s fall to the Ring, Frodo’s flight, Boromir’s death, and the capture of Merry and Pippin at Parth Galen and Amon Hen.",
       ["quest"], "Parth Galen and Amon Hen, 26 February T.A. 3019", "Third Age 26 February 3019",
       "The Breaking of the Fellowship is the cluster of disasters on the western shore of Anduin near Amon Hen. Frodo puts on the Ring to escape Boromir; Uruk-hai attack; Boromir dies defending Merry and Pippin; Aragorn chooses to hunt the captives rather than follow Frodo, whose road he trusts to remain hidden.",
       "Event (crisis)",
       "Occurs at the lawn of Parth Galen and the hill of Amon Hen at the breaking of the company’s southward boat-journey.",
       "Frodo; Sam; Boromir; Merry; Pippin; Aragorn, Legolas, Gimli; Saruman’s Uruk-hai.",
       "It ends the Fellowship as a unit and splits the narrative into Mordor, Rohan, and Gondor.",
       [
           "- **The temptation.** Boromir tries to seize the Ring.",
           "- **The choice.** Frodo leaves; Sam swims after him.",
           "- **The death.** Boromir’s last stand; the Three Hunters take up the captives’ trail.",
       ],
       [
           ("Boromir", f"{C}/boromir/", "Whose fall and death define the hour."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Who chooses solitude (with Sam)."),
           ("Aragorn", f"{C}/aragorn/", "Who elects the prisoners’ trail."),
           ("The Fellowship of the Ring", f"{E}/fellowship-of-the-ring/", "The company that ends here."),
       ],
       "Both resulting roads prove necessary: Hobbits into Mordor, hunters into Rohan. Aragorn’s choice is canonically agonized, not casual.")

    md("events", "battle-of-helms-deep", "The Battle of Helm’s Deep",
       "Rohan’s night-stand against Isengard at the Hornburg, ended by dawn, Gandalf, Erkenbrand, and the Huorns of Fangorn.",
       ["battle", "rohan"], "The Hornburg, 3–4 March T.A. 3019", "Third Age 3019",
       "The Battle of the Hornburg is Saruman’s attempt to end the Mark in one blow so Rohan cannot aid Gondor. The Deeping Wall is breached; the keep holds. At dawn Gandalf brings Erkenbrand, and Huorns destroy the fleeing host. Victory here is the first loud defeat of the White Hand.",
       "Event (battle)",
       "Fought at Helm’s Deep in Rohan, 3–4 March 3019.",
       "Théoden; Aragorn; Éomer; Gimli; Legolas; the people in the hold; Saruman’s army.",
       "To preserve Rohan as a fighting kingdom.",
       [
           "- **Night of wall-breaking.** Fire and numbers.",
           "- **Dawn.** Charge, riders from the west, and a wood that should not be there.",
       ],
       [
           ("Helm’s Deep", f"{L}/helms-deep/", "The fortress."),
           ("Théoden", f"{C}/theoden/", "King in the keep."),
           ("Saruman", f"{C}/saruman/", "Author of the host."),
           ("Rohan", f"{L}/rohan/", "The land at stake."),
       ],
       "The battle frees Théoden to ride south. Elven infantry from Lórien are a film addition, not novel canon.")

    md("events", "pelennor-fields", "The Battle of the Pelennor Fields",
       "The field-battle before Minas Tirith: Rohan’s charge, the Witch-king’s fall, and Aragorn’s coming in the black ships.",
       ["battle", "gondor"], "15 March T.A. 3019", "Third Age 3019",
       "The Battle of the Pelennor Fields is the great engagement before Minas Tirith on 15 March 3019. It includes the charge of the Rohirrim, the death of Théoden, the slaying of the Witch-king by Éowyn and Merry, and the turning of the Corsair ships, which bear Aragorn and the southern levies. The field is won; Mordor is not.",
       "Event (battle)",
       "Fought on the Pelennor, the townlands of Minas Tirith, during the siege.",
       "Théoden; Éowyn; Merry; Éomer; the Witch-king; Aragorn; Gondor’s defenders; Haradrim and Easterlings among the Enemy.",
       "To relieve the White City and break the first host of the invasion.",
       [
           "- **The charge.** Rohan arrives at dawn (in the book’s timing of the ride’s end).",
           "- **The wraith.** Prophecy fulfilled by a woman and a hobbit.",
           "- **The ships.** What seemed Corsairs are the Heir of Isildur and allies.",
           "- **After.** The Captains still must feint at the Morannon.",
       ],
       [
           ("Minas Tirith", f"{L}/minas-tirith/", "The city relieved."),
           ("Théoden", f"{C}/theoden/", "Who dies in the charge’s crisis."),
           ("Éowyn", f"{C}/eowyn/", "Who slays the Witch-king."),
           ("Aragorn", f"{C}/aragorn/", "Who arrives from the river."),
       ],
       "Pelennor is the War made visible. Oliphaunts, wraiths, and the Harlond are book-canon. The victory is incomplete by design: two Hobbits still crawl in Mordor.")

    md("events", "destruction-of-the-ring", "The Destruction of the One Ring",
       "The unmaking of Sauron’s Ring in the fire of its forging, accomplished when Gollum seizes it at the brink after Frodo claims it.",
       ["quest", "mordor"], "Sammath Naur, 25 March T.A. 3019", "Third Age 3019",
       "The Destruction of the One Ring is the climax of the Quest. At the Crack of Doom Frodo claims the Ring. Gollum bites it from his hand and falls into the fire. Sauron’s power fails; Barad-dûr falls; the Nazgûl go out. The date becomes Gondor’s New Year.",
       "Event (quest climax)",
       "Orodruin, 25 March 3019, in the Sammath Naur.",
       "Frodo; Gollum; Sam as witness; Sauron as the will unmade.",
       "To end the Third Age’s defining weapon and the Dark Lord’s ability to return in strength.",
       [
           "- **The claim.** No counsel of Elrond assumed the bearer would remain himself.",
           "- **The fall.** Gollum’s joy, murder, and death coincide.",
           "- **The consequence.** War-engines of Mordor stop; healing and scouring remain.",
       ],
       [
           ("Mount Doom", f"{L}/mount-doom/", "The only sufficient fire."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Bearer who cannot let go."),
           ("Gollum", f"{C}/gollum/", "Unwilling instrument of unmaking."),
           ("The One Ring", f"{P}/one-ring/", "What is destroyed."),
       ],
       "The book is explicit that the Ring is not thrown in by a still-heroic act of will at the last second. Mercy earlier in the plot supplies the missing act. Jackson’s films keep this structure at Orodruin.")

    md("events", "crowning-of-elessar", "The Crowning of Elessar",
       "Aragorn’s coronation as King of Gondor and Arnor, restoring Elendil’s line after a thousand years of Stewards.",
       ["gondor", "kingship"], "Minas Tirith, 1 May T.A. 3019", "Third Age 3019",
       "The Crowning of Elessar is the ritual restoration of the kingship in Minas Tirith on 1 May 3019. Gandalf sets the crown on Aragorn. Faramir yields the white rod of the Stewards. Midsummer brings Arwen; the marriage seals the new age politically and personally.",
       "Event (coronation)",
       "The Court of the Fountain, Minas Tirith, 1 May 3019; wedding at Midsummer.",
       "Aragorn; Gandalf; Faramir; the people of Gondor; Arwen at the later wedding.",
       "To end the Steward’s rule as sovereign fact and to begin the Reunited Kingdom.",
       [
           "- **The crown.** A white tree is found; a people remembers that it was waiting.",
           "- **The wedding.** Elves diminish by love; Men rise by the same, in the book’s typology.",
       ],
       [
           ("Aragorn", f"{C}/aragorn/", "The crowned king."),
           ("Minas Tirith", f"{L}/minas-tirith/", "Place of the rite."),
           ("Arwen Undómiel", f"{C}/arwen/", "Queen thereafter."),
           ("Gandalf", f"{C}/gandalf/", "Who sets the crown."),
       ],
       "The crowning is ritual after ruin. It does not itself destroy Sauron—that has already occurred—but it organizes the peace.")

    md("events", "scouring-of-the-shire", "The Scouring of the Shire",
       "The Hobbits’ return to a homeland fenced and ruled by ruffians in Saruman’s employ, and their uprising culminating at Bywater.",
       ["shire", "aftermath"], "November T.A. 3019", "Third Age 3019",
       "The Scouring of the Shire is the last military action of the book: the four Travellers find the Shire industrialized in miniature under Sharkey (Saruman). They raise the countryside. The Battle of Bywater is small and sufficient. Saruman is killed by Wormtongue at Bag End; Wormtongue is shot as he flees.",
       "Event (uprising)",
       "The Shire, chiefly November 3019, after the Hobbits’ return from the War.",
       "Frodo, Sam, Merry, Pippin; ruffians; Saruman; Gríma.",
       "To free the homeland the Quest was fought to save, proving the Hobbits can do that work themselves.",
       [
           "- **Occupation.** Ugly mills, felled avenues, rules and lockhouses.",
           "- **Bywater.** A pitched fight the Shire wins.",
           "- **Bag End.** Saruman’s death on the doorstep; Frodo forbids killing him just before Gríma strikes.",
       ],
       [
           ("The Shire", f"{L}/the-shire/", "The land scoured."),
           ("Saruman", f"{C}/saruman/", "Sharkey, the diminished wizard."),
           ("Samwise Gamgee", f"{C}/samwise-gamgee/", "Who helps heal the damage after."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Who will not let the Shire start its new peace with murder, yet cannot prevent Saruman’s end."),
       ],
       "The Scouring is canonical in the novel and omitted from the theatrical films. It is the book’s insistence that even saved worlds must be saved again at home.")

    md("events", "last-alliance", "The Last Alliance",
       "The war of Elves and Men at the end of the Second Age that threw Sauron down, when Isildur cut the Ring from his hand and would not destroy it.",
       ["second-age", "war"], "End of the Second Age", "Second Age 3430–3441",
       "The Last Alliance of Elves and Men is the war led by Gil-galad and Elendil against Sauron. It is ‘last’ because such a joining of the two kindreds in full strength will not come again. On the slopes of Orodruin the High King and Elendil fall; Isildur takes the Ring as weregild and refuses the fire. The Third Age is the bill for that unmade choice.",
       "Event (war)",
       "Second Age 3430–3441, ending on Orodruin.",
       "Gil-galad; Elendil; Isildur; Elrond as herald; Sauron.",
       "To overthrow Sauron; it succeeds militarily and fails to unmake the Ring.",
       [
           "- **The siege of Barad-dûr.** Seven years in the annalistic account.",
           "- **The last combat.** Sauron is thrown down; the Ring is cut away, not destroyed.",
           "- **Memory.** Elrond tells this failure at his Council in 3018.",
       ],
       [
           ("Sauron", f"{C}/sauron/", "The enemy overthrown but not ended."),
           ("The One Ring", f"{P}/one-ring/", "Taken, not unmade."),
           ("Elrond", f"{C}/elrond/", "Witness who remembers the fire refused."),
           ("Mount Doom", f"{L}/mount-doom/", "Where the refusal happens."),
       ],
       "The Last Alliance is prologue to the entire Third Age. Film prologue compresses it; the moral content—Isildur’s refusal—is the same.")

    md("events", "paths-of-the-dead", "The Paths of the Dead",
       "Aragorn’s journey under the Haunted Mountain to command the oath-breakers, winning the Corsair fleet for Gondor.",
       ["dunharrow", "kingship"], "Aragorn’s summons, T.A. 3019", "Third Age 3019",
       "The Paths of the Dead are the dark road from Dunharrow through the mountains, haunted by the shades of Men who broke oath to Isildur. Aragorn, with the Grey Company, Legolas, and Gimli, takes that road because the Pelennor will not wait for ordinary marches. At Erech the oath is fulfilled; at Pelargir the Dead take the Corsair ships, then are released.",
       "Event (summoning / march)",
       "Early March 3019, from Rohan through the White Mountains to Lebennin.",
       "Aragorn; the Dúnedain of the North; Legolas; Gimli; the Dead of Dunharrow.",
       "To bring a force to the southern coast in time to lift the siege from the river.",
       [
           "- **The Door.** Only the heir of Isildur can take the road in hope.",
           "- **Erech.** The Stone of Erech; the oath remembered.",
           "- **Pelargir.** The fleet is seized; the Dead are freed; the living still have a field to fight.",
       ],
       [
           ("Aragorn", f"{C}/aragorn/", "Who summons them."),
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Which his timely ships decide."),
           ("Legolas", f"{C}/legolas/", "Companion on the dark road."),
           ("Gimli", f"{C}/gimli/", "Who later admits fear of that road."),
       ],
       "The Dead are a weapon no Steward would touch. The book releases them after Pelargir; they do not fight on the Pelennor as a ghost-army in the novel (the film extends their presence onto the field).")

    write_extra_events(md, C, L, E, P)


def write_kindreds(md, C, L, E, P):
    md("kindreds", "hobbits", "Hobbits",
       "A shy agrarian people of the Shire and Bree-land, overlooked by the great, and therefore suited to carry a burden that magnifies the will to dominate.",
       ["kindred"], "The Halflings; the Little People", "Third Age",
       "Hobbits are a mortal people related in origin to Men, small in stature, concentrated in the Shire and in Bree-land in the late Third Age. Their courage, when it appears, often looks like stubbornness. The Wise guess that a Hobbit’s small desire is harder for the Ring to inflame into empire—a guess that is almost true, and the almost is the drama of Frodo and Sméagol.",
       "People / kindred",
       "Their early history is sketched in the prologue: migrations from the upper Vales of Anduin; three strains (Harfoots, Stoors, Fallohides).",
       "The Shire; Bree; the four Travellers; Bilbo; Gollum as a Stoor-deviant.",
       "In the War, to bear or resist the Ring; ordinarily, to farm, feast, and keep genealogies.",
       [
           "- **Character.** Meals, family names, suspicion of boats and of the Sea (mostly).",
           "- **The War.** Four Hobbits walk into history; a countryside wakes late in the Scouring.",
       ],
       [
           ("The Shire", f"{L}/the-shire/", "Principal homeland."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Chief Ring-bearer of the War."),
           ("Bilbo Baggins", f"{C}/bilbo-baggins/", "Finder of the Ring."),
       ],
       "Hobbits are Tolkien’s narrative instrument for seeing epic from near the ground. They are not children; the book is firm on that point even when the films infantilize Pippin at times.")

    md("kindreds", "elves", "Elves",
       "The Firstborn, immortal within the life of the world, already fading in the Third Age, whose last great acts are counsel, refuge, and departure.",
       ["kindred"], "The Firstborn; the Eldar", "All Ages",
       "Elves are the Elder Kindred, awake before Men, bound to the world until its end. In the Third Age they are a remnant: woodland princes, Noldorin exiles, mariners of Lindon. Their Rings preserve rather than conquer. In the War they fight at need, but their deeper role is memory—and leave-taking.",
       "People / kindred",
       "Firstborn of Ilúvatar’s Children; divided historically into Eldar and Avari, and among the Eldar into several kindreds (Vanyar, Noldor, Teleri/Sindar, and Silvan groups in the narrative’s geography).",
       "Galadriel; Elrond; Legolas; the Grey Havens; Lothlórien; Rivendell; Mirkwood.",
       "To remember the world’s making and to resist Sauron without claiming his methods; ultimately to depart or fade.",
       [
           "- **Third Age posture.** Preservation (the Three), hidden woods, dwindling numbers.",
           "- **War.** Counsel at Rivendell; a realm in Lórien; Legolas in the field; northern fighting in the appendices.",
           "- **End.** The keepers of the Three sail; the age of Elves in Middle-earth closes.",
       ],
       [
           ("Galadriel", f"{C}/galadriel/", "Greatest of the Noldor remaining in the story’s West."),
           ("Elrond", f"{C}/elrond/", "Half-elven who chose the Eldar."),
           ("Legolas", f"{C}/legolas/", "Woodland representative in the Fellowship."),
           ("The Grey Havens", f"{L}/grey-havens/", "Port of departure."),
       ],
       "Elves in *The Lord of the Rings* are not a generic shining army. Distinctions of kindred and the theme of fading are canonical. Immortality here is not invulnerability.")

    md("kindreds", "dwarves", "Dwarves",
       "A hardy people of stone and craft, the Children of Aulë, makers of halls and long memories, whose representative in the Fellowship becomes an Elf-friend.",
       ["kindred"], "Khazâd; the Children of Aulë", "All Ages",
       "Dwarves are a mortal kindred (long-lived, not Elven-immortal) made by Aulë and given life by Ilúvatar in the wider legendarium. They mine, remember insults, and love work that outlasts a lifespan. Their Seven Rings kindled greed more than wraith-life. Moria’s doom was a Balrog, not a slow fade of the Elvish sort.",
       "People / kindred",
       "Awoke in the Elder Days in their appointed places; Durin’s Folk are central to this site’s Third Age story.",
       "Gimli; Erebor; Moria; the Glittering Caves after the War.",
       "To craft, to endure, and in the War to stand with the Fellowship in the person of Gimli.",
       [
           "- **Character.** Stone, metal, secrecy of their inner names, tenacity.",
           "- **The War.** Gimli in the South; Erebor and Dale in the North (appendices).",
           "- **Fourth Age.** Still under mountains, less sung but not gone.",
       ],
       [
           ("Gimli", f"{C}/gimli/", "Durin’s Folk in the Fellowship."),
           ("Moria", f"{L}/moria/", "Greatest mansion, in ruin."),
           ("Erebor", f"{L}/erebor/", "Restored kingdom of the North."),
       ],
       "Dwarves are not comic relief in the novel, though they have grim humor. Gimli’s path—Galadriel, Legolas, Aglarond, the West—is unusual, not typical of all Khazâd.")

    md("kindreds", "men", "Men",
       "The Followers, mortal peoples of many kingdoms—Dúnedain, Rohirrim, Easterlings, Haradrim—whose Age begins in earnest when the Elves depart.",
       ["kindred"], "The Followers; the Secondborn", "All Ages",
       "Men are the Secondborn, mortal, heirs of the world’s future in Tolkien’s scheme. They are the most divided people in the War: Númenor’s heirs, Rohan’s riders, and nations under the Shadow. The War of the Ring is the last time Elves and Dwarves stand so near the centre of the West’s story.",
       "People / kindred",
       "Awoke with the rising of the Sun in the First Age (legendarium); spread through all lands of the narratives.",
       "Aragorn; Gondor; Rohan; the Nazgûl as enslaved Men; subject kingdoms of Sauron.",
       "To inherit Middle-earth’s dominion in the Fourth Age, for good or ill.",
       [
           "- **Dúnedain.** Long life, memory, decline, restoration under Elessar.",
           "- **Rohan.** Horse-lords, oath-keepers, not Númenórean by blood.",
           "- **The East and South.** Peoples who fight for Sauron; the book gives them little interiority, which is a limit of its viewpoint, not proof they are monstrous by nature in every individual.",
       ],
       [
           ("Aragorn", f"{C}/aragorn/", "Restored king of the Dúnedain."),
           ("Gondor", f"{L}/gondor/", "South-kingdom."),
           ("Rohan", f"{L}/rohan/", "The Mark."),
           ("The Nazgûl", f"{P}/nazgul/", "Men who took Rings and faded."),
       ],
       "After the Elves’ departure, the problems of Middle-earth become, more and more, the problems of Men. That is the Fourth Age’s premise.")

    md("kindreds", "ents", "Ents",
       "Tree-herds whose language is slow and whose wrath, once gathered, unmakes a wizard’s fortress.",
       ["kindred"], "Onodrim; the Shepherds of the Trees", "Elder Days to Third Age",
       "Ents are a race of tree-herds, made (in the legendarium) to keep the woods from others’ axes. They lose the Entwives and, with them, a future of children. By the War they are a remnant that can still surprise a world that has filed them under folklore. Their march is not cavalry but landscape choosing a side.",
       "People / kindred",
       "Awoke in the Elder Days with the forests they were to shepherd.",
       "Treebeard; Fangorn; the Entmoot; Isengard as target.",
       "To protect trees; in 3019, to destroy Saruman’s pits.",
       [
           "- **Slowness.** Entish is a long language; decisions take days.",
           "- **The march.** Isengard is flooded; Huorns intervene at Helm’s Deep.",
           "- **Diminution.** Without Entwives, they expect to dwindle.",
       ],
       [
           ("Treebeard", f"{C}/treebeard/", "Eldest in the narrative."),
           ("Fangorn Forest", f"{L}/fangorn/", "Their remnant home."),
           ("Isengard", f"{L}/isengard/", "Unmade by their assault."),
       ],
       "Ents are unique to this war’s strangeness. They are not allegory for a modern political party; they are a mythic answer to industrialized felling, written before that vocabulary was common.")

    md("kindreds", "orcs", "Orcs",
       "A numerous, cruel soldiery bred for war, divided by masters and hatreds, the rank-and-file of Mordor and Isengard.",
       ["kindred", "shadow"], "Goblins; the hosts of the Dark Lord", "First Age to Third Age",
       "Orcs are the ordinary horror of the wars of the legendarium: not unique like the Ring, but a system of fear, breeding pits, and stolen crafts. They quarrel among themselves, which twice aids the Hobbits inside Mordor. Uruk-hai are Saruman’s (and in Mordor, Sauron’s) larger, sun-tolerant soldiers. The published *Lord of the Rings* does not settle a single metaphysical origin-story with scholastic finality; it shows them as made for cruelty and war.",
       "People / soldiery of the Shadow",
       "Present from the First Age in Morgoth’s wars; multiplied under Sauron and Saruman.",
       "Sauron; Saruman; Cirith Ungol’s garrison; the hosts at the Black Gate and Helm’s Deep.",
       "To provide mass armies for the Dark Lords and for Saruman’s imitation of them.",
       [
           "- **Faction.** Mordor Orcs, Isengard Uruks, Moria’s goblins—often mutually hostile.",
           "- **The Quest.** Their infighting lets Sam and Frodo slip through.",
       ],
       [
           ("Saruman", f"{C}/saruman/", "Breeder of Uruk-hai at Isengard."),
           ("Sauron", f"{C}/sauron/", "Master of the greater hosts."),
           ("Isengard", f"{L}/isengard/", "Factory of the White Hand’s soldiers."),
           ("Mordor", f"{L}/mordor/", "Principal reservoir of the Eye’s armies."),
       ],
       "The chronicle does not linger on Orcish inner life. It shows enough to make the factories of Isengard and the tower of Cirith Ungol feel populated—and doomed when their masters fall.")

    md("kindreds", "istari", "The Istari",
       "Five Maiar sent in the shapes of aged Men to contest Sauron by stirring resistance, not by matching power with power.",
       ["maiar", "order"], "The Wizards", "Third Age",
       "The Istari are an order of Wizards: Maiar clad as old Men, forbidden to dominate the peoples of Middle-earth or to match Sauron force for force. That rule is the test. Gandalf keeps it; Saruman breaks it; Radagast turns aside to beasts and birds; the two Blue Wizards pass out of the western tale (their fates are sketched only in later notes, not in *The Lord of the Rings* narrative).",
       "Order (Maiar in mortal form)",
       "Sent about T.A. 1000 by the Valar (legendarium; the novel shows the result, not the Valinorean debate).",
       "Gandalf; Saruman; Radagast; the Blue Wizards (named in other texts); the White Council.",
       "To kindle the Free Peoples’ own courage against Sauron.",
       [
           "- **The charter.** Counsel, not empire.",
           "- **The failure.** Saruman’s voice, pits, and ring-lore.",
           "- **The fulfilment.** Gandalf the White completing the office Saruman abandoned.",
       ],
       [
           ("Gandalf", f"{C}/gandalf/", "Who keeps the charge."),
           ("Saruman", f"{C}/saruman/", "Who breaks it."),
       ],
       "A wizard’s staff is office as much as weapon. When Saruman’s is broken, the office has already been empty for years. The novel is not a treatise on all five; it is a story of two.")

    md("kindreds", "nazgul", "The Nazgûl",
       "Nine kings of Men who took Rings from Sauron and faded into enslaved terror, the Dark Lord’s most trusted hunters.",
       ["wraiths", "shadow"], "The Nine; the Ringwraiths", "Second Age to Third Age",
       "The Nazgûl are the Nine, Men who accepted Rings of Power and became wraiths wholly subject to the One. They smell the Ring, unmake courage by nearness, and serve as captains and hunters. Their chief is the Witch-king. When he falls, the others continue until the Ring is cut from the world; then they go out like flames deprived of oil.",
       "Enslaved wraiths (formerly Men)",
       "Second Age recipients of nine Rings; their mortal names are not given in *The Lord of the Rings*.",
       "The Witch-king; Sauron; the One Ring; Weathertop; Minas Morgul; the Pelennor.",
       "To hunt the Ring and to command Sauron’s armies as terror given shape.",
       [
           "- **Fading.** Power first, then a life that is not life.",
           "- **The Hunt.** The Black Riders in Eriador; winged mounts later in the War.",
           "- **End.** Destruction of the One unmakes their remaining hold on existence.",
       ],
       [
           ("The Witch-king of Angmar", f"{C}/witch-king/", "Their lord."),
           ("Sauron", f"{C}/sauron/", "Their master."),
           ("The One Ring", f"{P}/one-ring/", "The power that binds them."),
           ("Weathertop", f"{L}/weathertop/", "Where they wound Frodo."),
       ],
       "The Nine are what the Ring promises Men. They are not independent Dark Lords. Film visibility (faces, or none) varies; the book stresses hood, voice, and the wound of the unseen blade.")

    md("kindreds", "one-ring", "The One Ring",
       "Sauron’s master-ring, a tool of domination containing much of his native power, which unmakes him when it is unmade.",
       ["artifact", "ring"], "Isildur’s Bane; the Precious", "Second Age to Third Age",
       "The One Ring is the master-ring forged by Sauron in Orodruin to govern the other Rings of Power. It contains a great part of his strength. It lengthens life by stretching it thin and offers each bearer a kingdom cut to that bearer’s hunger. Destroying it is an anti-quest: not to win an object but to lose one on purpose.",
       "Relic / Ring of Power",
       "Forged in the Chambers of Fire about S.A. 1600; cut from Sauron by Isildur in S.A. 3441; lost in Anduin; found by Déagol; taken by Sméagol; taken by Bilbo; borne by Frodo; destroyed 25 March T.A. 3019.",
       "Sauron; Isildur; Gollum; Bilbo; Frodo; the Three, Seven, and Nine as the system it was meant to rule.",
       "To dominate the wearers of the other Rings and to embody Sauron’s will to order the world by owning it.",
       [
           "- **Deceit of Eregion.** The One is Sauron’s secret completion of the ring-craft he taught as Annatar.",
           "- **Isildur’s Bane.** Taken as weregild, not cast into the fire.",
           "- **The long interval.** River, cave, Hobbit-hole, Quest.",
           "- **Unmaking.** Only Orodruin’s fire suffices; the bearer at the end cannot will the loss.",
       ],
       [
           ("Sauron", f"{C}/sauron/", "Its maker, diminished without it."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Its last intended destroyer, who claims it instead."),
           ("Gollum", f"{C}/gollum/", "Whose seizure completes the unmaking."),
           ("The Destruction of the One Ring", f"{E}/destruction-of-the-ring/", "The end of its history."),
       ],
       "The Ring is a character by another name in critical shorthand, but it is not a speaking person in the text. Middle-earth’s Third Age is the interval between cutting it from a hand and putting it back into fire. Its cultural afterlife in the real world is vast; this page records only the legendarium’s canon.")


if __name__ == "__main__":
    main()
