"""Additional encyclopedia entries — imported by gen_entries.py."""


def write_extra_characters(md, C, L, E, P):
    md("characters", "grima-wormtongue", "Gríma Wormtongue",
       "Counsellor of Théoden who poisons the king's counsel for Saruman and is slain at Bag End during the Scouring of the Shire.",
       ["human", "rohan", "traitor"], "Wormtongue; Saruman's spy", "Third Age",
       "Gríma son of Gálmód is a Man of Rohan who serves as Théoden's counsellor while secretly answering to Saruman. His whispers isolate the king, weaken the Mark, and exile Éomer. Exposed by Gandalf at Edoras, he flees to Isengard and later to the Shire as Sharkey's lieutenant.",
       "Character (Man of Rohan; traitor)",
       "Born in Rohan; rose to the king's ear before the War of the Ring.",
       "Théoden; Saruman; Éomer; Éowyn; the Shire (late).",
       "To keep Rohan passive while Isengard prepares war; later to enforce petty tyranny in the Shire.",
       [
           "- **The poisoned court.** He argues against aid, against Gandalf, and against Éomer's loyalty.",
           "- **Edoras.** Gandalf restores Théoden; Gríma is cast out and rides to Orthanc.",
           "- **Sharkey's man.** In the Shire he helps run the ruffian regime until he kills Saruman and is killed himself.",
       ],
       [
           ("Théoden", f"{C}/theoden/", "King he bent and betrayed."),
           ("Saruman", f"{C}/saruman/", "Master he served in secret."),
           ("The Scouring of the Shire", f"{E}/scouring-of-the-shire/", "Where his end comes at Bag End."),
           ("Edoras", f"{L}/edoras/", "Court he ruled by whispers."),
       ],
       "Gríma is the book's image of counsel turned to venom. His death at Bag End closes Saruman's Shire plot in the novel.")

    md("characters", "shelob", "Shelob",
       "Ancient great spider of the Ephel Dúath who stings Frodo and is wounded by Sam in the pass above Minas Morgul.",
       ["monster"], "Her Ladyship; the last child of Ungoliant", "First Age to Third Age",
       "Shelob is a monstrous spider dwelling in the tunnels above the Winding Stair and Cirith Ungol. Gollum leads the Hobbits to her as a trap. She stings Frodo; Sam fights her with Sting and the Phial of Galadriel. She survives wounded—a horror older than Sauron's present rule.",
       "Character (monster / ancient evil)",
       "Spawn of Ungoliant in legend; long resident in the mountains of Mordor's border.",
       "Gollum; Frodo; Sam; Cirith Ungol; Orcs of the tower who loot Frodo after.",
       "To feed on passers-by; narratively to break the Ring-bearer and hand him to the tower.",
       [
           "- **The lair.** Tunnels, webs, and bones under the pass Gollum knows.",
           "- **The sting.** Frodo falls as if dead; Sam takes the Ring briefly.",
           "- **The fight.** Sam wounds her; she retreats. Orcs find Frodo and carry him to the tower.",
       ],
       [
           ("Gollum", f"{C}/gollum/", "Who betrayed the Hobbits to her."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Ring-bearer she stings."),
           ("Samwise Gamgee", f"{C}/samwise-gamgee/", "Who drives her off and rescues him."),
           ("Cirith Ungol", f"{L}/cirith-ungol/", "Pass she haunts."),
       ],
       "Shelob is not Sauron's servant but a shared predator. The book treats her as a leftover evil, like the Balrog in Moria—ancient, hungry, and indifferent to the War's politics.")

    md("characters", "glorfindel", "Glorfindel",
       "High Elf of Rivendell who meets Frodo on the Road and whose prophecy names the Witch-king's doom.",
       ["elf", "noldor"], "Lord of the House of the Golden Flower", "First Age to Third Age",
       "Glorfindel is an Elf-lord of Rivendell, mighty among Elrond's household. He finds Frodo wounded after Weathertop and helps bear him toward the Ford. His words at the Ford—that the Witch-king will not fall by the hand of man—are fulfilled on the Pelennor.",
       "Character (Elf; Noldo)",
       "A lord of Gondolin in the First Age (wider legendarium); in the Third Age a resident of Imladris.",
       "Elrond; Frodo; Aragorn; the Bruinen; the Witch-king (prophecy).",
       "To aid the Ring-bearer's flight from the Nazgûl in Eriador.",
       [
           "- **The Road.** He passes Frodo's hidden company and warns of pursuit.",
           "- **The Ford.** He leads the wounded Hobbit toward Rivendell; the river rises against the Riders.",
           "- **The prophecy.** His statement about the Witch-king shapes how readers understand Éowyn and Merry's deed.",
       ],
       [
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Bearer he escorts toward safety."),
           ("Rivendell", f"{L}/rivendell/", "His home in the Third Age."),
           ("Weathertop", f"{L}/weathertop/", "Where the wound he helps heal was given."),
           ("The Witch-king of Angmar", f"{C}/witch-king/", "Subject of his prophecy."),
       ],
       "Glorfindel does not appear in the southern war in the book. Films often fold his Ford role into Arwen; the chronicle notes the book's separate assignment.")

    md("characters", "cirdan", "Círdan",
       "Elven shipwright of the Grey Havens, keeper of Narya until he gave it to Gandalf, among the oldest still in Middle-earth.",
       ["elf", "sindar"], "The Shipwright; Lord of Mithlond", "First Age to Fourth Age",
       "Círdan the Shipwright rules the Grey Havens at Mithlond, building the ships that take Elves into the West. He surrendered Narya, the Ring of Fire, to Gandalf when the Istari arrived. At the end of the Third Age he remains when most great Elves have gone.",
       "Character (Elf; Sinda; lord)",
       "Ancient lord of the Falas and later of Lindon and Mithlond; beard is noted as unusual among Elves.",
       "The Grey Havens; Gandalf; Narya; Frodo and Bilbo's final ship.",
       "To build the way West and to counsel the Istari at their coming.",
       [
           "- **The Havens.** His folk maintain the port for Elven departure.",
           "- **Narya.** He gives Gandalf the Ring of Fire, trusting the Grey Pilgrim.",
           "- **The last ship.** Frodo and Bilbo sail from his havens; the keepers of the Three depart.",
       ],
       [
           ("The Grey Havens", f"{L}/grey-havens/", "His harbour."),
           ("Gandalf", f"{C}/gandalf/", "Recipient of Narya."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Ring-bearer granted passage from his shore."),
           ("Elrond", f"{C}/elrond/", "Fellow lord who sails from Mithlond."),
       ],
       "Círdan is marginal in dialogue but central in the legendarium's ending. He is said to remain in Middle-earth into the Fourth Age in the appendices.")

    md("characters", "radagast", "Radagast the Brown",
       "Istar who dwells at Rhosgobel, friend to beasts and birds, who lent his steeds to Gandalf and warned of the Nazgûl in the North.",
       ["maia", "wizard"], "Radagast; the Brown", "Third Age",
       "Radagast is one of the Five Wizards, called the Brown for his love of wild things. He lives at Rhosgobel between Mirkwood and the Anduin. Gandalf sends him as messenger to Orthanc in a trap; Saruman uses the errand. He sends eagles and news that aid the hunt for the Ring.",
       "Character (Maia / Istar)",
       "Came with the Istari about T.A. 1000; settled in Rhovanion.",
       "Beasts and birds; Gandalf; Saruman (unwilling go-between); the eagles.",
       "To tend the living world; his messages and beasts indirectly serve the wider war.",
       [
           "- **Rhosgobel.** A house among trees where he knows every nest and burrow.",
           "- **The errand.** Gandalf's note to Saruman passes through him and leads to Gandalf's imprisonment.",
           "- **The eagles.** Beasts carry word; Gwaihir later bears Gandalf from Orthanc.",
       ],
       [
           ("Gandalf", f"{C}/gandalf/", "Fellow Istar who trusts his beasts."),
           ("Saruman", f"{C}/saruman/", "Who exploits his simplicity."),
           ("Gwaihir", f"{C}/gwaihir/", "Eagle who aids Gandalf."),
           ("The Istari", f"{P}/istari/", "Order to which he belongs."),
       ],
       "Radagast is not a comic footnote in the book: he is the reason Gandalf reaches Isengard. His failure is distraction from the war of counsels, not cowardice.")

    md("characters", "tom-bombadil", "Tom Bombadil",
       "Ageless master of the Old Forest who rescues the Hobbits from the Barrow-wight and is untouched by the Ring's power.",
       ["enigma"], "Iarwain Ben-adar; Forn; Orald", "Unknown age",
       "Tom Bombadil is a singular figure east of the Shire who sings the world around him into order. He saves the Hobbits from Old Man Willow and from a Barrow-wight. When Frodo puts the Ring on in his house, Tom sees him without vanishing. The Council considers sending the Ring to him and rejects it—he would forget it or lose it.",
       "Character (unknown kind)",
       "Claims to remember the first raindrop and the first acorn; predates the Hobbits' lands.",
       "Goldberry; the Old Forest; the Barrow-downs; the four Hobbits (early journey).",
       "To be master of his country; not to be a guardian of the Ring.",
       [
           "- **The Forest.** He sings Willow to release Merry and Pippin.",
           "- **The Barrow.** He rouses Frodo to break the wight's spell.",
           "- **The Ring.** He handles it without effect; the Quest cannot rely on him.",
       ],
       [
           ("Goldberry", f"{C}/goldberry/", "River-daughter; his companion."),
           ("Old Forest", f"{L}/old-forest/", "Land he rules by song."),
           ("Barrow-downs", f"{L}/barrow-downs/", "Where he saves the Hobbits from wights."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Who wears the Ring in his house without Tom's corruption."),
       ],
       "Tom remains deliberately unexplained. The book rules him out as Ring-keeper because his care is local and his memory is not the memory of guardians.")

    md("characters", "goldberry", "Goldberry",
       "River-daughter who dwells with Tom Bombadil and welcomes the Hobbits to the one night of rest before the Barrow-downs.",
       ["enigma"], "Daughter of the River", "Unknown age",
       "Goldberry is the wife of Tom Bombadil, called River-woman's daughter. She welcomes Frodo's company to their house with water-lilies in her hair. Her presence is calm, seasonal, and without fear of the Ring. She represents the Withywindle's gentler face beside Tom's wild mastery.",
       "Character (unknown kind)",
       "Associated with the River Withywindle and Tom's house at the edge of the Old Forest.",
       "Tom Bombadil; the Hobbits as guests; the Withywindle.",
       "To keep Tom's house and to offer hospitality without entering the War.",
       [
           "- **The welcome.** 'The water lilies have come to you'—a meal and a night's safety.",
           "- **The morning.** She sends them on toward the downs where danger waits.",
       ],
       [
           ("Tom Bombadil", f"{C}/tom-bombadil/", "Companion and lord of the household."),
           ("Old Forest", f"{L}/old-forest/", "Country near their home."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Guest before the Barrow trial."),
       ],
       "Goldberry appears only in this episode. She is not a combatant or counsellor in the War; her role is restorative interlude.")

    md("characters", "haldir", "Haldir",
       "Galadhrim march-warden of Lórien who blindfolds the Fellowship at the Naith and later leads archers to Helm's Deep in the film only.",
       ["elf"], "March-warden of Lórien", "Third Age",
       "Haldir is an Elf of Lothlórien who meets the Fellowship at the borders and enforces the law of the Golden Wood: strangers enter blindfolded. He guides them toward Caras Galadhon. In the book he does not march to Helm's Deep; that is a film addition.",
       "Character (Elf; Galadhrim)",
       "Serves the lords of Lórien as border-warden in the Third Age.",
       "Galadriel; Celeborn; the Fellowship as guided guests.",
       "To guard the Wood's secrecy and to conduct lawful guests to the lords.",
       [
           "- **The Naith.** He requires even Legolas and Aragorn to be blindfolded for parity with Gimli.",
           "- **The march.** In the book his role ends in Lórien; film sends him to die at Helm's Deep.",
       ],
       [
           ("Lothlórien", f"{L}/lothlorien/", "Wood he guards."),
           ("Galadriel", f"{C}/galadriel/", "Lady of the realm he serves."),
           ("The Fellowship of the Ring", f"{E}/fellowship-of-the-ring/", "Company he escorts inward."),
       ],
       "Haldir is a small but memorable voice for Lórien's closed policy. Readers should not import film-only deaths into book canon.")

    md("characters", "beregond", "Beregond",
       "Guard of the Citadel of Minas Tirith who befriends Pippin and slays the troll-chief at the Black Gate.",
       ["human", "gondor"], "Guard of the Citadel", "Third Age",
       "Beregond is a Man of Gondor, soldier of the Citadel who swears service beside Peregrin Took. He loves Faramir and nearly dies defending him from Denethor's pyre. After the War he is assigned to guard Faramir in Ithilien and is remembered for killing a troll at the Morannon.",
       "Character (Man of Gondor; soldier)",
       "Born in Minas Tirith; captain in the Guard of the Citadel.",
       "Pippin; Faramir; Denethor; Beregond's son Bergil; the Houses of Healing.",
       "To serve the Steward's house and to save Faramir when law and despair collide.",
       [
           "- **The Citadel.** He instructs Pippin in Gondor's customs and watches the sky with him.",
           "- **The pyre.** He fights the porters of Rath Dínen to reach Faramir; Gandalf intervenes.",
           "- **The Gate.** He marches to the last battle and survives.",
       ],
       [
           ("Peregrin Took", f"{C}/peregrin-took/", "Brother-in-arms of the Guard."),
           ("Faramir", f"{C}/faramir/", "Captain he saves from burning."),
           ("Denethor II", f"{C}/denethor/", "Lord whose command he defies."),
           ("Minas Tirith", f"{L}/minas-tirith/", "City of his service."),
       ],
       "Beregond's breach of the Citadel's law is punished by service in Ithilien—a mercy that keeps honour and life together.")

    md("characters", "imrahil", "Prince Imrahil",
       "Prince of Dol Amroth who leads the sortie from Minas Tirith and recognizes Aragorn as king by ancient kinship.",
       ["human", "gondor"], "Prince of Dol Amroth", "Third Age",
       "Imrahil is a Man of Gondor, lord of Dol Amroth with Númenórean blood and swan-ships. He commands the city's sortie when the gate breaks and meets Aragorn in the field. He bears Faramir and Éowyn to the Houses of Healing and yields the city to the returning king.",
       "Character (Man of Gondor; prince)",
       "Ruler of Dol Amroth, fief on the Bay of Belfalas; kinsman of Elendil's line in distant degree.",
       "Faramir; Éowyn; Aragorn; Minas Tirith; the Pelennor.",
       "To defend the city and to recognize the true king when he comes from the Paths of the Dead.",
       [
           "- **The sortie.** His knights charge when the Witch-king enters the broken gate.",
           "- **The healers.** He helps carry the wounded to the Houses of Healing.",
           "- **The King.** He hails Aragorn with the ancient name and supports his claim.",
       ],
       [
           ("Dol Amroth", f"{L}/dol-amroth/", "His princedom."),
           ("Minas Tirith", f"{L}/minas-tirith/", "City he defends."),
           ("Aragorn", f"{C}/aragorn/", "King he acknowledges."),
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Field of his charge."),
       ],
       "Imrahil is the book's image of Gondor's nobility still intact beneath the Steward's pride. His swan-knights are not a film invention though films shorten his role.")

    md("characters", "mouth-of-sauron", "The Mouth of Sauron",
       "Lieutenant of Barad-dûr who parleys at the Morannon and displays Sam's gear to taunt the Captains before Aragorn strikes him down.",
       ["human", "mordor"], "Lieutenant of the Tower", "Third Age",
       "The Mouth of Sauron is a Man, probably of Númenórean descent, who has served Sauron so long that he has forgotten his own name. He rides out under the parley flag at the Black Gate with tokens taken from Frodo's gear. Gandalf rejects his terms; Aragorn beheads him in wrath.",
       "Character (Man; servant of Sauron)",
       "Long corrupted in Sauron's service; speaks with the Dark Lord's voice at times.",
       "Sauron; the Morannon; Frodo's mithril-coat and gear as props.",
       "To bargain in bad faith and to break the Captains' hope before the last battle.",
       [
           "- **The parley.** He claims the Ring-bearer is captive and offers surrender terms.",
           "- **The tokens.** Sam's gear and the mithril-coat suggest Frodo is taken.",
           "- **The stroke.** Aragorn kills him; the Captains march knowing the Quest may still live.",
       ],
       [
           ("Sauron", f"{C}/sauron/", "Master whose terms he speaks."),
           ("Black Gate", f"{L}/black-gate/", "Place of the parley."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Bearer whose fate he misrepresents."),
           ("Aragorn", f"{C}/aragorn/", "Who refuses the lie and strikes him."),
       ],
       "The Mouth is brief on stage but structurally vital: he nearly breaks hope at the Morannon. The book does not show Sauron speaking; this voice stands in.")

    md("characters", "rosie-cotton", "Rosie Cotton",
       "Hobbit of Bywater whom Sam loves and marries after the War, anchor of the life he returns to build.",
       ["hobbit"], "Rose Cotton; Sam's Rosie", "Third Age",
       "Rosie Cotton is a Hobbit of the Shire, daughter of Farmer Cotton, whom Samwise Gamgee loves long before the Quest. Her presence in Sam's mind—especially near Cirith Ungol—helps him resist despair. After the War they marry, raise a family at Bagshot Row, and Sam becomes Mayor.",
       "Character (Hobbit)",
       "Born in Bywater; known to Sam from youth; sister to Tom, Jolly, Nick, and Nibs Cotton.",
       "Samwise Gamgee; the Cotton family; the Shire after the Scouring.",
       "To represent home and ordinary happiness Sam fights to restore.",
       [
           "- **Before the Road.** Sam thinks of her garden and her smile when the Quest is darkest.",
           "- **Return.** She helps heal the Shire; she and Sam wed when the year turns.",
           "- **After.** Many children; Sam's mayoral years; she survives into his later life.",
       ],
       [
           ("Samwise Gamgee", f"{C}/samwise-gamgee/", "Husband and Ring-bearer's companion."),
           ("Bywater", f"{L}/bywater/", "Village of her family."),
           ("The Shire", f"{L}/the-shire/", "Land they rebuild together."),
       ],
       "Rosie is not a warrior but she is a motive. The book's ending ties victory to marriage, gardens, and children—not only to thrones.")

    md("characters", "barliman-butterbur", "Barliman Butterbur",
       "Innkeeper of the Prancing Pony at Bree who forgets Gandalf's letter and aids the Hobbits after the Ringwraith attack.",
       ["hobbit", "man"], "Master of the Prancing Pony", "Third Age",
       "Barliman Butterbur is the Man who keeps the Prancing Pony in Bree. He forgets to send Gandalf's warning letter to Frodo—a failure that nearly costs everything. After the Nazgûl attack he helps with ponies and news and later receives the returned Bill the Pony.",
       "Character (Man of Bree)",
       "Long keeper of the chief inn on the East Road; honest but absent-minded.",
       "Gandalf's letter; Frodo's company; Nob the hob and Bob the ostler; Bree-land.",
       "To host travellers and, belatedly, to speed the Ring-bearer on the Road.",
       [
           "- **The letter.** Gandalf's note warning Frodo to leave at once—never delivered in time.",
           "- **The attack.** Strider hides the Hobbits; Butterbur helps with beds and ponies afterward.",
           "- **Bill.** The pony bought here returns after the Quest.",
       ],
       [
           ("Bree", f"{L}/bree/", "Town of his inn."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Traveller he failed to warn in time."),
           ("Aragorn", f"{C}/aragorn/", "Strider who takes charge at the Pony."),
       ],
       "Butterbur's forgetfulness is comic and consequential. Tolkien lets him be good-hearted without being competent—a mirror of the Shire's unpreparedness.")

    md("characters", "quickbeam", "Quickbeam",
       "Ent of Fangorn who decides quickly at the Entmoot and marches with unusual haste against Isengard.",
       ["ent"], "Bregalad; the hastiest Ent", "Third Age",
       "Quickbeam (Bregalad) is an Ent who has already lost rowan trees to Saruman's axes. At the Entmoot he does not need long deliberation. He marches with Treebeard's host and names Orcs on the battlefield. His haste contrasts Entish slowness and shows the forest's anger.",
       "Character (Ent)",
       "Resident of Fangorn; younger in Ent terms than Treebeard.",
       "Treebeard; Merry and Pippin; Isengard as enemy; rowans he mourned.",
       "To decide for war when the Entmoot might still be talking.",
       [
           "- **The Moot.** He is already resolved when others debate.",
           "- **Isengard.** He fights in the flood and the breaking of the ring.",
       ],
       [
           ("Treebeard", f"{C}/treebeard/", "Eldest Ent who leads the march."),
           ("Fangorn Forest", f"{L}/fangorn/", "His home."),
           ("Isengard", f"{L}/isengard/", "Target of his wrath."),
           ("Ents", f"{P}/ents/", "His dwindling people."),
       ],
       "Quickbeam gives the Ents a face besides Treebeard. His name is a joke the Hobbits understand at once.")

    md("characters", "gwaihir", "Gwaihir",
       "Windlord of the Great Eagles who bears Gandalf from Orthanc and later rescues Frodo and Sam from Orodruin.",
       ["eagle"], "Gwaihir the Windlord", "Third Age",
       "Gwaihir is the lord of the Eagles who answers Gandalf's call at Isengard and carries him from Saruman's roof. At the end he bears Frodo and Sam from the ruin of Mount Doom. He serves Manwë's purposes, not the Free Peoples' plans, and comes when need and command align.",
       "Character (Eagle; emissary)",
       "Chief of the Eagles of the North in the War of the Ring.",
       "Gandalf; Radagast's messages; Frodo and Sam; Manwë (ultimately).",
       "To aid at crises where eagles are the only rescue.",
       [
           "- **Orthanc.** He finds Gandalf on the tower and carries him to Edoras.",
           "- **The Morannon.** He watches the march; he does not carry the armies.",
           "- **Orodruin.** He lifts the Ring-bearers from the fire's edge when all seems lost.",
       ],
       [
           ("Gandalf", f"{C}/gandalf/", "Who calls him more than once."),
           ("Radagast", f"{C}/radagast/", "Whose beast-messages reach eagle-kind."),
           ("Mount Doom", f"{L}/mount-doom/", "Place of the last rescue."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Bearer he bears away."),
       ],
       "Eagles are not a taxi service the heroes can summon at will. Each appearance is dramatic because it is rare and costly in the world's logic.")

    md("characters", "brand-king-of-dale", "Brand",
       "King of Dale who defends Erebor against Sauron's northern army and falls on the field before Dale is retaken.",
       ["human", "dale"], "King of Dale", "Third Age",
       "Brand is the King of Dale in the War of the Ring, grandson of Bard the Bowman. When Sauron's forces assault Erebor and Dale, Brand and Dáin Ironfoot fight together. Both fall; his son Bard II and Dáin's heir hold the Mountain until news of the Ring's destruction breaks the enemy.",
       "Character (Man of Dale; King)",
       "Ruler of Dale beneath Erebor in the late Third Age; ally of the Dwarves.",
       "Dáin Ironfoot; Bard II; Erebor; the Battle of Dale (appendices).",
       "To hold the North when Sauron strikes Erebor while the South fights on the Pelennor.",
       [
           "- **The assault.** Easterlings and northern Orcs besiege Dale and the Mountain.",
           "- **The fall.** Brand and Dáin die defending the gates.",
           "- **Victory.** His son survives; the North is freed when the Ring is unmade.",
       ],
       [
           ("Dáin Ironfoot", f"{C}/dain-ironfoot/", "Ally who falls beside him."),
           ("Erebor", f"{L}/erebor/", "Kingdom he defends with Dale."),
           ("Bard the Bowman", f"{C}/bard-the-bowman/", "Ancestor who slew Smaug."),
           ("The Battle of Dale", f"{E}/battle-of-dale/", "Northern front of the same War."),
       ],
       "Brand's war is appendix-canon but proves the Ring's fall saves more than Gondor. Without it, the North could have fallen unseen.")

    md("characters", "gil-galad", "Gil-galad",
       "Last High King of the Noldor in Middle-earth who led the Last Alliance with Elendil and fell on the slopes of Orodruin.",
       ["elf", "noldor", "king"], "High King of the Noldor", "First Age to Second Age",
       "Gil-galad is an Elf-king of Lindon, last of the High Kings of the Noldor in Middle-earth. With Elendil he forms the Last Alliance of Elves and Men against Sauron. He falls in the siege of Barad-dûr; Elrond was his herald. His spear Aeglos is remembered on the field.",
       "Character (Elf; Noldo; King)",
       "Ruler of Lindon in the Second Age; ally of Númenor and later of Elendil's exiles.",
       "Elendil; Elrond; the Last Alliance; Sauron; Aeglos.",
       "To overthrow Sauron when he claims the One Ring openly.",
       [
           "- **Alliance.** Elves of Lindon and Men of the West march east.",
           "- **Siege.** Barad-dûr is invested for years.",
           "- **Fall.** He dies with Elendil when Sauron comes out; Isildur takes the Ring.",
       ],
       [
           ("Elendil", f"{C}/elendil/", "Ally who falls beside him."),
           ("Elrond", f"{C}/elrond/", "Herald who survives."),
           ("The Last Alliance", f"{E}/last-alliance/", "War he leads."),
           ("Isildur", f"{C}/isildur/", "Who cuts the Ring from Sauron after."),
       ],
       "Gil-galad is past before the Third Age begins, but every account of the Ring's first taking passes through his war.")

    md("characters", "anarion", "Anárion",
       "Younger son of Elendil who co-founded Gondor and whose line continued through the Stewards until Aragorn's return.",
       ["man", "dunadan", "king"], "King of Gondor; co-founder", "Second Age",
       "Anárion is the younger son of Elendil, twin in authority with Isildur in Gondor though not in Arnor. He built Minas Anor with his father and ruled the South-kingdom from Osgiliath. He died in the siege of Barad-dûr; his line ruled Gondor until the Stewards' age and the king's return.",
       "Character (Man; Dúnadan; King)",
       "Son of Elendil; lord of Minas Anor; co-ruler of Gondor with Isildur's line in the South.",
       "Elendil; Isildur; Gondor; Minas Tirith (Minas Anor); Stewards (later).",
       "To hold the South-kingdom while the High King ruled from Arnor.",
       [
           "- **Founding.** He raises the Tower of Ecthelion and the White Tree in the South.",
           "- **Siege.** He dies before Sauron's fall; his son Meneldil receives the South.",
           "- **Line.** Kings of Gondor descend from him until Eärnur; then Stewards rule in their name.",
       ],
       [
           ("Elendil", f"{C}/elendil/", "Father and High King."),
           ("Isildur", f"{C}/isildur/", "Brother who ruled Arnor and shared Gondor."),
           ("Gondor", f"{L}/gondor/", "Kingdom he founded."),
           ("Denethor II", f"{C}/denethor/", "Late Steward of his house's realm."),
           ("Aragorn", f"{C}/aragorn/", "Who reunites the lines of Elendil."),
       ],
       "Anárion's line is the Gondorian half of Elendil's legacy. Aragorn inherits both Isildur's North and Anárion's South by right and marriage.")

    md("characters", "deagol", "Déagol",
       "Stoor Hobbit of the Gladden Fields who found the One Ring in the river and was murdered by Sméagol his cousin.",
       ["stoor", "hobbit"], "Finder of the Ring in the river", "Third Age",
       "Déagol is a Stoor Hobbit who fishes the Gladden Fields with his cousin Sméagol. In T.A. 2463 he finds a golden ring in the water. Sméagol demands it as a birthday present, strangles him, and hides the murder. The Ring passes to Gollum and so begins the long road to Bilbo and Frodo.",
       "Character (Stoor Hobbit)",
       "Lived among the Stoors near the Gladden; cousin and friend of Sméagol.",
       "Sméagol/Gollum; the One Ring; the river Anduin.",
       "To be the Ring's first finder after Isildur's loss—unwittingly.",
       [
           "- **The find.** A fish pulls him under; his hand closes on gold.",
           "- **The murder.** Sméagol kills him on his birthday and takes the Precious.",
           "- **After.** His body is hidden; the Stoors do not know how the Ring entered their kind.",
       ],
       [
           ("Gollum", f"{C}/gollum/", "Cousin who murdered him for the Ring."),
           ("The One Ring", f"{P}/one-ring/", "Object of the killing."),
           ("The Anduin", f"{L}/anduin/", "River where it lay after Isildur."),
       ],
       "Déagol appears only in Gandalf's reconstruction of the Ring's history. His death is the first crime the Ring inspires in the Third Age.")

    md("characters", "smaug", "Smaug",
       "Last great fire-drake of the North who seized Erebor's treasure and was slain by Bard beneath Lonely Mountain.",
       ["dragon"], "Smaug the Golden; the Worm", "Third Age",
       "Smaug is a Dragon who drove Durin's Folk from Erebor in T.A. 2770 and lay on their hoard until Thorin's Quest. Bilbo stole a cup and riddled with him; later Bard of Esgaroth shot him with a black arrow learned from old lore. His fall freed the treasure and drew the Battle of Five Armies.",
       "Character (Dragon)",
       "Came south from the Withered Heath; occupied Erebor nearly two centuries.",
       "Erebor; Lake-town; Thorin's company; the Arkenstone; Bilbo.",
       "To hoard gold and rule the Mountain from sleep and terror.",
       [
           "- **The taking.** He ruined Dale and the Mountain in fire.",
           "- **The burglar.** Bilbo's theft wakes his wrath and reveals a bare patch on his chest.",
           "- **The fall.** Bard's arrow finds the gap; Smaug dies on the town he meant to destroy.",
       ],
       [
           ("Erebor", f"{L}/erebor/", "Hoard he occupied."),
           ("Bard the Bowman", f"{C}/bard-the-bowman/", "Who slew him."),
           ("Bilbo Baggins", f"{C}/bilbo-baggins/", "Burglar who first stole from him."),
           ("Thorin Oakenshield", f"{C}/thorin-oakenshield/", "King who came to reclaim the hoard."),
           ("The Slaying of Smaug", f"{E}/slaying-of-smaug/", "His death."),
       ],
       "Smaug is the bridge between *The Hobbit* and the Ring's later history: the hoard Thorin reclaims is where Bilbo finds the Ring's context of greed.")

    md("characters", "beorn", "Beorn",
       "Skin-changer of the Vales of Anduin who hosted Thorin's company and fought at the Battle of Five Armies in bear form.",
       ["beorning", "skin-changer"], "Beorn; the Skin-changer", "Third Age",
       "Beorn is a Man of the Anduin vales who can take the shape of a great bear. He distrusts strangers but hosts Gandalf's party and marches to Ravenhill in bear-form at the Battle of Five Armies. His people, the Beornings, later guard the High Pass and the Ford of Carrock.",
       "Character (Man; skin-changer)",
       "Lived alone between Mirkwood and the Mountains; friend to animals; enemy of Orcs.",
       "Gandalf; Bilbo; Thorin's company; the Carrock; later the High Pass road.",
       "To protect his lands and to repay Gandalf's trust with aid against the Orc host.",
       [
           "- **The hall.** He feeds the company and warns of Mirkwood.",
           "- **The battle.** He comes in bear-shape when the fight turns against the Free Peoples.",
           "- **After.** His line keeps the passes open in the late Third Age (appendices).",
       ],
       [
           ("Mirkwood", f"{L}/mirkwood/", "Forest he borders."),
           ("Thorin Oakenshield", f"{C}/thorin-oakenshield/", "Guest he grudgingly helped."),
           ("The Battle of Five Armies", f"{E}/battle-of-five-armies/", "Where he turned the tide."),
       ],
       "Beorn does not appear in the War of the Ring, but his people's keeping of the passes matters to northern travel lore.")

    md("characters", "bard-the-bowman", "Bard the Bowman",
       "Descendant of Girion of Dale who shot Smaug with a black arrow and became King of restored Dale.",
       ["human", "dale"], "Bard; the Bowman", "Third Age",
       "Bard is a bowman of Esgaroth, of the line of Girion, who understands Smaug's weak spot from thrush-speech and old tales. His arrow kills the Dragon. He leads Lake-town's survivors, receives a fourteenth share of treasure, and rebuilds Dale. Brand and Bard II descend from him.",
       "Character (Man of Dale)",
       "Guard and archer of Lake-town; heir of Girion's lordship in memory.",
       "Smaug; Thorin; Bilbo; Girion's legacy; Brand (grandson).",
       "To slay the Dragon and restore Dale beneath Erebor.",
       [
           "- **The thrush.** A bird brings word of the bare patch on Smaug's chest.",
           "- **The shot.** The black arrow flies when the Dragon attacks the town.",
           "- **The kingdom.** He does not take Erebor; he rebuilds Dale and trades with the Dwarves.",
       ],
       [
           ("Smaug", f"{C}/smaug/", "Dragon he slew."),
           ("Brand", f"{C}/brand-king-of-dale/", "Grandson who rules in the War of the Ring."),
           ("Erebor", f"{L}/erebor/", "Mountain freed by his deed."),
           ("The Slaying of Smaug", f"{E}/slaying-of-smaug/", "Moment of his fame."),
       ],
       "Bard is the Man who ends the Dragon-era of the North. His line still holds Dale when Sauron strikes Erebor again.")

    md("characters", "farmer-maggot", "Farmer Maggot",
       "Wealthy Hobbit farmer of the Marish who knows Tom Bombadil and drives Frodo to Bucklebury Ferry with his dogs.",
       ["hobbit"], "Farmer of the Marish", "Third Age",
       "Farmer Maggot is a Hobbit of the Shire's Marish, a farmer who owns dogs feared by local Hobbits and knows Tom Bombadil. He has no love of Black Riders and speedily ferries Frodo, Sam, and Pippin toward Buckland when the Nazgûl hunt begins.",
       "Character (Hobbit)",
       "Lives at Maggot's Farm in the Eastfarthing; grows mushrooms; knows the Old Forest's border.",
       "Frodo; Sam; Pippin; Tom Bombadil; the Black Riders on the Road.",
       "To aid the travellers without joining the Quest.",
       [
           "- **The farm.** Frodo steals mushrooms in youth; Maggot later gives them freely.",
           "- **The Riders.** He describes a Black Rider at his gate and helps the Hobbits escape by boat.",
       ],
       [
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Traveller he ferries toward Buckland."),
           ("Buckland", f"{L}/buckland/", "Destination of the night ride."),
           ("Tom Bombadil", f"{C}/tom-bombadil/", "Friend he knows from the border country."),
       ],
       "Maggot is early proof that the Shire's ordinary folk can be brave without knowing the whole tale.")

    md("characters", "lobelia-sackville-baggins", "Lobelia Sackville-Baggins",
       "Reluctant hero of the Scouring who swung her umbrella at ruffians and was imprisoned for defying Sharkey's men.",
       ["hobbit"], "Mrs. Lobelia; the Sackville-Baggins", "Third Age",
       "Lobelia Sackville-Baggins is a Hobbit of the Shire, wife of Otho, long coveter of Bag End. During the Scouring she defies Saruman's ruffians and is imprisoned. After the victory she returns Bag End's keys to Frodo and is honoured when she dies.",
       "Character (Hobbit)",
       "Of the Sackville-Baggins family; Bilbo's cousin; sharp-tongued and proud.",
       "Bag End; Frodo; the Scouring; Sharkey's regime.",
       "To be a comic rival turned unlikely resistor of tyranny.",
       [
           "- **Before.** She wanted Bag End; Bilbo and Frodo kept it.",
           "- **The Scouring.** She fights ruffians with an umbrella; she is jailed.",
           "- **After.** She gives back keys; the Shire remembers her courage.",
       ],
       [
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Cousin and heir of Bag End."),
           ("The Scouring of the Shire", f"{E}/scouring-of-the-shire/", "When she resisted."),
           ("The Shire", f"{L}/the-shire/", "Her home."),
       ],
       "Lobelia is Tolkien's joke that even the petty can grow large when home is threatened.")

    md("characters", "bill-ferny", "Bill Ferny",
       "Bree ruffian who sold ponies to the Hobbits and later served as Saruman's spy and ruffian in the Shire.",
       ["human", "traitor"], "Bill Ferny of Bree", "Third Age",
       "Bill Ferny is a Man of Bree, a sneering fellow in league with the Nazgûl's hunt and later with Saruman's Shire occupation. He sells a poor pony to the Hobbits at inflated price. In the Scouring he appears among the ruffians until the Hobbits win.",
       "Character (Man of Bree; ruffian)",
       "Known in Bree as a bad character; associates with outsiders.",
       "The Nazgûl; Saruman's men; Butterbur's inn as scene of suspicion.",
       "To profit from trouble and to serve whoever pays in the Shire's ruin.",
       [
           "- **Bree.** He lurks at the Pony; a Nazgûl uses his voice at the gate.",
           "- **The pony.** Bill the Pony is bought from him and later returns.",
           "- **Scouring.** He is among the defeated occupiers.",
       ],
       [
           ("Bree", f"{L}/bree/", "His town."),
           ("Barliman Butterbur", f"{C}/barliman-butterbur/", "Innkeeper who distrusts him."),
           ("The Scouring of the Shire", f"{E}/scouring-of-the-shire/", "End of his petty tyranny."),
       ],
       "Bill Ferny links the Road's early danger to the Shire's late occupation—the same small evil in two acts.")

    md("characters", "azog", "Azog",
       "Orc-chief of Moria who slew Thrór and was killed by Dáin at Azanulbizar, beginning the long feud of Thrór's line.",
       ["orc"], "Azog the Defiler", "Third Age",
       "Azog is an Orc of Moria who killed King Thrór at the East-gate of Khazad-dûm, mutilating his body. The War of the Dwarves and Orcs followed. He was slain by young Dáin Ironfoot in the Battle of Azanulbizar. His son Bolg leads Orcs at the Battle of Five Armies.",
       "Character (Orc; chieftain)",
       "Ruled Moria's Orcs in the late Third Age before Balin's colony.",
       "Thrór; Thráin; Thorin; Dáin; Bolg (son); the Azanulbizar battlefield.",
       "To defile Durin's heir and to break Dwarf pride at Moria's gate.",
       [
           "- **Thrór's death.** He kills the king at the gate and brands his head.",
           "- **The war.** Dwarves hunt Orcs for years across the mountains.",
           "- **Azanulbizar.** Dáin kills Azog; the gate is too costly to reclaim.",
       ],
       [
           ("Dáin Ironfoot", f"{C}/dain-ironfoot/", "Who slew him as a youth."),
           ("Thorin Oakenshield", f"{C}/thorin-oakenshield/", "Heir of the line he insulted."),
           ("Moria", f"{L}/moria/", "His domain."),
           ("The Battle of Azanulbizar", f"{E}/battle-of-azanulbizar/", "Where he fell."),
       ],
       "Azog is backstory for Thorin and Dáin, but the book keeps his name alive in Dwarf memory at every mention of Moria.")


def write_extra_locations(md, C, L, E, P):
    md("locations", "bree", "Bree",
       "Crossroads town where Hobbits and Big Folk dwell together, and the Prancing Pony stands on the East Road.",
       ["eriador", "settlement"], "Bree-land; the crossroads", "Third Age",
       "Bree is a town of Men and Hobbits at the junction of the Greenway and the East Road. The Prancing Pony is its chief inn. Frodo's company is hunted here by Nazgûl; Strider joins them. It is the last inhabited stop before the wilds toward Weathertop and the Shire's borders.",
       "Town / crossroads",
       "Ancient settlement; Bree-land has long mixed Hobbits and Men.",
       "Barliman Butterbur; Strider; Bill Ferny; Hobbits of the Shire and Bree.",
       "To host travel between Eriador's regions; narratively the threshold of danger.",
       [
           "- **The Pony.** Rooms, ale, and the lost letter.",
           "- **The attack.** Nazgûl stab at doors; Strider leads the Hobbits out by the gate.",
       ],
       [
           ("Barliman Butterbur", f"{C}/barliman-butterbur/", "Innkeeper."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Ring-bearer who passes through."),
           ("Aragorn", f"{C}/aragorn/", "Strider who takes up guard here."),
       ],
       "Bree is neither Shire nor wilderness—a liminal place where the epic touches ordinary life.")

    md("locations", "bag-end", "Bag End",
       "Smial of the Bagginses under Hobbiton Hill, starting point of Bilbo's and Frodo's journeys and object of Lobelia's envy.",
       ["shire", "homeland"], "Bag End Under-Hill", "Third Age",
       "Bag End is a Hobbit-hole at the end of Bagshot Row in Hobbiton, home of the Baggins family. Bilbo returns from Erebor to its comforts; Frodo inherits it and the Ring. After the War Sam restores it; later he lives there as Mayor's family until Frodo's departure.",
       "Homestead (Hobbit-hole)",
       "Built by Bungo Baggins; long the chief smial of the family.",
       "Bilbo; Frodo; Sam; Lobelia Sackville-Baggins; the Party Tree nearby.",
       "To be the image of home the Quest leaves and returns to.",
       [
           "- **The Party.** Bilbo's farewell feast and disappearance.",
           "- **Departure.** Frodo sells it to the Sackville-Bagginses and leaves secretly.",
           "- **Return and gift.** Frodo gives it to Sam; the Scouring heals the hill.",
       ],
       [
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Master who bore the Ring from here."),
           ("Bilbo Baggins", f"{C}/bilbo-baggins/", "Former master and finder of the Ring."),
           ("The Shire", f"{L}/the-shire/", "Country it stands in."),
       ],
       "Bag End is the emotional pole opposite Mount Doom: the same story measured from hole to volcano.")

    md("locations", "buckland", "Buckland",
       "Hobbit country east of the Brandywine, home of the Brandybucks and the Old Forest's wary neighbours.",
       ["shire", "homeland"], "The Buckland; the East-march", "Third Age",
       "Buckland lies between the Brandywine and the Old Forest, settled by the Oldbucks (later Brandybucks). Brandy Hall at Bucklebury is its centre. Merry is of this country; the High Hay fences the Forest. Frodo's first night out of the Shire proper is at Crickhollow.",
       "Region (Hobbit march)",
       "Settled T.A. 740 by Gorhendad Oldbuck; later the Brandybuck chieftains.",
       "Merry; Brandy Hall; the Ferry; Old Forest border.",
       "To guard the Shire's eastern flank and to house a bolder Hobbit strain.",
       [
           "- **Crickhollow.** Frodo's supposed new home; the conspiracy unmasked.",
           "- **The Ferry.** Escape from a Black Rider on the Road.",
       ],
       [
           ("Meriadoc Brandybuck", f"{C}/meriadoc-brandybuck/", "Master of Buckland after the War."),
           ("Old Forest", f"{L}/old-forest/", "Wood beyond the Hay."),
           ("The Shire", f"{L}/the-shire/", "Realm it marches with."),
       ],
       "Buckland Hobbits are slightly less insular than the Shire average—a fit birthplace for Merry's later courage.")

    md("locations", "old-forest", "Old Forest",
       "Ancient wood east of Buckland where Old Man Willow and the Withywindle test the Hobbits before Tom Bombadil's rescue.",
       ["forest", "eriador"], "The Old Forest", "Third Age",
       "The Old Forest is a remnant of Eriador's ancient woods, hostile to trespassers. Old Man Willow sleeps at its heart; the Withywindle runs through it. The Hobbits take a shortcut and are trapped until Tom Bombadil sings them free.",
       "Ancient forest",
       "Predates the Shire; once part of a vast woodland; the High Hay keeps it from Buckland.",
       "Tom Bombadil; Goldberry; Old Man Willow; the four Hobbits (early).",
       "To be a living barrier and a reminder that Eriador was once all trees.",
       [
           "- **The path.** The Hobbits lose the path and circle toward the River.",
           "- **The Willow.** Merry and Pippin are trapped until Tom arrives.",
       ],
       [
           ("Tom Bombadil", f"{C}/tom-bombadil/", "Master who walks here unharmed."),
           ("Buckland", f"{L}/buckland/", "Neighbour separated by the Hay."),
           ("Barrow-downs", f"{L}/barrow-downs/", "Hills beyond its eastern edge."),
       ],
       "The Forest is not evil in Sauron's sense—it is old and resentful. That distinction matters in Tolkien's ecology.")

    md("locations", "barrow-downs", "Barrow-downs",
       "Hill country of ancient barrows east of the Old Forest where a wight captures Merry and Pippin until Tom Bombadil intervenes.",
       ["eriador", "ruin"], "Tyrn Gorthad", "Third Age",
       "The Barrow-downs are rolling hills crowned with stone rings and barrows of the Edain of old. Fog and wights linger there. Frodo's company camps incautiously; a Barrow-wight traps Merry and Pippin. Tom Bombadil rouses Frodo to break the spell with a sword from the mound.",
       "Burial hills / haunted land",
       "Tombs of the Men of the First Age who fought Morgoth in the North.",
       "Barrow-wights; Tom Bombadil; Frodo; Merry; Pippin; blades from the mound (later Westernesse knives).",
       "To hold memory of forgotten wars and to arm the Hobbits with blades that wound the Nazgûl.",
       [
           "- **The fog.** The downs disorient travellers.",
           "- **The barrow.** Frodo calls Tom; Merry and Pippin are saved; daggers are taken.",
       ],
       [
           ("Tom Bombadil", f"{C}/tom-bombadil/", "Who rescues the Hobbits."),
           ("Old Forest", f"{L}/old-forest/", "Wood to the west."),
           ("Weathertop", f"{L}/weathertop/", "Next camp where the blades are used."),
       ],
       "The daggers from the barrow wound the Witch-king's flesh—a gift of the dead to the living Quest.")

    md("locations", "dunharrow", "Dunharrow",
       "Cliff refuge behind the Dwimorberg where Rohan musters before the Paths of the Dead, haunted by legend and silence.",
       ["rohan", "refuge"], "The Hold of Dunharrow", "Third Age",
       "Dunharrow is a natural fortress of cliffs and tiers behind the White Mountains, reached by a zigzag path. Théoden gathers the muster of Rohan here. Below lies the Dark Door to the Paths of the Dead. Aragorn takes the forbidden road while the Rohirrim ride toward Minas Tirith.",
       "Refuge / muster-point",
       "Ancient refuge of the Rohirrim; associated with the Dead beneath the mountains.",
       "Théoden; Éowyn (left as regent); Aragorn; the Dwimorberg.",
       "To gather the Ride in secret and to hide the king's road until the hour.",
       [
           "- **The muster.** Riders assemble in the tiers.",
           "- **The Door.** Aragorn, Legolas, and Gimli enter the Paths; Éowyn begs to follow.",
       ],
       [
           ("Rohan", f"{L}/rohan/", "Realm it serves."),
           ("The Paths of the Dead", f"{E}/paths-of-the-dead/", "Road taken from its threshold."),
           ("Théoden", f"{C}/theoden/", "King who musters here."),
       ],
       "Dunharrow is fear made geography—the living ride out by daylight while the heir of Isildur walks under the mountain.")

    md("locations", "minas-morgul", "Minas Morgul",
       "Tower-city of the Ringwraiths in the pass of Imlad Morgul, once Minas Ithil, shining twin of Minas Anor before the Ring's capture.",
       ["gondor", "mordor"], "Tower of the Moon; the Dead City", "Second Age to Third Age",
       "Minas Morgul is the city Isildur built as Minas Ithil, later taken when the Ringwraiths returned. It glows with a sickly light. Frodo and Sam see it from the cross-roads; the Witch-king leads his host out to war against Minas Tirith.",
       "Fortress-city (corrupted)",
       "Built by Isildur; fallen to the Nazgûl in the Third Age.",
       "The Witch-king; Frodo and Sam; Gollum; the pass into Mordor.",
       "To guard the eastern pass and to be the launching place of the Morgul-host.",
       [
           "- **The cross-roads.** Statues and turning toward the Morgul Vale.",
           "- **The march.** The Witch-king's army pours toward Osgiliath and the Pelennor.",
       ],
       [
           ("Isildur", f"{C}/isildur/", "Who built it as Minas Ithil."),
           ("The Witch-king of Angmar", f"{C}/witch-king/", "Lord of the city."),
           ("Cirith Ungol", f"{L}/cirith-ungol/", "Pass nearby into Mordor."),
           ("Minas Tirith", f"{L}/minas-tirith/", "Twin city still held by Gondor."),
       ],
       "Minas Morgul is the anti-Minas Tirith—same origin, opposite master. The book uses it to show Gondor's long defeat in the East.")

    md("locations", "osgiliath", "Osgiliath",
       "Once capital of Gondor on the Anduin, now a ruined crossing fought over before the siege of Minas Tirith.",
       ["gondor", "ruin"], "Citadel of the Stars", "Second Age to Third Age",
       "Osgiliath was the chief city of Gondor, spanning the Anduin. The palantír of the chief stone was lost here. Sauron's forces take the eastern half; Faramir fights a fighting retreat. The Morgul-host crosses on its way to the Pelennor.",
       "Ruined city / crossing",
       "Founded by Isildur and Anárion; capital until the kin-strife and plagues.",
       "Faramir; Boromir; the Anduin; Minas Tirith upstream.",
       "To be the contested ford between East and West in the War's Gondor chapter.",
       [
           "- **Faramir's defence.** Rangers hold the western ruins until overwhelmed.",
           "- **The crossing.** The Witch-king's army passes toward the city of the Kings.",
       ],
       [
           ("Faramir", f"{C}/faramir/", "Captain who retreats from its banks."),
           ("Minas Tirith", f"{L}/minas-tirith/", "City upstream that depends on its defence."),
           ("The Anduin", f"{L}/anduin/", "River it bridges."),
       ],
       "Osgiliath's fall in the book is the drumbeat before the siege—not a spectacle city but a wound in Gondor's body.")

    md("locations", "dol-amroth", "Dol Amroth",
       "Princedom on the Bay of Belfalas ruled by Imrahil, whose swan-knights ride to Minas Tirith's relief.",
       ["gondor", "fief"], "The Prince's fief", "Third Age",
       "Dol Amroth is a fief of Gondor on the southern coast, ruled by the Princes of the House of Dol Amroth with Númenórean blood. Imrahil leads its knights to the Pelennor. The swan-ships and swan-knights are its sigils.",
       "Coastal princedom",
       "Ancient fief of Gondor; claims Elvish kinship in legend.",
       "Imrahil; Faramir (kin); the Bay of Belfalas.",
       "To hold the southern coast and to answer the city's need in war.",
       [
           "- **The sortie's ally.** Imrahil's cavalry joins the field when the gate breaks.",
           "- **After.** Faramir and Éowyn dwell in Ithilien under the Prince's kindred's shadow.",
       ],
       [
           ("Imrahil", f"{C}/imrahil/", "Prince in the War of the Ring."),
           ("Minas Tirith", f"{L}/minas-tirith/", "City he relieves."),
           ("Gondor", f"{L}/gondor/", "Realm of which he is lord."),
       ],
       "Dol Amroth is Gondor's reminder that not all strength lives in the White City.")

    md("locations", "pelargir", "Pelargir",
       "Chief haven of Gondor on the Anduin where Aragorn captures the Corsair fleet and turns the ships toward Minas Tirith.",
       ["gondor", "haven"], "The Royal Havens", "Second Age to Third Age",
       "Pelargir is the great harbour of Gondor on the Anduin near the Sea. Corsairs of Umbar hold it until Aragorn and the Dead drive them out. The captured black ships become the terror that breaks the Corsair force at the Pelennor—Dúnedain at the prow instead of Southrons.",
       "Haven / city",
       "Founded by the Faithful of Númenor in the Second Age.",
       "Aragorn; the Dead; Umbar's Corsairs; the fleet that saves Minas Tirith.",
       "To be the southern naval strength of Gondor and the prize of the Paths of the Dead.",
       [
           "- **The Dead's release.** Oath fulfilled at the ships.",
           "- **The turn.** Sails raised for Minas Tirith with the grey Company aboard.",
       ],
       [
           ("Aragorn", f"{C}/aragorn/", "Who takes the fleet."),
           ("The Paths of the Dead", f"{E}/paths-of-the-dead/", "Road that ends here."),
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Battle the ships decide."),
       ],
       "Pelargir is the hinge between Aragorn's ghost-road and his kingly arrival—without it, the black sails stay evil.")

    md("locations", "black-gate", "The Black Gate",
       "Morannon of Mordor, iron gate of Sauron's land where the Captains feint a last battle to draw his eye from Orodruin.",
       ["mordor", "fortress"], "The Morannon", "Second Age to Third Age",
       "The Black Gate is the main entrance to Mordor from the northwest, a wall of iron and stone with the reeking land of Gorgoroth beyond. Aragorn leads the Host of the West here to challenge Sauron. The Mouth parleys; battle follows; Frodo and Sam are on the Mountain while armies clash at the gate.",
       "Fortified gate",
       "Built by Sauron in the Second Age; rebuilt when he returns.",
       "Sauron; the Mouth of Sauron; Aragorn; Gandalf; the Host of the West.",
       "To be the only frontal way into Mordor and the stage of the last diversion.",
       [
           "- **The parley.** Tokens of Frodo shown; hope nearly breaks.",
           "- **The battle.** Armies fight while the Ring-bearer reaches the Sammath Naur.",
       ],
       [
           ("Mordor", f"{L}/mordor/", "Land it guards."),
           ("The Mouth of Sauron", f"{C}/mouth-of-sauron/", "Who rides out under truce."),
           ("Mount Doom", f"{L}/mount-doom/", "Goal hidden behind the feint."),
           ("The Battle of the Black Gate", f"{E}/battle-of-black-gate/", "Final field battle."),
       ],
       "The Morannon battle is strategically a distraction—heroic, costly, and necessary only because Sauron must believe the Ring is a weapon used against him.")

    md("locations", "dead-marshes", "Dead Marshes",
       "Stagnant meres below the Emyn Muil where faces of the dead lie under water and Gollum leads Frodo and Sam by secret paths.",
       ["wilderness", "mordor-border"], "The marshes of the Dead", "Third Age",
       "The Dead Marshes lie in the wastes between the Emyn Muil and the plain before Mordor. Lights and faces float beneath the pools—memories of a long-ago battle. Gollum knows stepping-stones; Frodo is nearly lured into the water. The area is a moral and physical bog on the approach to the Black Land.",
       "Marsh / haunted ground",
       "Site of an ancient battle absorbed by fen and time.",
       "Gollum; Frodo; Sam; Sauron's searching Eye (later).",
       "To be an obstacle only a traitor-guide can navigate.",
       [
           "- **The path.** Hopping stones by night and fog.",
           "- **The faces.** Frodo sees dead warriors under the water and nearly falls in.",
       ],
       [
           ("Gollum", f"{C}/gollum/", "Guide who knows the safe line."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Bearer nearly taken by the pools."),
           ("Emyn Muil", f"{L}/emyn-muil/", "Broken hills to the north."),
       ],
       "The marshes are Middle-earth's refuse heap of forgotten wars—a warning that every battle leaves ghosts.")

    md("locations", "emyn-muil", "Emyn Muil",
       "Broken hills of sharp rock between the Dead Marshes and the Anduin where Frodo and Sam wander lost until Gollum finds them.",
       ["wilderness"], "The Emyn Muil", "Third Age",
       "The Emyn Muil are a maze of grey hills and cliffs east of the Anduin bend. Frodo and Sam wander here after leaving the Emyn Muil's eastern edge from the Fellowship's break. Gollum finds them and bargains to lead them. The terrain forces dependence on the creature they distrust.",
       "Badlands / hill country",
       "Natural maze on Mordor's northwest approach.",
       "Frodo; Sam; Gollum; the Ring's weight.",
       "To isolate the Ring-bearer and to begin the Gollum-road to Cirith Ungol.",
       [
           "- **Lost days.** Food runs low; the hills repeat.",
           "- **The catch.** Gollum is captured and sworn on the Ring.",
       ],
       [
           ("Gollum", f"{C}/gollum/", "Guide bound here."),
           ("Dead Marshes", f"{L}/dead-marshes/", "Country to the south."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Bearer crossing toward Mordor."),
       ],
       "The Emyn Muil is the Quest at its smallest—two Hobbits, one wretch, and rock without names.")

    md("locations", "caradhras", "Caradhras",
       "Redhorn peak of the Misty Mountains where snow and fell voice drive the Fellowship back toward Moria.",
       ["misty-mountains"], "Redhorn; Caradhras", "Third Age",
       "Caradhras is the mountain the Fellowship tries to cross from Hollin. Snow and wind mount; Boromir's suggestion to use the Ring is shouted down; Gandalf fears a will in the storm. They turn back to the Dimrill Gate and Moria—a choice that costs Gandalf.",
       "Mountain pass",
       "One of the great peaks of the Misty Mountains above Khazad-dûm.",
       "The Fellowship; Legolas and Gimli's argument about the mountain's name; the storm.",
       "To bar the high road and force the lower road into darkness.",
       [
           "- **The climb.** Pack-ponies lost; snow buries the path.",
           "- **The turn.** Moria chosen instead; the Balrog waits.",
       ],
       [
           ("Moria", f"{L}/moria/", "Alternative road taken after failure here."),
           ("The Fellowship of the Ring", f"{E}/fellowship-of-the-ring/", "Company turned back."),
           ("Gandalf", f"{C}/gandalf/", "Who reads malice in the storm."),
       ],
       "Caradhras is the book's first major fork: over the mountain or through the mines. The mountain answers for them.")

    md("locations", "amon-hen", "Amon Hen",
       "Hill of Sight on the Anduin's western bank where Frodo sits in the high seat and chooses the Quest alone.",
       ["wilderness"], "Hill of Sight", "Third Age",
       "Amon Hen is a hill crowned with an ancient seat of seeing on the western shore of Nen Hithoel. Frodo climbs it after the debate at Parth Galen, puts on the Ring, and sees far—then chooses to go to Mordor alone. The Breaking of the Fellowship follows on the lawn below.",
       "Hill / seat of vision",
       "Ancient Gondorian or older work on the Anduin bend.",
       "Frodo; the Ring; Boromir (who follows); Aragorn and the hunters later.",
       "To be the place of Frodo's decisive choice and the Ring's pull toward sight.",
       [
           "- **The seat.** Visions of war spread below when the Ring is worn.",
           "- **The flight.** Frodo leaves; Boromir's temptation peaks; Orcs attack.",
       ],
       [
           ("Parth Galen", f"{L}/parth-galen/", "Lawn at the hill's foot."),
           ("The Breaking of the Fellowship", f"{E}/breaking-of-the-fellowship/", "Event begun here."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Bearer who chooses alone."),
       ],
       "Amon Hen pairs with Amon Lhaw across the water—Sight and Hearing—both old tools the War outruns.")

    md("locations", "parth-galen", "Parth Galen",
       "Green lawn at the feet of Amon Hen where the Fellowship camps and breaks when Boromir falls and Orcs strike.",
       ["wilderness"], "The Green Sward", "Third Age",
       "Parth Galen is the grassy sward below Amon Hen on the west bank of Nen Hithoel. The Fellowship lands here after leaving Lórien. Debate, temptation, death, and capture happen in one afternoon—the narrative hinge of the whole War.",
       "River lawn",
       "Natural clearing on the Anduin bend above Rauros.",
       "The Fellowship; Boromir; Uruk-hai of Isengard.",
       "To be the campsite where the company ends as a single story.",
       [
           "- **Camp.** Boats hidden; paths chosen or argued.",
           "- **Breaking.** Boromir dies; Merry and Pippin taken; Frodo and Sam gone east.",
       ],
       [
           ("Amon Hen", f"{L}/amon-hen/", "Hill above the lawn."),
           ("The Breaking of the Fellowship", f"{E}/breaking-of-the-fellowship/", "What happens here."),
           ("Boromir", f"{C}/boromir/", "Who falls defending the younger Hobbits."),
       ],
       "Parth Galen is the last green place before the Quest splits into threads the book will follow separately.")

    md("locations", "dol-guldur", "Dol Guldur",
       "Hill of dark sorcery in southern Mirkwood where the Necromancer dwelt before openly returning to Mordor.",
       ["mirkwood", "fortress"], "Hill of Dark Sorcery", "Third Age",
       "Dol Guldur is a fortress on a hill in southern Mirkwood, seat of the Necromancer—Sauron in hiding—until the White Council drives him out. He returns to Mordor openly; the Nazgûl retake it in the War. Galadriel throws it down after his final fall.",
       "Dark fortress",
       "Built in the Second Age; occupied by Sauron as Necromancer in the Third.",
       "Sauron; the White Council; Thranduil's realm (nearby); Khamûl (later).",
       "To be Sauron's hidden base while the Ring sleeps; later an eastern threat in the War.",
       [
           "- **The Necromancer.** Gandalf investigates; the Council strikes.",
           "- **Return.** Sauron openly in Mordor; Dol Guldur still poisons Mirkwood.",
           "- **Fall.** Galadriel cleanses it after the Ring is destroyed.",
       ],
       [
           ("Mirkwood", f"{L}/mirkwood/", "Forest it darkens."),
           ("Sauron", f"{C}/sauron/", "Who dwelt here in disguise."),
           ("Thranduil", f"{C}/thranduil/", "King whose realm it threatens."),
       ],
       "Dol Guldur explains why Mirkwood is black and why Legolas's people live in fear long before Mordor opens.")

    md("locations", "bywater", "Bywater",
       "Village of the Shire where the Battle of Bywater ends Sharkey's occupation and the four Travellers return as heroes.",
       ["shire", "settlement"], "Bywater on the Water", "Third Age",
       "Bywater is a village in the Shire near Hobbiton, with an inn and the Cottons' farm. Sam's Rosie lives here. The Scouring culminates in the Battle of Bywater on the fields outside—Hobbits defeat ruffians; Saruman's grip breaks.",
       "Village",
       "Ordinary Shire settlement on the Water.",
       "Rosie Cotton; Farmer Cotton; the four Travellers; Sharkey's ruffians.",
       "To be the field where the War is won at home.",
       [
           "- **Return.** The four come back to a fenced, ruled Shire.",
           "- **Battle.** Bywater is the decisive fight of the Scouring.",
       ],
       [
           ("Rosie Cotton", f"{C}/rosie-cotton/", "Sam's beloved of this village."),
           ("The Scouring of the Shire", f"{E}/scouring-of-the-shire/", "Its local battle."),
           ("The Shire", f"{L}/the-shire/", "Realm it belongs to."),
       ],
       "Bywater proves the epic's last battle is small in scale but full in meaning.")

    md("locations", "iron-hills", "Iron Hills",
       "Dwarven country east of Erebor whence Dáin Ironfoot brought reinforcements to the Battle of Five Armies and later ruled before Erebor.",
       ["dwarf-home"], "The Iron Hills", "Third Age",
       "The Iron Hills are a range east of Erebor inhabited by Dwarves of Durin's Folk, notably Dáin's branch. Dáin leads from here to Thorin's aid at the Five Armies. Later he rules Erebor until he falls in the War of the Ring; the Hills remain part of the northern Dwarf-realms.",
       "Dwarf region",
       "Long settled by Durin's Folk; rich in iron as the name says.",
       "Dáin Ironfoot; Thorin; Erebor as ally-neighbour.",
       "To supply kings and armies when Erebor is threatened.",
       [
           "- **Five Armies.** Dáin's host turns the battle.",
           "- **Later.** Dáin moves to Erebor; the Hills remain his people's land.",
       ],
       [
           ("Dáin Ironfoot", f"{C}/dain-ironfoot/", "Lord who came from here."),
           ("Erebor", f"{L}/erebor/", "Mountain kingdom allied nearby."),
           ("Thorin Oakenshield", f"{C}/thorin-oakenshield/", "Kinsman he rescued."),
       ],
       "The Iron Hills are appendix-geography that makes Dáin's arrival at Erebor credible and timely.")

    md("locations", "houses-of-healing", "Houses of Healing",
       "Wards of Minas Tirith where Aragorn heals Faramir, Éowyn, and Merry after the Pelennor using kingsfoil and old lore.",
       ["gondor", "sanctuary"], "The Houses of Healing", "Third Age",
       "The Houses of Healing are the hospital wards of Minas Tirith, where the wounded of the Pelennor are brought. Aragorn enters as a healer, not yet crowned, and saves those struck by the Black Breath. The herb kingsfoil (athelas) is his sign.",
       "Hospital / sanctuary",
       "Ancient institution of Gondor in the sixth circle of the City.",
       "Aragorn; Faramir; Éowyn; Merry; Ioreth the talkative wisewoman.",
       "To mend the critically wounded when medicine alone fails.",
       [
           "- **The Black Breath.** Wounds from the Witch-king and his weapons.",
           "- **The hands of the king.** Aragorn's healing proves his right as much as his sword.",
       ],
       [
           ("Minas Tirith", f"{L}/minas-tirith/", "City that contains them."),
           ("Aragorn", f"{C}/aragorn/", "Healer-king."),
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Source of the wounded."),
       ],
       "Healing here is political theology: the king's touch is part of his office in Gondor's lore.")

    md("locations", "tower-of-cirith-ungol", "Tower of Cirith Ungol",
       "Orc-tower guarding the pass where Frodo is stripped of the Ring and Sam rescues him before the march to Orodruin.",
       ["mordor", "fortress"], "Tower of the Pass", "Third Age",
       "The Tower of Cirith Ungol is an Orc-stronghold at the top of the pass above Shelob's lair. Frodo is taken here alive after the spider's sting. Sam infiltrates, takes the Ring briefly, and rescues Frodo—a reversal that keeps the Quest alive at its lowest point.",
       "Orc tower",
       "Built by Gondor long ago; held by Orcs in Sauron's service.",
       "Shagrat and Gorbag's companies; Frodo; Sam; the mithril-coat as prize.",
       "To guard the pass and to search any intruder taken in the web.",
       [
           "- **Capture.** Orcs quarrel over Frodo's gear; the mithril-coat goes to Barad-dûr.",
           "- **Rescue.** Sam fights with Sting and the Phial; Frodo is carried out.",
       ],
       [
           ("Cirith Ungol", f"{L}/cirith-ungol/", "Pass it commands."),
           ("Shelob", f"{C}/shelob/", "Spider below who stings Frodo."),
           ("Samwise Gamgee", f"{C}/samwise-gamgee/", "Who enters alone."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Prisoner within."),
       ],
       "The tower is Sam's hour—the gardener as hero when no king is present.")


def write_extra_events(md, C, L, E, P):
    md("events", "battle-of-five-armies", "The Battle of Five Armies",
       "Clash beneath Erebor among Dwarves, Elves, Men, and Orcs after Smaug's fall, ending Thorin's line and crowning Dáin.",
       ["battle", "erebor"], "At the foot of Erebor, T.A. 2941", "Third Age 2941",
       "The Battle of Five Armies is fought on and below the Lonely Mountain after Smaug's death. Dwarves of Erebor and Iron Hills, Elves of Mirkwood, Men of Lake-town, and Orcs of the North collide. Thorin dies; Dáin becomes King under the Mountain. Bilbo watches from Ravenhill, invisible.",
       "Event (battle)",
       "Triggered by Smaug's fall and disputed treasure; Bolg leads Orcs from Gundabad.",
       "Thorin; Dáin; Bard; Thranduil; Beorn; Bilbo.",
       "To decide who holds Erebor's treasure and kingdom after the Dragon.",
       [
           "- **The muster.** Elves and Men besiege the Dwarves in the Mountain.",
           "- **The Orcs.** Bolg's host arrives; enemies ally against the common threat.",
           "- **The turn.** Beorn and eagles help; Thorin falls; peace and Dáin's kingship follow.",
       ],
       [
           ("Thorin Oakenshield", f"{C}/thorin-oakenshield/", "Who dies on Ravenhill."),
           ("Dáin Ironfoot", f"{C}/dain-ironfoot/", "Victor and new king."),
           ("Smaug", f"{C}/smaug/", "Whose death invited the armies."),
           ("Erebor", f"{L}/erebor/", "Mountain contested."),
       ],
       "This battle closes *The Hobbit* and sets the North's politics for the later War.")

    md("events", "siege-of-minas-tirith", "The Siege of Minas Tirith",
       "Assault on the White City by the Morgul-host: broken gate, Witch-king's fall, and relief by Rohan and the Captains' ships.",
       ["battle", "gondor"], "Minas Tirith, 13–15 March T.A. 3019", "Third Age March 3019",
       "The Siege of Minas Tirith is the central battle of the War in the South. Grond breaks the gate; the Witch-king enters; Théoden falls; Éowyn and Merry slay the Lord of the Nazgûl; Aragorn arrives on captured ships. The city stands but barely.",
       "Event (siege / battle)",
       "Follows Osgiliath's fall and Faramir's retreat; ends with the Pelennor victory.",
       "Denethor; Faramir; Gandalf; Théoden; Éowyn; Aragorn; the Witch-king.",
       "To break Gondor's heart before Sauron moves to crush all resistance.",
       [
           "- **The flame.** Signal fires call Rohan.",
           "- **The gate.** Grond and the Witch-king; Gandalf alone in the breach.",
           "- **The Ride and the ships.** Rohan charges; Aragorn's fleet turns the tide.",
       ],
       [
           ("The Battle of the Pelennor Fields", f"{E}/pelennor-fields/", "Field outside the walls."),
           ("Minas Tirith", f"{L}/minas-tirith/", "City besieged."),
           ("The Witch-king of Angmar", f"{C}/witch-king/", "Who breaks the gate and falls."),
       ],
       "The siege is the book's longest sustained battle sequence—hope measured in circles of the City.")

    md("events", "battle-of-black-gate", "The Battle of the Black Gate",
       "Last battle of the War where the Host of the West challenges Sauron at the Morannon while Frodo and Sam reach Orodruin.",
       ["battle", "mordor"], "Morannon, 25 March T.A. 3019", "Third Age 25 March 3019",
       "The Battle of the Black Gate is Aragorn and Gandalf's feint—a small army marching to certain seeming doom so the Ring-bearer can walk unseen to Mount Doom. The Mouth parleys; battle joins; the Ring is destroyed even as the armies fight; the gate collapses in Sauron's undoing.",
       "Event (battle / diversion)",
       "Planned after the Pelennor to draw Sauron's Eye outward.",
       "Aragorn; Gandalf; Pippin; Beregond; the Mouth of Sauron; Frodo and Sam (parallel).",
       "To keep Sauron watching the army, not the Mountain.",
       [
           "- **The march.** Seven thousand walk to the Morannon.",
           "- **The parley.** Frodo's mithril-coat shown; hope tested.",
           "- **The end.** Mount Doom erupts; Sauron's power breaks; armies saved.",
       ],
       [
           ("Black Gate", f"{L}/black-gate/", "Place of the battle."),
           ("The Destruction of the One Ring", f"{E}/destruction-of-the-ring/", "Simultaneous unmaking."),
           ("Aragorn", f"{C}/aragorn/", "Captain of the feint."),
       ],
       "This battle is won not on the field but in the fire—a lesson the Captains gamble everything on.")

    md("events", "entmoot-and-fall-of-isengard", "The Entmoot and the Fall of Isengard",
       "Ents debate war at Fangorn and flood Isengard, breaking Saruman's ring while Orthanc stands unbroken.",
       ["battle", "ents"], "Fangorn and Isengard, T.A. 3019", "Third Age February–March 3019",
       "The Entmoot is the gathering where Ents decide to march against Saruman—hurried by Quickbeam and stirred by Merry and Pippin's news. They break the ring of Isengard, flood the pits, and trap Saruman in Orthanc. Treebeard keeps him under guard until Gandalf casts him out.",
       "Event (war / flood)",
       "Follows Merry and Pippin's meeting with Treebeard.",
       "Treebeard; Quickbeam; Merry; Pippin; Saruman; Gríma.",
       "To answer industrial felling with the fury of the forest.",
       [
           "- **The Moot.** Long debate; decision for war.",
           "- **The flood.** Water from the mountains drowns Isengard's forges.",
           "- **Orthanc.** The tower survives; Saruman is caged in it.",
       ],
       [
           ("Isengard", f"{L}/isengard/", "Fortress unmade."),
           ("Treebeard", f"{C}/treebeard/", "Leader of the march."),
           ("Saruman", f"{C}/saruman/", "Prisoner in his tower."),
       ],
       "Isengard's fall is the War's strangest victory—no human king, only trees and water.")

    md("events", "battle-of-bywater", "The Battle of Bywater",
       "Final fight of the Scouring where Hobbits defeat Saruman's ruffians on the fields near Bywater.",
       ["battle", "shire"], "Bywater, November T.A. 3019", "Third Age November 3019",
       "The Battle of Bywater is the armed climax of the Scouring of the Shire. Merry and Pippin lead organized Hobbits against ruffians; Sharkey's regime collapses. Saruman is captured and later killed at Bag End. The Shire is free but scarred.",
       "Event (battle)",
       "Follows the four Travellers' return and rallying of the Shire.",
       "Merry; Pippin; Frodo; Sam; Saruman; Lobelia's resistance (earlier).",
       "To throw out the petty tyranny installed while heroes were away.",
       [
           "- **Muster.** Horn-call and barricades on the Road.",
           "- **Charge.** Hobbits rout ruffians with courage and surprise.",
           "- **After.** Saruman's end; trees replanted; Sharkey gone.",
       ],
       [
           ("The Scouring of the Shire", f"{E}/scouring-of-the-shire/", "Larger event it concludes."),
           ("Bywater", f"{L}/bywater/", "Village beside the field."),
           ("Saruman", f"{C}/saruman/", "Overthrown here and at Bag End."),
       ],
       "Bywater is small war with full stakes—the book refuses an ending that forgets home.")

    md("events", "weathertop-ambush", "The Ambush at Weathertop",
       "Attack of the Nazgûl on Amon Sûl where Frodo is wounded by the Witch-king's Morgul-knife.",
       ["quest", "eriador"], "Weathertop, 6 October T.A. 3018", "Third Age October 3018",
       "The Ambush at Weathertop is the Ringwraiths' assault on Strider's camp below the ruin of Amon Sûl. Frodo puts on the Ring; the Witch-king stabs him with a Morgul-blade. A fragment remains; he would become a wraith without Elrond's healing.",
       "Event (attack)",
       "Follows pursuit from Bree and flight across the Road.",
       "Frodo; Aragorn; the five Nazgûl present; Glorfindel (later at the Ford).",
       "To take the Ring or the Ring-bearer; partial success in wounding.",
       [
           "- **The fire.** Strider's circle of flames holds briefly.",
           "- **The stab.** Frodo sees the Witch-king in the Unseen world.",
           "- **Flight.** Glorfindel and Aragorn race toward Rivendell.",
       ],
       [
           ("Weathertop", f"{L}/weathertop/", "Hill of the attack."),
           ("Frodo Baggins", f"{C}/frodo-baggins/", "Wounded bearer."),
           ("The Witch-king of Angmar", f"{C}/witch-king/", "Who stabs him."),
           ("Rivendell", f"{L}/rivendell/", "Where healing waits."),
       ],
       "Weathertop is the moment the Quest stops being a journey and becomes a race against wraithcraft.")

    md("events", "flight-to-the-ford", "The Flight to the Ford",
       "Pursuit of Frodo by Nazgûl to the Bruinen where the river rises at Elrond's command and washes the Riders away.",
       ["quest", "eriador"], "Road to the Ford of Bruinen, October 3018", "Third Age October 3018",
       "The Flight to the Ford is the last stage of the Ringwraith hunt in Eriador. Glorfindel finds Frodo; white horse carries him; Nazgûl chase to the Ford. At the boundary of Rivendell the water rises in horse-shapes and destroys the Riders' mounts.",
       "Event (pursuit)",
       "Immediately follows Weathertop wound and hurried march.",
       "Frodo; Glorfindel; Aragorn; Elrond (off-stage); the Nine.",
       "To bring the bearer to safety or into Sauron's hands—failed at the water.",
       [
           "- **The ride.** Frodo fades from the Morgul shard as they run.",
           "- **The Ford.** Last Riders cross; river answers Elrond.",
       ],
       [
           ("Glorfindel", f"{C}/glorfindel/", "Escort from the Road."),
           ("Rivendell", f"{L}/rivendell/", "Refuge beyond the Ford."),
           ("Weathertop Ambush", f"{E}/weathertop-ambush/", "Wound that forces haste."),
       ],
       "The Ford is Rivendell's moat—a boundary where Elven power still rules in Eriador.")

    md("events", "battle-of-azanulbizar", "The Battle of Azanulbizar",
       "Final battle of the War of Dwarves and Orcs at Moria's East-gate where Dáin slew Azog but the Dwarves did not reclaim Khazad-dûm.",
       ["battle", "dwarves"], "Dimrill Dale, T.A. 2799", "Third Age 2799",
       "Azanulbizar is the bloody battle in the Dimrill Dale before Moria's gates. Thráin and Thorin fight; Náin falls; young Dáin kills Azog. The Dwarves win the day but losses forbid entering Moria; they turn to Erebor and the Iron Hills instead.",
       "Event (battle)",
       "Climax of the long war after Azog killed Thrór.",
       "Thorin; Dáin; Azog; Balin; Glóin among the veterans.",
       "To avenge Thrór and break Orc power at Moria—partial victory.",
       [
           "- **The charge.** Dwarves assault the East-gate.",
           "- **Azog's fall.** Dáin kills him at age thirty-two.",
           "- **The cost.** Too many dead to hold the mines; pyres in the dale.",
       ],
       [
           ("Azog", f"{C}/azog/", "Orc-king slain."),
           ("Dáin Ironfoot", f"{C}/dain-ironfoot/", "Hero of the day."),
           ("Moria", f"{L}/moria/", "Gate they would not re-enter."),
           ("Thorin Oakenshield", f"{C}/thorin-oakenshield/", "Warrior who earned fame here."),
       ],
       "Azanulbizar explains why Moria is Orc-held when Balin tries again—and why Dáin is respected.")

    md("events", "slaying-of-smaug", "The Slaying of Smaug",
       "Death of the Dragon of Erebor by Bard's arrow, ending two centuries of ruin and drawing armies to the Mountain.",
       ["battle", "erebor"], "Esgaroth and Erebor, T.A. 2941", "Third Age 2941",
       "The Slaying of Smaug is the shot of Bard the Bowman from Lake-town as the Dragon attacks the town in wrath. A thrush shows the bare patch on Smaug's chest; the black arrow flies true. Smaug falls on the town's ruins; treasure and trouble both lie open.",
       "Event (single deed / turning point)",
       "Follows Bilbo's theft of a cup and conversation with Smaug.",
       "Bard; Smaug; Bilbo; Thorin (heir waiting); Lake-town.",
       "To kill the Dragon and free Erebor's hoard—success with heavy cost to the town.",
       [
           "- **The attack.** Smaug flies against Esgaroth.",
           "- **The word.** Thrush and old lore tell Bard where to aim.",
           "- **The fall.** Dragon dies; gold waits; armies gather.",
       ],
       [
           ("Smaug", f"{C}/smaug/", "Dragon slain."),
           ("Bard the Bowman", f"{C}/bard-the-bowman/", "Archer who fired."),
           ("The Battle of Five Armies", f"{E}/battle-of-five-armies/", "What followed."),
           ("Erebor", f"{L}/erebor/", "Mountain opened by his death."),
       ],
       "Smaug's death is the hinge between dragon-era North and the politics of Dwarves, Men, and Elves.")

    md("events", "drowning-of-numenor", "The Downfall of Númenor",
       "Akallabêth: Ar-Pharazôn's armada against Valinor and the drowning of Númenor, after which Elendil's Faithful flee to Middle-earth.",
       ["catastrophe", "numenor"], "Númenor and the Great Sea, S.A. 3319", "Second Age 3319",
       "The Downfall of Númenor is the destruction of the Isle of Kings when Ar-Pharazôn sails against the Undying Lands. Ilúvatar reshapes the world; Númenor sinks. Elendil and the Faithful escape with the palantíri and seeds of the White Tree. Sauron's fair form is lost.",
       "Event (catastrophe)",
       "End of the Second Age's Númenórean empire; Sauron's bodily ruin.",
       "Elendil; Isildur; Anárion; Ar-Pharazôn; Sauron (captive then spirit).",
       "To close the age of Númenórean pride and begin the Realms in Exile.",
       [
           "- **Corruption.** Sauron in Númenor turns the king toward the West.",
           "- **The armada.** Ships sail to forbidden Valinor.",
           "- **The wave.** The isle is drowned; Faithful ships flee east.",
       ],
       [
           ("Elendil", f"{C}/elendil/", "Leader of the survivors."),
           ("Elros", f"{C}/elros/", "Ancestor of the drowned kings' line through Andúnië."),
           ("Gondor", f"{L}/gondor/", "Realm founded after."),
           ("The Last Alliance", f"{E}/last-alliance/", "War the exiles soon fight."),
       ],
       "The Downfall is backstory to all Dúnedain drama—why Gondor exists and why kingship is exile's memory.")

    md("events", "shelob-and-cirith-ungol", "Shelob and the Tower of Cirith Ungol",
       "Gollum's betrayal in the pass, Frodo's sting and capture, and Sam's rescue—the Quest's lowest corridor before Orodruin.",
       ["quest", "mordor"], "Cirith Ungol, 13–14 March T.A. 3019", "Third Age March 3019",
       "This sequence covers Gollum's lead through Shelob's tunnel, the spider's attack, Frodo's capture by Orcs, and Sam's infiltration of the Tower of Cirith Ungol. Sam bears the Ring briefly and returns it. The mithril-coat is taken to Barad-dûr, misleading Sauron.",
       "Event (crisis)",
       "On the stairs and tunnels above Minas Morgul.",
       "Frodo; Sam; Gollum; Shelob; Shagrat's Orcs.",
       "To pass the secret way—or fail and be stripped of the Ring.",
       [
           "- **The tunnel.** Darkness and Gollum's last kindness feigned.",
           "- **Shelob.** Frodo falls; Sam fights with Phial and Sting.",
           "- **The tower.** Sam rescues Frodo; they dress as Orcs and go on.",
       ],
       [
           ("Shelob", f"{C}/shelob/", "Spider of the pass."),
           ("Tower of Cirith Ungol", f"{L}/tower-of-cirith-ungol/", "Prison."),
           ("Gollum", f"{C}/gollum/", "Traitor-guide."),
           ("Mount Doom", f"{L}/mount-doom/", "Goal still ahead."),
       ],
       "Here the Quest nearly ends twice—spider and tower—and Sam carries both Ring and master.")

    md("events", "battle-of-dale", "The Battle of Dale",
       "Northern front of the War where Brand and Dáin fell defending Erebor until Sauron's fall broke the besiegers.",
       ["battle", "dale"], "Dale and Erebor, March 3019", "Third Age March 3019",
       "The Battle of Dale is fought simultaneously with the southern War. Sauron's Easterlings assault Dale and Erebor. Brand and Dáin Ironfoot die at the gates. Bard II and Thorin III hold the Mountain until news of the Ring's destruction scatters the enemy.",
       "Event (battle)",
       "Appendix account of the North during the War of the Ring.",
       "Brand; Dáin; Bard II; Easterlings; Erebor.",
       "To tie the North to the same War that consumes Gondor.",
       [
           "- **Siege.** Dale burns; Dwarves and Men retreat into Erebor.",
           "- **Deaths.** Brand and Dáin fall at the gate.",
           "- **Relief.** The Ring unmade; northern host breaks.",
       ],
       [
           ("Brand", f"{C}/brand-king-of-dale/", "King who fell."),
           ("Dáin Ironfoot", f"{C}/dain-ironfoot/", "King under the Mountain who fell with him."),
           ("Erebor", f"{L}/erebor/", "Fortress of the defence."),
       ],
       "Readers who skip appendices miss that the War was global—the South's victory saves the North hours later.")

    md("events", "colloquy-at-orthanc", "The Colloquy at Orthanc",
       "Gandalf's confrontation with Saruman at the flooded ring of Isengard where the wizard's staff is broken and he is cast from the Order.",
       ["council", "isengard"], "Orthanc, 5 March T.A. 3019", "Third Age 5 March 3019",
       "After Helm's Deep the victors ride to Isengard and find Saruman trapped in Orthanc. Gandalf offers mercy; Saruman refuses and tries the Voice. The staff is broken; Saruman is cast from the Istari. Gríma throws the palantír; Pippin picks it up—setting later trouble.",
       "Event (confrontation)",
       "Follows Ents' flooding of Isengard.",
       "Gandalf; Saruman; Théoden; Aragorn; Legolas; Gimli; Merry; Pippin; Treebeard.",
       "To end Saruman's open war and strip his authority.",
       [
           "- **The Voice.** Saruman nearly turns the listeners.",
           "- **The break.** Gandalf shatters his staff.",
           "- **The stone.** Palantír falls to Pippin.",
       ],
       [
           ("Saruman", f"{C}/saruman/", "Cast down."),
           ("Orthanc", f"{L}/orthanc/", "Tower of the parley."),
           ("Isengard", f"{L}/isengard/", "Ring-fortress already flooded."),
           ("Gandalf", f"{C}/gandalf/", "White authority who judges him."),
       ],
       "Orthanc is Saruman's last throne—persuasion instead of armies, and failure of both.")
