export type Category = "characters" | "locations" | "events" | "peoples";

export type Entry = {
  slug: string;
  category: Category;
  name: string;
  epithet: string;
  era: string;
  summary: string;
  body: string[];
  related: string[];
  tags: string[];
};

export const categories: {
  id: Category;
  title: string;
  blurb: string;
}[] = [
  {
    id: "characters",
    title: "Characters",
    blurb: "Wanderers, kings, and keepers of the Ring.",
  },
  {
    id: "locations",
    title: "Locations",
    blurb: "Realms of light, shadow, and everything between.",
  },
  {
    id: "events",
    title: "Events",
    blurb: "The turning points of the Third Age.",
  },
  {
    id: "peoples",
    title: "Peoples",
    blurb: "The kindreds who shaped Middle-earth.",
  },
];

export const entries: Entry[] = [
  {
    slug: "frodo-baggins",
    category: "characters",
    name: "Frodo Baggins",
    epithet: "Ring-bearer of the Shire",
    era: "Third Age",
    summary:
      "A hobbit of Bag End who inherits the One Ring and carries it into the heart of Mordor, paying a cost that even victory cannot fully restore.",
    body: [
      "Frodo is the heir of Bilbo Baggins, raised among the gentle rhythms of Hobbiton and unprepared, at first, for the weight of an heirloom that is not merely gold. When the truth of the Ring is revealed, he does not claim a quest so much as accept a duty: the thing cannot stay in the Shire, and someone must take it away.",
      "His courage is quiet rather than martial. Along the Road he learns the difference between endurance and hope, between friendship and the lonely work of bearing a will that is not his own. The Ring wears at him, sharpening fear and suspicion, yet he continues because turning back would make the Shire itself a battlefield.",
      "At Mount Doom he reaches the limit of that endurance. The quest succeeds not because he remains uncorrupted, but because mercy shown years earlier to Gollum still has a place in the story. After the War, Frodo is honored in Gondor and the Shire alike, yet the wounds of blade, sting, and burden do not heal in the mortal lands. He sails West, leaving the chronicle of his journey to those who remain.",
    ],
    related: ["samwise-gamgee", "gollum", "one-ring", "shire", "mount-doom"],
    tags: ["hobbit", "fellowship", "ring-bearer"],
  },
  {
    slug: "samwise-gamgee",
    category: "characters",
    name: "Samwise Gamgee",
    epithet: "Gardener of Bag End",
    era: "Third Age",
    summary:
      "Frodo’s gardener and closest companion, whose loyalty, practical courage, and stubborn hope keep the quest alive when strength and light fail.",
    body: [
      "Sam begins as a listener at windows and a tender of gardens. What looks like rustic simplicity is, in truth, a deep loyalty: he will not let his master walk into darkness alone. He carries pans, rope, and lembas with the same seriousness others reserve for swords.",
      "On the stairs of Cirith Ungol and in the wastes of Mordor, Sam becomes more than a servant. He fights Shelob, bears the Ring for a time without claiming it as a crown, and speaks hope into a journey that has almost no remaining language for hope. His love of growing things is not comic relief; it is a counter-spell against the barren will of Sauron.",
      "After the War he returns to the Shire, marries, plants, and helps heal a land that was briefly spoiled. In later years he too is granted passage over the Sea, a rare honor for one who never sought it.",
    ],
    related: ["frodo-baggins", "shire", "cirith-ungol", "gollum"],
    tags: ["hobbit", "fellowship"],
  },
  {
    slug: "aragorn",
    category: "characters",
    name: "Aragorn",
    epithet: "Heir of Isildur, King Elessar",
    era: "Third Age",
    summary:
      "A Ranger of the North who walks in exile for decades, then claims the thrones of Arnor and Gondor and closes the age of hidden kings.",
    body: [
      "Raised in Rivendell under the name Estel, Aragorn learns early that lineage is both a promise and a danger. Isildur’s heir is hunted, and the North-kingdom is a memory. He serves in Rohan and Gondor under other names, studies the wilds as Strider, and waits until the War of the Ring forces the hidden claim into the open.",
      "His kingship is not merely a coronation. He walks the Paths of the Dead, commands at Pelennor and the Black Gate, and heals in the Houses of Healing when the shadow of the Nazgûl still clings to the wounded. The crown is the last act of a life already spent in service.",
      "As Elessar he marries Arwen, restores the northern realm, and ushers in the Fourth Age. The story of Aragorn is the story of patience: a man who could have seized power early and instead earned the right to wear it.",
    ],
    related: ["arwen", "rivendell", "gondor", "paths-of-the-dead", "anduril"],
    tags: ["man", "dunadan", "fellowship", "king"],
  },
  {
    slug: "gandalf",
    category: "characters",
    name: "Gandalf",
    epithet: "Mithrandir, the Grey then White",
    era: "Third Age",
    summary:
      "An Istar sent to contest Sauron by counsel rather than conquest, who dies in Moria and returns with authority enough to break Saruman’s claim to leadership.",
    body: [
      "Among the Wise, Gandalf is the wanderer: pipe-smoke, sharp words, and a habit of arriving where he is least invited and most needed. He studies the Ring’s history, stirs hobbits from their comfort, and distrusts the easy solutions of force. Where Saruman seeks to order the world, Gandalf seeks to keep its peoples free to choose.",
      "In Moria he falls with the Balrog, a duel that takes him out of the Fellowship’s sight and out of his first form. He returns as Gandalf the White, not a different person but a completed charge: the enemy’s chief wizard has fallen into pride, and the West needs a leader who will not sit in a tower and call that wisdom.",
      "He marshals Rohan, Gondor, and the last alliance of free peoples at the Morannon, buying time for two hobbits he cannot follow. When the Third Age ends, his task in Middle-earth is done, and he sails into the West.",
    ],
    related: ["saruman", "moria", "shire", "istari"],
    tags: ["maia", "wizard", "fellowship"],
  },
  {
    slug: "legolas",
    category: "characters",
    name: "Legolas",
    epithet: "Prince of the Woodland Realm",
    era: "Third Age",
    summary:
      "An Elf of Mirkwood whose keen sight and light step serve the Fellowship, and whose friendship with Gimli becomes one of the Age’s quieter healings.",
    body: [
      "Legolas comes to Rivendell as a messenger of Thranduil and leaves as a companion of the Ring. He is swift in forest and on stone, a bowman whose skill is legendary even among Elves, yet the War teaches him the worth of companions who are not of his kind.",
      "His rivalry with Gimli begins in old grievances between Elf and Dwarf and ends in a friendship that outlasts the quest. After the War he brings woodland folk to Ithilien and, in time, builds a ship to follow the Straight Road, taking Gimli with him—an ending almost unheard of in the older songs.",
    ],
    related: ["gimli", "mirkwood", "fellowship-of-the-ring"],
    tags: ["elf", "fellowship"],
  },
  {
    slug: "gimli",
    category: "characters",
    name: "Gimli",
    epithet: "Son of Glóin",
    era: "Third Age",
    summary:
      "A Dwarf of Erebor who joins the Fellowship, fights at Helm’s Deep and the Pelennor, and becomes Galadriel’s unlikely champion among his own people.",
    body: [
      "Gimli enters the story as a representative of Durin’s folk, wary of Elves and proud of the stone-halls of his fathers. Moria is both pilgrimage and grief: he sees Khazad-dûm as it is, not as the songs still pretend it to be.",
      "He is a warrior of the axe, counting foes at Helm’s Deep with grim humor, yet he is also moved to reverence in Lothlórien. The gift of Galadriel’s hair becomes, for him, a treasure beyond mithril. In the Fourth Age he leads Dwarves to the glittering caves of Aglarond and is remembered as the Elf-friend who sailed West.",
    ],
    related: ["legolas", "moria", "lothlorien", "helms-deep"],
    tags: ["dwarf", "fellowship"],
  },
  {
    slug: "boromir",
    category: "characters",
    name: "Boromir",
    epithet: "Captain of Gondor",
    era: "Third Age",
    summary:
      "Denethor’s heir, whose love of Minas Tirith leads him to desire the Ring as a weapon, and whose last stand for Merry and Pippin restores his honor.",
    body: [
      "Boromir comes to Rivendell seeking counsel for a city that has held the line against Mordor for too long with too little help. He is brave, open-handed, and convinced that power used in Gondor’s defense cannot be wholly evil. That conviction is the Ring’s doorway.",
      "He tries to take the Ring from Frodo at Parth Galen, then immediately understands what he has become. His death at Amon Hen—horn broken, body ringed with arrows, hobbits carried off—is the Fellowship’s first true breaking. Aragorn, Legolas, and Gimli honor him as a captain of the West, not as the man who stumbled.",
    ],
    related: ["faramir", "gondor", "breaking-of-the-fellowship", "frodo-baggins"],
    tags: ["man", "gondor", "fellowship"],
  },
  {
    slug: "meriadoc-brandybuck",
    category: "characters",
    name: "Meriadoc Brandybuck",
    epithet: "Merry of Buckland",
    era: "Third Age",
    summary:
      "A conspirator of the Shire who rides to war with Rohan and helps unmake the Witch-king on the Pelennor Fields.",
    body: [
      "Merry is curious, well-read by hobbit standards, and more involved in the ‘conspiracy’ to aid Frodo than Frodo ever planned. He is captured with Pippin, escapes into Fangorn’s orbit, and swears service to Théoden.",
      "Forbidden the ride to Minas Tirith, he goes anyway, small in the saddle behind Éowyn. Together they strike the Lord of the Nazgûl, a deed no Man was said to accomplish. After the War he is a Master of Buckland, a writer of herblore, and a reminder that the Shire’s borders were never as far from history as they seemed.",
    ],
    related: ["peregrin-took", "eowyn", "pelennor-fields", "rohan"],
    tags: ["hobbit", "fellowship"],
  },
  {
    slug: "peregrin-took",
    category: "characters",
    name: "Peregrin Took",
    epithet: "Pippin, Guard of the Citadel",
    era: "Third Age",
    summary:
      "The youngest of the four hobbits, whose curiosity costs the Fellowship in Moria and later saves Faramir from his father’s pyre.",
    body: [
      "Pippin’s stone in the well of Moria is a child’s mistake with adult consequences. He grows quickly after that: prisoner of the Uruk-hai, guest of Treebeard, and then a soldier of Gondor who looks into the palantír and draws Sauron’s eye at a crucial hour.",
      "In Minas Tirith he serves Denethor, sees the steward’s despair clearly, and acts. His warning brings Gandalf to the tombs in time to save Faramir. He later fights at the Black Gate and returns home a knight in all but the Shire’s informal sense of the word.",
    ],
    related: ["meriadoc-brandybuck", "denethor", "minas-tirith", "treebeard"],
    tags: ["hobbit", "fellowship"],
  },
  {
    slug: "gollum",
    category: "characters",
    name: "Gollum",
    epithet: "Sméagol, the Trailer",
    era: "Third Age",
    summary:
      "A hobbit-kind twisted by centuries with the Ring, who guides Frodo to Mordor and, in seizing his Precious at the end, completes the quest he meant to betray.",
    body: [
      "Once Sméagol of the Stoor-kind, he murders Déagol for a gold ring found on a river-bed and flees into the dark under the Misty Mountains. Time, hunger, and the Ring split him into a creature who talks to himself because there is no one else left to hear.",
      "He hates the thief Baggins and loves the Ring past the point of identity. Captured, questioned, and bound to Frodo by an oath on the Precious, he becomes a guide of dreadful competence. His two minds war on the stairs: Sméagol almost chooses mercy; Gollum chooses Shelob.",
      "At the Crack of Doom he bites the Ring from Frodo’s hand and falls. The chronicle does not call this redemption so much as a terrible necessity: the Ring could not be cast away by a bearer still standing. Bilbo’s pity, and Frodo’s after it, is what left Gollum alive to be that necessity.",
    ],
    related: ["frodo-baggins", "one-ring", "mount-doom", "bilbo-baggins"],
    tags: ["stoor", "ring"],
  },
  {
    slug: "galadriel",
    category: "characters",
    name: "Galadriel",
    epithet: "Lady of Lothlórien",
    era: "First Age to Third Age",
    summary:
      "One of the greatest of the Noldor remaining in Middle-earth, who refuses the Ring when it is freely offered and thereby passes the last test of her long exile.",
    body: [
      "Galadriel’s memory reaches back to the light of the Two Trees. She has been rebel, exile, and queen of a hidden wood where time itself seems slowed by the power of Nenya. To the Fellowship she is both host and examiner, showing each of them a possible desire.",
      "When Frodo offers her the One Ring, she speaks the temptation aloud: a queen terrible and beautiful as the Sea. Then she laughs, diminishes, and remains Galadriel. That refusal is as important as any battle in the War. After Sauron’s fall, the power of the Three fades, and she sails West with the Ring-bearers.",
    ],
    related: ["lothlorien", "elrond", "celeborn", "one-ring"],
    tags: ["elf", "noldor", "ring-bearer"],
  },
  {
    slug: "elrond",
    category: "characters",
    name: "Elrond",
    epithet: "Master of Rivendell",
    era: "First Age to Third Age",
    summary:
      "Half-elven lord who chose the Firstborn, kept one of the Three Rings, and convened the Council that set the Quest of Mount Doom in motion.",
    body: [
      "Elrond is a keeper of memory: the Last Alliance, Isildur’s failure, the long watch against Angmar. Rivendell is his answer to a world that forgets—a house of healing, lore, and delayed endings. He raises Aragorn, fosters the shards of Narsil, and knows that hiding the Ring is no longer possible.",
      "The Council of Elrond is his great political act of the War: he does not command the Quest, but he makes a place where hobbit, dwarf, elf, and man can agree to try the impossible. When the Third Age closes, he too takes ship, leaving his daughter Arwen to her mortal choice.",
    ],
    related: ["rivendell", "arwen", "council-of-elrond", "aragorn"],
    tags: ["half-elven", "ring-bearer"],
  },
  {
    slug: "arwen",
    category: "characters",
    name: "Arwen Undómiel",
    epithet: "Evenstar of her people",
    era: "Third Age",
    summary:
      "Daughter of Elrond who chooses a mortal life with Aragorn, binding the fading of the Elves to the renewal of the kingdoms of Men.",
    body: [
      "Arwen is often seen at a distance in the War itself—a banner, a memory, a future. Her choice is the old choice of Lúthien: love over the undying life of her kind. She waits in Rivendell while Aragorn walks the wild, and she rides to Minas Tirith when the crown is won.",
      "Her marriage is not an ornament to the victory. It is the joining of lines that the First Age left sundered, and a quiet acknowledgment that the age of the Elves is ending by consent as much as by defeat.",
    ],
    related: ["aragorn", "elrond", "rivendell", "minas-tirith"],
    tags: ["half-elven"],
  },
  {
    slug: "sauron",
    category: "characters",
    name: "Sauron",
    epithet: "The Dark Lord of Mordor",
    era: "Second Age to Third Age",
    summary:
      "A Maia of Aulë who became Morgoth’s lieutenant, forged the One Ring to dominate the wearers of the others, and spent the Third Age as a lidless will searching for its return.",
    body: [
      "Sauron is not a mindless storm. He is order without mercy: the desire to perfect the world by owning it. In Eregion he taught ring-craft as Annatar; in Númenor he taught pride until the island broke. After his bodily overthrow at the end of the Second Age, he rebuilt in secret, first as the Necromancer of Dol Guldur, then as the Lidless Eye in Barad-dûr.",
      "He cannot imagine that anyone would try to destroy the Ring rather than use it. That failure of imagination is the crack in his power. When the Ring is unmade, the greater part of himself—poured into that gold—goes with it, and the towers of Mordor fall as a will falls, not merely as stone.",
    ],
    related: ["one-ring", "mordor", "barad-dur", "nazgul"],
    tags: ["maia", "dark lord"],
  },
  {
    slug: "saruman",
    category: "characters",
    name: "Saruman",
    epithet: "Curunír of Isengard",
    era: "Third Age",
    summary:
      "Chief of the Istari who studies the Enemy in order to rival him, turning Isengard into a factory of war and his own voice into a weapon.",
    body: [
      "Saruman begins as a scholar of ring-lore and a voice the White Council trusts. Study becomes imitation. He looks into a palantír, bargains with Mordor, and decides that the West is too weak to win by old virtues. Orcs, wolves, and the burning of Fangorn’s borders are the visible form of that decision.",
      "His voice almost turns Théoden to despair and the Ents to delay. When Isengard is flooded and his staff is broken, he is left a beggar of spite. The Scouring of the Shire is his last petty kingdom: a wizard reduced to a boss of ruffians, slain by the servant he had taught to cringe.",
    ],
    related: ["isengard", "treebeard", "gandalf", "scouring-of-the-shire"],
    tags: ["maia", "wizard"],
  },
  {
    slug: "eowyn",
    category: "characters",
    name: "Éowyn",
    epithet: "Shieldmaiden of Rohan",
    era: "Third Age",
    summary:
      "Niece of Théoden who refuses a life of waiting, rides to war in secret, and slays the Witch-king beside Merry.",
    body: [
      "Éowyn’s cage is made of love and custom: she is needed at home, praised for her beauty, and denied the honor given to riders. Gríma’s gaze and the king’s decline sharpen her despair into a wish for a glorious death.",
      "Disguised as Dernhelm, she faces the Witch-king when Théoden falls. Her answer to the wraith’s boast—that no living man may hinder him—is not a riddle but a fact. Later, in the Houses of Healing, she lays down the death-wish and chooses a living future with Faramir in Ithilien.",
    ],
    related: ["theoden", "meriadoc-brandybuck", "faramir", "pelennor-fields"],
    tags: ["human", "rohan"],
  },
  {
    slug: "theoden",
    category: "characters",
    name: "Théoden",
    epithet: "King of the Mark",
    era: "Third Age",
    summary:
      "A king aged by poison and counsel until Gandalf wakes him, after which he rides to Helm’s Deep and dies in splendor on the Pelennor.",
    body: [
      "Under Wormtongue, Théoden is a hall of shadows: the king still sits, but the Mark is already half-lost. Gandalf’s coming is a restoration of will as much as of health. Théoden then does what kings of Rohan are for: he rides.",
      "He holds the Hornburg, answers Gondor’s red arrow, and leads the charge that breaks the first terror of the Pelennor. His death beneath the Witch-king is the death he would have chosen once his mind was his own again: among riders, with his people watching.",
    ],
    related: ["eowyn", "eomer", "helms-deep", "edoras"],
    tags: ["human", "rohan", "king"],
  },
  {
    slug: "faramir",
    category: "characters",
    name: "Faramir",
    epithet: "Captain of Gondor, later Steward and Prince",
    era: "Third Age",
    summary:
      "Younger son of Denethor who understands the Ring’s danger, spares Frodo, and survives his father’s pyre to help heal the South-kingdom.",
    body: [
      "Faramir loves lore and the woods of Ithilien as much as he loves the White City. Where Boromir saw a weapon, Faramir sees a test. He has the hobbits in his power and lets them go, asking only that they remember Gondor as something other than a grasping hand.",
      "Wounded in the retreat from Osgiliath, he is nearly burned in Denethor’s despair. Healed, he becomes steward in the king’s name and husband to Éowyn, a pairing of two people who learned that survival can be a form of courage.",
    ],
    related: ["boromir", "denethor", "ithilien", "eowyn"],
    tags: ["human", "gondor"],
  },
  {
    slug: "denethor",
    category: "characters",
    name: "Denethor II",
    epithet: "Steward of Gondor",
    era: "Third Age",
    summary:
      "A proud ruler who matches Sauron in the palantír too long, reads only defeat in its visions, and chooses fire rather than a king he will not wait to see.",
    body: [
      "Denethor is no fool and no coward. He has held Gondor with intelligence and grim will. The palantír shows him true things—armies, fleets, the Dark Lord’s strength—and he lacks the humility to remember that true things can still be incomplete.",
      "Boromir’s death and Faramir’s wounding break the last of his hope. He would burn with his son rather than yield the rod of the stewards. His end is a warning the chronicle keeps close: wisdom without trust becomes a kind of eye, and an eye can be mastered.",
    ],
    related: ["faramir", "boromir", "minas-tirith", "sauron"],
    tags: ["human", "gondor"],
  },
  {
    slug: "treebeard",
    category: "characters",
    name: "Treebeard",
    epithet: "Fangorn, eldest of the Ents",
    era: "Elder Days to Third Age",
    summary:
      "Shepherd of trees whose slowness hides a vast anger; he leads the last march of the Ents against Isengard.",
    body: [
      "Treebeard is a memory with roots. He remembers a world with more woods and fewer orcs, and he has learned to speak in the long measure of growing things. Merry and Pippin do not hurry him so much as remind him that the world has already hurried past the Ents.",
      "The Entmoot decides for war. Isengard is unmade not by siege engines but by the land itself rising: water, stone, and trees reclaiming a wizard’s factory. Afterward Treebeard keeps Saruman caged for a time, still hoping, perhaps, that voices can change.",
    ],
    related: ["fangorn", "isengard", "peregrin-took", "ents"],
    tags: ["ent"],
  },
  {
    slug: "bilbo-baggins",
    category: "characters",
    name: "Bilbo Baggins",
    epithet: "Burglar of Erebor, uncle of Frodo",
    era: "Third Age",
    summary:
      "The hobbit whose adventure under the Mountain brought the Ring into the Shire, and whose pity for Gollum shaped the fate of the Age.",
    body: [
      "Bilbo’s tale is the comic door that opens onto epic. He leaves Bag End for a share of treasure and returns with a ring he thinks is only useful. Decades later, the leaving of that ring—almost failed, then completed with Gandalf’s help—is the first victory of the War.",
      "In Rivendell he is a poet of fading memory, still sharp enough to offer verses and a small sword. He does not walk to Mordor, but the mercy he showed in the dark under the mountains walks there in his stead.",
    ],
    related: ["frodo-baggins", "gollum", "shire", "rivendell"],
    tags: ["hobbit", "ring-bearer"],
  },
  {
    slug: "witch-king",
    category: "characters",
    name: "The Witch-king of Angmar",
    epithet: "Lord of the Nazgûl",
    era: "Second Age to Third Age",
    summary:
      "Chief of the Ringwraiths, once a king of Men, who breaks the gates of Minas Tirith and falls to Éowyn and Merry.",
    body: [
      "The Witch-king is the shape fear takes when it wears a crown. He destroyed the North-kingdom in the wars of Angmar, then returned to Mordor as the Dark Lord’s most terrible captain. At Weathertop he wounds Frodo with a Morgul-knife; at Pelennor he comes as a winged death.",
      "Prophecy said no man would kill him. The prophecy was kept. His fall is the turning of the battle’s terror, though the War itself is not yet done.",
    ],
    related: ["nazgul", "pelennor-fields", "eowyn", "minas-tirith"],
    tags: ["nazgul", "wraith"],
  },
  {
    slug: "shire",
    category: "locations",
    name: "The Shire",
    epithet: "Four Farthings of the hobbits",
    era: "Third Age",
    summary:
      "A green, ordered land between the Brandywine and the Far Downs, whose peace is the thing the Quest is meant to save—and which does not remain untouched.",
    body: [
      "The Shire is farms, family names, and a suspicion of anything that happens faster than a harvest. Its borders are watched by Rangers the hobbits barely notice. That unnoticed protection is part of the joke and part of the design: the small are kept small so the great wars can rage elsewhere.",
      "Bag End, Bywater, Buckland, and the Green Dragon are the homely map of the chronicle. When Saruman’s ruffians fence and fell and mill the water into mud, the hobbits discover they can fight for a pantry as fiercely as Gondor fights for a tower. The Scouring is the Shire’s own war, brief and bitterly local.",
    ],
    related: ["frodo-baggins", "scouring-of-the-shire", "hobbits"],
    tags: ["eriador", "homeland"],
  },
  {
    slug: "rivendell",
    category: "locations",
    name: "Rivendell",
    epithet: "Imladris, the Last Homely House",
    era: "Second Age to Third Age",
    summary:
      "Elrond’s hidden valley east of the Misty Mountains’ western feet, a refuge of lore, healing, and delayed farewells.",
    body: [
      "Rivendell is reached by a Ford that can rise in anger and by paths that do not care to be found. Within, the air is of old songs and running water. It is not a fortress in the Gondorian sense; it is a pause in the fading of the Elves.",
      "Here the shards of Narsil are kept, the Council is held, and the Fellowship is named. Travelers remember it as the last place where the Quest still felt like a story with a fireside.",
    ],
    related: ["elrond", "council-of-elrond", "aragorn"],
    tags: ["elf-home", "eriador"],
  },
  {
    slug: "lothlorien",
    category: "locations",
    name: "Lothlórien",
    epithet: "The Golden Wood",
    era: "Third Age",
    summary:
      "A mallorn forest held in a kind of remembered spring by Galadriel’s ring, closed to most of the world and open, briefly, to the Fellowship.",
    body: [
      "Time in Lórien does not pass as it does on the Anduin. The wood is guarded by unseen borders and by the will of its Lady. To Gimli it is at first a place of rumor and danger; to the others it is rest after Moria’s dark.",
      "The Fellowship leaves with boats, cloaks, and gifts that will matter more than they guess. When the One is destroyed, Lórien’s enchantment thins. The Golden Wood becomes, like so much Elvish art, a memory of how the world once felt.",
    ],
    related: ["galadriel", "anduin", "fellowship-of-the-ring"],
    tags: ["elf-home"],
  },
  {
    slug: "moria",
    category: "locations",
    name: "Moria",
    epithet: "Khazad-dûm",
    era: "Elder Days to Third Age",
    summary:
      "The greatest mansion of Durin’s folk, ruined by the awakening of a Balrog and crossed in terror by the Fellowship.",
    body: [
      "Khazad-dûm was a city of light under the mountains, rich in mithril and pride. Durin’s Bane turned it into a name of dread. By the late Third Age it is a maze of drums, orcs, and a darkness that is not empty.",
      "Gandalf’s fall on the Bridge of Khazad-dûm is the Fellowship’s first irreversible loss. Gimli’s grief is for a home that can be visited only as a tomb. After the War, Dwarves look again toward those halls, but the chronicle of the Ring treats Moria as a trial of underground night.",
    ],
    related: ["gandalf", "gimli", "fellowship-of-the-ring"],
    tags: ["dwarf-home", "misty-mountains"],
  },
  {
    slug: "rohan",
    category: "locations",
    name: "Rohan",
    epithet: "The Riddermark",
    era: "Third Age",
    summary:
      "A land of grass and horses given to the Éothéod, whose riders become Gondor’s most famous allies in the War of the Ring.",
    body: [
      "Rohan is weather and hooves: the Wold, the Entwash, the snows of the White Mountains. Its people are not Númenórean by blood, but they keep an older northern courage. Edoras and the Golden Hall are the heart; the Westfold is the wound Saruman opens.",
      "The War in Rohan is Helm’s Deep and the mustering of the Mark. Without those riders, Minas Tirith’s field would have been a graveyard without a song.",
    ],
    related: ["edoras", "helms-deep", "theoden", "eomer"],
    tags: ["kingdom", "men"],
  },
  {
    slug: "edoras",
    category: "locations",
    name: "Edoras",
    epithet: "Seat of the Golden Hall",
    era: "Third Age",
    summary:
      "The capital of Rohan, a hill-town of thatch and wind below the White Mountains, where Théoden is woken and the war-horn of the Mark is sounded.",
    body: [
      "Meduseld shines even when the king does not. Edoras is exposed, proud, and close to the memory of Helm’s Deep. From its steps one sees the plains that are both wealth and vulnerability.",
      "Gandalf’s confrontation in the hall returns a people to themselves. After that day, Edoras is less a setting than a starting gate for war.",
    ],
    related: ["rohan", "theoden", "gandalf"],
    tags: ["city", "rohan"],
  },
  {
    slug: "helms-deep",
    category: "locations",
    name: "Helm’s Deep",
    epithet: "The Hornburg",
    era: "Third Age",
    summary:
      "A fortress in the gorge of the White Mountains where Rohan withstands Saruman’s host until dawn, trees, and Gandalf’s riders turn the siege.",
    body: [
      "The Deeping Wall and the Hornburg are Rohan’s answer to numbers. Here the old, the young, and a handful of Elves in some tellings—always the Rohirrim and three hunters in the core tale—hold against Uruk-hai and blasting fire.",
      "The battle is won by endurance plus a charge at sunrise and the sudden forest that should not be there. Helm’s Deep becomes the proof that Isengard can bleed.",
    ],
    related: ["rohan", "saruman", "aragorn", "gimli"],
    tags: ["fortress", "battle"],
  },
  {
    slug: "gondor",
    category: "locations",
    name: "Gondor",
    epithet: "The South-kingdom",
    era: "Third Age",
    summary:
      "Realm of the Dúnedain in the south, diminished yet unbroken, whose White City and coastal fiefs take the main blow of Sauron’s war.",
    body: [
      "Gondor is stone, lineage, and a long decline that never quite becomes fall. Its stewards rule in the name of kings who do not come. Osgiliath is ruined, Ithilien is a march of rangers, and still the banners of the White Tree are kept.",
      "The War of the Ring is, for Gondor, existence itself: siege, field, and the sudden return of a king out of the North. The Fourth Age is Gondor’s second spring.",
    ],
    related: ["minas-tirith", "faramir", "aragorn", "pelennor-fields"],
    tags: ["kingdom", "men", "numenor"],
  },
  {
    slug: "minas-tirith",
    category: "locations",
    name: "Minas Tirith",
    epithet: "The White City, Tower of Guard",
    era: "Third Age",
    summary:
      "Seven-tiered capital of Gondor on the Hill of Guard, last great fortress of the West against the Shadow in the East.",
    body: [
      "Minas Tirith faces Mordor as a white question the Dark Lord has not yet answered. Its gates, walls, and silent throne-room hold a people who remember better days and still refuse to leave.",
      "The siege breaks the first gate, fills the sky with fear, and is lifted by Rohan and the black ships that are not the enemy’s after all. Crowning day on the city’s high court is the visible end of the Stewards’ long watch.",
    ],
    related: ["gondor", "pelennor-fields", "denethor", "aragorn"],
    tags: ["city", "gondor"],
  },
  {
    slug: "mordor",
    category: "locations",
    name: "Mordor",
    epithet: "The Black Land",
    era: "Second Age to Third Age",
    summary:
      "Sauron’s fenced realm of ash, fortresses, and slave-fields, entered by stealth when war has drawn its armies outward.",
    body: [
      "Mordor is geography as prison: mountains on three sides, the Morannon in the north, Cirith Ungol in the west. Inside are the Plateau of Gorgoroth, the Road, and the Eye. It is industrial evil: pits, forges, and a landscape taught not to grow.",
      "Frodo and Sam cross it as beggars in orc-gear, small enough to be overlooked. Their success depends on Sauron looking everywhere except at his own feet.",
    ],
    related: ["mount-doom", "barad-dur", "cirith-ungol", "sauron"],
    tags: ["dark realm"],
  },
  {
    slug: "mount-doom",
    category: "locations",
    name: "Mount Doom",
    epithet: "Orodruin, Amon Amarth",
    era: "Second Age to Third Age",
    summary:
      "The volcano where the One Ring was forged and the only fire in which it can be unmade.",
    body: [
      "Orodruin is both furnace and altar. Sauron’s ring-craft is bound to its Sammath Naur, a chamber of fire and will. The mountain wakes when the Dark Lord wakes; its ashen breath is Mordor’s weather.",
      "The Quest ends on a road of cracked stone and a struggle at the brink. The mountain takes Gollum, the Ring, and a piece of Frodo that will never come back.",
    ],
    related: ["one-ring", "frodo-baggins", "gollum", "destruction-of-the-ring"],
    tags: ["mordor"],
  },
  {
    slug: "isengard",
    category: "locations",
    name: "Isengard",
    epithet: "Angrenost, the Wizard’s Vale",
    era: "Third Age",
    summary:
      "A ring of stone around the tower of Orthanc, transformed by Saruman from a guard of Gondor into a pit of war-engines and orc-breeding.",
    body: [
      "Orthanc cannot be broken by Ents; the circle of Isengard can. Saruman fills the vale with wheels, fires, and a mockery of forests. The palantír in the tower is his leash to Mordor and his mirror of pride.",
      "The flooding of Isengard is the land’s revenge. What remains is a stone island in a lake, a wizard shouting at the world that no longer answers.",
    ],
    related: ["saruman", "treebeard", "orthanc"],
    tags: ["fortress"],
  },
  {
    slug: "fangorn",
    category: "locations",
    name: "Fangorn Forest",
    epithet: "Home of the Ents",
    era: "Elder Days to Third Age",
    summary:
      "An ancient wood on Rohan’s border, slow to anger and terrible when it finally marches.",
    body: [
      "Fangorn is older than the kingdoms around it. Men call it haunted; Ents call it a remnant. Merry and Pippin find that the trees have shepherds, and the shepherds have names longer than campaigns.",
      "The forest’s intervention in the War is local and decisive: it ruins Isengard and later appears as a sudden wood of Huorns at Helm’s Deep. Then it goes still again, as woods do when the axes stop.",
    ],
    related: ["treebeard", "ents", "isengard"],
    tags: ["forest"],
  },
  {
    slug: "ithilien",
    category: "locations",
    name: "Ithilien",
    epithet: "Garden of Gondor",
    era: "Third Age",
    summary:
      "A fair land between Anduin and the Mountains of Shadow, fought over until it becomes a princedom of healing after the War.",
    body: [
      "Ithilien still remembers being beautiful. Rangers move through its groves like a rumor. Faramir’s refuge at Henneth Annûn is a window of green in a war of ash.",
      "After the fall of Sauron, the land is given to Faramir and Éowyn to restore. Legolas brings Elven gardeners. The chronicle likes this ending: not every victory is a crown; some are orchards.",
    ],
    related: ["faramir", "gondor", "eowyn"],
    tags: ["gondor"],
  },
  {
    slug: "weathertop",
    category: "locations",
    name: "Weathertop",
    epithet: "Amon Sûl",
    era: "Third Age",
    summary:
      "A ruined watchtower on the Great East Road where Frodo is stabbed by the Witch-king and the hunt of the Ringwraiths becomes a race against fading.",
    body: [
      "Amon Sûl once held a palantír and the pride of Arnor. In Frodo’s day it is wind, broken stone, and a skyline visible to enemies. The camp on its hill is a mistake born of weariness.",
      "The Morgul-wound that Frodo takes here is the first true mark of the Shadow on the Ring-bearer. Rivendell will slow it; it will never be as if it had not happened.",
    ],
    related: ["witch-king", "frodo-baggins", "nazgul"],
    tags: ["eriador", "ruin"],
  },
  {
    slug: "cirith-ungol",
    category: "locations",
    name: "Cirith Ungol",
    epithet: "Pass of the Spider",
    era: "Third Age",
    summary:
      "A high pass into Mordor guarded by a tower of orcs and by Shelob, chosen by Gollum as a path of betrayal.",
    body: [
      "The pass is a throat. Stairs, tunnels, and a darkness that has a body in it. Shelob is not Sauron’s servant so much as his neighbor, a hunger older than the current war.",
      "Sam’s fight in the tunnel and his rescue of Frodo from the orc-tower are the Quest’s most desperate hours. Afterward the hobbits are inside the trap they meant only to skirt.",
    ],
    related: ["gollum", "samwise-gamgee", "mordor"],
    tags: ["mordor", "pass"],
  },
  {
    slug: "grey-havens",
    category: "locations",
    name: "The Grey Havens",
    epithet: "Mithlond",
    era: "Second Age to Fourth Age",
    summary:
      "The Elven port on the Gulf of Lune from which the Ring-bearers take ship into the West at the end of the Third Age.",
    body: [
      "The Havens are an ending made of water and white timber. Círdan has kept ships for an age of leave-takings. When Gandalf, Elrond, Galadriel, Frodo, and Bilbo board, the Fourth Age of Men is already beginning behind them.",
      "Sam watches the ship diminish. The chronicle’s last taste of the Sea is not adventure but permission to rest.",
    ],
    related: ["frodo-baggins", "gandalf", "galadriel", "elrond"],
    tags: ["elf-home", "sea"],
  },
  {
    slug: "barad-dur",
    category: "locations",
    name: "Barad-dûr",
    epithet: "The Dark Tower",
    era: "Second Age to Third Age",
    summary:
      "Sauron’s fortress, bound in its foundations to the One Ring, which collapses when the Ring is destroyed.",
    body: [
      "Barad-dûr is will given battlements. It was raised with the Ring’s power and cannot stand when that power is gone. From its highest window the Eye searches, a metaphor so complete that many forget there was once a body behind it.",
      "The Tower’s fall is seen from the Field of Cormallen as a weather of ruin. Armies of Mordor become a crowd without a mind.",
    ],
    related: ["sauron", "mordor", "one-ring"],
    tags: ["fortress", "mordor"],
  },
  {
    slug: "council-of-elrond",
    category: "events",
    name: "The Council of Elrond",
    epithet: "Rivendell, 25 October 3018",
    era: "Third Age 3018",
    summary:
      "A gathering of the Free Peoples that hears the history of the Ring and chooses destruction over hiding, sending, or using it.",
    body: [
      "The Council is a rare hour in which lore, politics, and doom sit at one table. Boromir argues for the weapon of Gondor; others argue for the Sea or for burial. The Ring, present in the room, makes every speech a little too keen.",
      "Frodo’s offer to take it is not a strategy so much as a moral fact: the least likely bearer is the one least likely to turn the Quest into a new Dark Lord. The Fellowship is composed as a compromise of peoples and a guard for a hobbit’s feet.",
    ],
    related: ["elrond", "frodo-baggins", "rivendell", "one-ring"],
    tags: ["quest", "rivendell"],
  },
  {
    slug: "fellowship-of-the-ring",
    category: "events",
    name: "The Fellowship of the Ring",
    epithet: "Nine walkers against nine riders",
    era: "Third Age 3018–3019",
    summary:
      "The company named in Rivendell to escort the Ring south, broken at Parth Galen by treachery, death, and the Ring-bearer’s choice to go alone.",
    body: [
      "Nine is a number with an answer already in the world: the Nazgûl. The Fellowship is meant to be a living counter-spell. It fails as a single body and succeeds as a scattering of necessary errands: hobbits into Mordor, hunters into Rohan, a wizard back from death.",
      "Their road—Caradhras, Moria, Lórien, the Great River—is the last time so many kinds of people walk with one purpose and one secret. After Amon Hen, the War has many fronts and no more shared campfire.",
    ],
    related: ["breaking-of-the-fellowship", "council-of-elrond", "frodo-baggins"],
    tags: ["quest"],
  },
  {
    slug: "breaking-of-the-fellowship",
    category: "events",
    name: "The Breaking of the Fellowship",
    epithet: "Parth Galen and Amon Hen",
    era: "Third Age 26 February 3019",
    summary:
      "Boromir’s fall to the Ring’s lure, Frodo’s flight, the death of Gondor’s captain, and the capture of Merry and Pippin.",
    body: [
      "The breaking is several disasters happening in the same hour. Frodo puts on the Ring to escape a friend; Boromir dies defending two hobbits who are not the Ring-bearer; Aragorn must choose which grief to follow.",
      "He chooses the prisoners, trusting Frodo’s road to remain hidden. That choice sends the Three Hunters into the epic of Rohan and leaves the true Quest almost unarmed. Both roads prove necessary.",
    ],
    related: ["boromir", "frodo-baggins", "aragorn", "fellowship-of-the-ring"],
    tags: ["quest"],
  },
  {
    slug: "battle-of-helms-deep",
    category: "events",
    name: "The Battle of Helm’s Deep",
    epithet: "The Hornburg, 3–4 March 3019",
    era: "Third Age 3019",
    summary:
      "Rohan’s stand against Isengard’s host, ended by dawn, Gandalf, Erkenbrand, and the Huorns of Fangorn.",
    body: [
      "The battle is a night of wall-breaking and desperate sorties. Saruman means to end the Mark in a single blow so that Rohan cannot aid Gondor. He nearly succeeds.",
      "Victory here is the first loud defeat of the Wizard’s war-machine. It frees Théoden to ride south and shows that the White Hand can be broken without taking Orthanc by storm.",
    ],
    related: ["helms-deep", "theoden", "saruman", "rohan"],
    tags: ["battle", "rohan"],
  },
  {
    slug: "pelennor-fields",
    category: "events",
    name: "The Battle of the Pelennor Fields",
    epithet: "15 March 3019",
    era: "Third Age 3019",
    summary:
      "The great field-battle before Minas Tirith: the charge of Rohan, the fall of the Witch-king, and Aragorn’s coming in the black ships.",
    body: [
      "Pelennor is the War made visible: oliphaunts, wraiths, the Harlond, the white city smoking. Théoden’s charge is the song; Éowyn and Merry’s deed is the silence after the song; the Corsair ships turning out to be friends is the reversal no defender dared expect.",
      "The field is won, and still Mordor is not. The captains know they must next offer themselves as bait at the Morannon so that two small figures can crawl a little farther.",
    ],
    related: ["minas-tirith", "theoden", "eowyn", "aragorn"],
    tags: ["battle", "gondor"],
  },
  {
    slug: "destruction-of-the-ring",
    category: "events",
    name: "The Destruction of the One Ring",
    epithet: "Sammath Naur, 25 March 3019",
    era: "Third Age 3019",
    summary:
      "The unmaking of Sauron’s Ring in the fire of its forging, accomplished through Gollum’s seizure at the brink after Frodo claims the Ring.",
    body: [
      "No speech of Elrond assumed the bearer would remain himself at the end. The Ring’s last act is to be claimed. Gollum’s leap—joy, murder, and fall together—does what Frodo cannot.",
      "The date becomes Gondor’s New Year. Barad-dûr falls, the Nazgûl burn like shooting stars, and the War’s engine stops. What remains is healing, scouring, and the long grey road to the Sea.",
    ],
    related: ["mount-doom", "frodo-baggins", "gollum", "one-ring"],
    tags: ["quest", "mordor"],
  },
  {
    slug: "crowning-of-elessar",
    category: "events",
    name: "The Crowning of Elessar",
    epithet: "Minas Tirith, 1 May 3019",
    era: "Third Age 3019",
    summary:
      "Aragorn’s coronation as King of Gondor and Arnor, restoring the line of Elendil after a thousand years of stewards.",
    body: [
      "The crowning is ritual after ruin: a white tree found, a crown held by a wizard, a people remembering that they were waiting. Faramir yields the staff. The city becomes a capital again rather than a last redoubt.",
      "Midsummer brings Arwen. The marriage is the political and personal seal of the new age: Elves diminishing by love, Men rising by the same.",
    ],
    related: ["aragorn", "minas-tirith", "arwen", "gandalf"],
    tags: ["gondor", "kingship"],
  },
  {
    slug: "scouring-of-the-shire",
    category: "events",
    name: "The Scouring of the Shire",
    epithet: "November 3019",
    era: "Third Age 3019",
    summary:
      "The hobbits’ return to a homeland fenced, felled, and ruled by ruffians in Saruman’s employ, and their uprising at Bywater.",
    body: [
      "The epic does not end at the Black Gate. The Shire has been industrialized in miniature: ugly mills, felled avenues, a boss called Sharkey. Merry, Pippin, Sam, and Frodo—now soldiers in all but title—raise the countryside.",
      "The Battle of Bywater is small and enough. Saruman dies on the doorstep of Bag End. The point is not glory. It is that even saved worlds must be saved again at home, and that hobbits can do that work themselves.",
    ],
    related: ["shire", "saruman", "samwise-gamgee", "frodo-baggins"],
    tags: ["shire", "aftermath"],
  },
  {
    slug: "last-alliance",
    category: "events",
    name: "The Last Alliance",
    epithet: "End of the Second Age",
    era: "Second Age 3430–3441",
    summary:
      "The war of Elves and Men that threw Sauron down, when Isildur cut the Ring from his hand and would not destroy it.",
    body: [
      "On the slopes of Orodruin, Gil-galad and Elendil fall, and Isildur takes the enemy’s jewel as weregild. The Alliance is ‘last’ because the world will not again see such a joining of the two kindreds in full strength.",
      "Elrond remembers the failure at the fire. The entire Third Age is the bill for that unmade choice.",
    ],
    related: ["sauron", "one-ring", "elrond", "mount-doom"],
    tags: ["second-age", "war"],
  },
  {
    slug: "paths-of-the-dead",
    category: "events",
    name: "The Paths of the Dead",
    epithet: "Aragorn’s summons",
    era: "Third Age 3019",
    summary:
      "Aragorn’s journey through the Haunted Mountain to command the oath-breakers, winning the Corsair fleet for Gondor.",
    body: [
      "The Dead are a weapon no steward would touch. Aragorn, with the Grey Company, Legolas, and Gimli, takes the dark road because the Pelennor will not wait for ordinary marches.",
      "The oath fulfilled at Erech and the taking of the ships at Pelargir are kingship as terror turned to aid. The Dead are released; the living still have a field to fight.",
    ],
    related: ["aragorn", "pelennor-fields", "legolas", "gimli"],
    tags: ["dunharrow", "kingship"],
  },
  {
    slug: "hobbits",
    category: "peoples",
    name: "Hobbits",
    epithet: "The Halflings, the Little People",
    era: "Third Age",
    summary:
      "A shy, agrarian people of the Shire and Bree-land, overlooked by the great, and therefore suited to carry a burden that magnifies the will to dominate.",
    body: [
      "Hobbits love meals, genealogy, and not being bothered. Their courage, when it appears, looks like stubbornness: a refusal to leave a friend or a pantry to ruin. They are Harfoots, Stoors, and Fallohides in the old divisions, but the War knows them as four travelers and a countryside that wakes up late.",
      "The Wise guess that a hobbit’s small desire is harder for the Ring to inflame into empire. That guess is almost true, and the almost is the whole drama of Frodo and Sméagol.",
    ],
    related: ["shire", "frodo-baggins", "bilbo-baggins"],
    tags: ["kindred"],
  },
  {
    slug: "elves",
    category: "peoples",
    name: "Elves",
    epithet: "The Firstborn, the Eldar",
    era: "All Ages",
    summary:
      "The immortal people of starlight and craft, already fading in the Third Age, whose last great acts are counsel, refuge, and departure.",
    body: [
      "Elves are not a single mood. There are woodland princes, Noldorin exiles, and mariners who have been saying farewell since the First Age. Their rings preserve rather than conquer, and that preservation is itself a kind of refusal to let the world change.",
      "In the War they fight at times, but their deeper role is memory: they remember that Sauron has been thrown down before and that pride is how he returns.",
    ],
    related: ["galadriel", "elrond", "legolas", "grey-havens"],
    tags: ["kindred"],
  },
  {
    slug: "dwarves",
    category: "peoples",
    name: "Dwarves",
    epithet: "Khazâd, the Children of Aulë",
    era: "All Ages",
    summary:
      "A hardy people of stone and craft, makers of halls and grudges, whose representative in the Fellowship becomes an Elf-friend.",
    body: [
      "Dwarves endure. They mine, remember insults, and love work that outlasts a lifespan. Their rings kindled greed more than wraith-life; their doom in Moria was a Balrog, not a slow fade.",
      "Gimli’s path is unusual: reverence for Galadriel, friendship with Legolas, a colony in the Glittering Caves. The Fourth Age still has Dwarves under mountains, less sung but not gone.",
    ],
    related: ["gimli", "moria", "erebor"],
    tags: ["kindred"],
  },
  {
    slug: "men",
    category: "peoples",
    name: "Men",
    epithet: "The Followers, the Secondborn",
    era: "All Ages",
    summary:
      "Mortal peoples of many kingdoms—Dúnedain, Rohirrim, Easterlings, Haradrim—whose Age begins in earnest when the Elves depart.",
    body: [
      "Men are the chronicle’s future and its most divided present. Númenor’s heirs keep long life and longer memory; Rohan keeps horses and oaths; other nations ride under the Shadow for reasons the West rarely bothers to learn.",
      "The War of the Ring is the last time Elves and Dwarves stand so near the center. Afterward, the problems of Middle-earth become, more and more, the problems of Men.",
    ],
    related: ["aragorn", "gondor", "rohan", "nazgul"],
    tags: ["kindred"],
  },
  {
    slug: "ents",
    category: "peoples",
    name: "Ents",
    epithet: "Onodrim, the Shepherds of the Trees",
    era: "Elder Days to Third Age",
    summary:
      "Tree-herds whose language is slow and whose wrath, once gathered, unmakes a wizard’s fortress.",
    body: [
      "Ents were made to keep the woods from the axes of others. They lose the Entwives and, with them, a future of children. By the War they are a remnant that can still surprise a world that has filed them under folklore.",
      "Their march is the War’s strangest army: not cavalry, not knights, but the landscape choosing a side.",
    ],
    related: ["treebeard", "fangorn", "isengard"],
    tags: ["kindred"],
  },
  {
    slug: "orcs",
    category: "peoples",
    name: "Orcs",
    epithet: "Goblins, the hosts of the Dark Lord",
    era: "First Age to Third Age",
    summary:
      "A numerous, cruel soldiery bred for war, divided by masters and hatreds, forming the rank-and-file of both Mordor and Isengard.",
    body: [
      "Orcs are the War’s ordinary horror: not a unique evil like the Ring, but a system of fear, breeding pits, and stolen crafts. They quarrel among themselves as readily as they obey, which twice aids the hobbits inside Mordor.",
      "Uruk-hai are Saruman’s attempt at a better weapon. The chronicle does not linger on orcish inner life; it shows enough to make the factories of Isengard and the towers of Cirith Ungol feel populated and doomed.",
    ],
    related: ["saruman", "sauron", "isengard", "mordor"],
    tags: ["kindred", "shadow"],
  },
  {
    slug: "istari",
    category: "peoples",
    name: "The Istari",
    epithet: "The Wizards",
    era: "Third Age",
    summary:
      "Five Maiar sent in the shapes of aged Men to contest Sauron by stirring resistance, not by matching power with power.",
    body: [
      "The Istari are forbidden to dominate the peoples of Middle-earth. That rule is the whole test. Gandalf keeps it; Saruman breaks it; Radagast wanders into bird-speech; the Blue Wizards pass out of the western tale.",
      "A wizard’s staff is office as much as weapon. When Saruman’s is broken, the office has already been empty for years.",
    ],
    related: ["gandalf", "saruman"],
    tags: ["maiar", "order"],
  },
  {
    slug: "nazgul",
    category: "peoples",
    name: "The Nazgûl",
    epithet: "The Nine, the Ringwraiths",
    era: "Second Age to Third Age",
    summary:
      "Kings of Men who took rings from Sauron and faded into enslaved terror, the Dark Lord’s most trusted hunters.",
    body: [
      "The Nine are what the Ring promises Men: power first, then a life that is not life. They smell the One, fear water and fire in their own fashion, and unmake courage by being near it.",
      "Their chief is the Witch-king. When he falls, the others continue until the Ring itself is cut from the world. Then they go out like flames deprived of oil.",
    ],
    related: ["witch-king", "sauron", "one-ring", "weathertop"],
    tags: ["wraiths", "shadow"],
  },
  {
    slug: "one-ring",
    category: "peoples",
    name: "The One Ring",
    epithet: "Isildur’s Bane, the Precious",
    era: "Second Age to Third Age",
    summary:
      "Sauron’s master-ring, a tool of domination that contains much of his native power and unmakes him when it is unmade.",
    body: [
      "The Ring is a character by another name. It wants to be found, wants to be used, wants to go home. It lengthens life by stretching it thin. It offers each bearer a kingdom cut to that bearer’s hunger: a garden, a queen, a captaincy, a world of slaves.",
      "Destroying it is an anti-quest: not to win an object but to lose one on purpose. Middle-earth’s Third Age is the long interval between cutting it from a hand and putting it back into fire.",
    ],
    related: ["sauron", "frodo-baggins", "gollum", "destruction-of-the-ring"],
    tags: ["artifact", "ring"],
  },
  {
    slug: "erebor",
    category: "locations",
    name: "Erebor",
    epithet: "The Lonely Mountain",
    era: "Third Age",
    summary:
      "Dwarf-kingdom restored after the fall of Smaug, whose people send Gimli to Rivendell and later fight the Easterlings in the North.",
    body: [
      "Erebor is the mountain of Bilbo’s adventure, already a recovered kingdom by the War of the Ring. Its gold no longer sleeps under a dragon, but its isolation remains: a northern ally too far to march to Pelennor.",
      "Dale and Erebor wage their own war while Gondor burns. The chronicle of the Ring only glances north, enough to say the darkness was not a single battlefield.",
    ],
    related: ["gimli", "bilbo-baggins", "dwarves"],
    tags: ["dwarf-home"],
  },
  {
    slug: "mirkwood",
    category: "locations",
    name: "Mirkwood",
    epithet: "Greenwood the Great, darkened",
    era: "Third Age",
    summary:
      "A vast forest of the east, shadowed by Dol Guldur, home to Thranduil’s realm and to Legolas before the Quest.",
    body: [
      "Once Greenwood, the forest takes a new name when a Necromancer sits in Dol Guldur. Spiders, darkness, and a wary Elvenking define the tales that pass through it.",
      "In the War, the wood is assailed and later cleansed in name and in part. Legolas’s people remain of the trees even when the Shadow lifts.",
    ],
    related: ["legolas", "sauron", "elves"],
    tags: ["forest"],
  },
  {
    slug: "anduin",
    category: "locations",
    name: "The Anduin",
    epithet: "The Great River",
    era: "All Ages",
    summary:
      "The long river from the north down which the Fellowship travels, and in whose reeds Isildur once lost the Ring.",
    body: [
      "Anduin is a road and a border: Lórien on one bank, later Gondor and the east-march. The Argonath announce the old kingdom to anyone still willing to look up.",
      "The river hides Gollum as a log, bears the Fellowship’s boats, and remembers a disaster older than hobbits: a golden thing slipping from a cut hand into the dark.",
    ],
    related: ["breaking-of-the-fellowship", "one-ring", "gondor"],
    tags: ["river"],
  },
  {
    slug: "eomer",
    category: "characters",
    name: "Éomer",
    epithet: "Third Marshal, then King of the Mark",
    era: "Third Age",
    summary:
      "Sister-son of Théoden, an exile from the poisoned court who becomes Rohan’s war-leader and later its king.",
    body: [
      "Éomer meets the Three Hunters as a man already at odds with Gríma’s policy. He lends horses, breaks rules, and is imprisoned for it until the king wakes.",
      "On the Pelennor he sees a sister he thought dead and a king he loved fallen. He still finishes the battle. In the Fourth Age he is a king allied to Elessar, the Mark’s grief turned into a reign.",
    ],
    related: ["eowyn", "theoden", "rohan", "pelennor-fields"],
    tags: ["human", "rohan"],
  },
  {
    slug: "celeborn",
    category: "characters",
    name: "Celeborn",
    epithet: "Lord of Lothlórien",
    era: "First Age to Fourth Age",
    summary:
      "Galadriel’s husband, a Sindarin lord of the Golden Wood who remains in Middle-earth for a time after she sails.",
    body: [
      "Celeborn is counsel and courtesy in Lórien’s high flet. He arms the Fellowship with boats and warnings about the River and the wood. His marriage is a joining of Noldorin and Sindarin streams of Elven history.",
      "After the War he dwells for a while in East Lórien, a late guardian of trees, before taking the last roads West in his own hour.",
    ],
    related: ["galadriel", "lothlorien"],
    tags: ["elf", "sindar"],
  },
  {
    slug: "orthanc",
    category: "locations",
    name: "Orthanc",
    epithet: "The unbreakable tower",
    era: "Early Third Age to Fourth Age",
    summary:
      "A tower of four piers of black stone at the center of Isengard, proof against Ent-wrath, later given by Saruman’s fall back toward Gondor’s keeping.",
    body: [
      "Orthanc is Númenórean work: smooth, cold, indifferent to the industrial mess Saruman piles around it. From its roof he argues with the world; from its palantír he is argued with by Sauron.",
      "After the flood, the tower remains, a needle in a lake. Keys pass, in the end, to the King. Some fortresses outlast the villains who rented them.",
    ],
    related: ["isengard", "saruman", "gondor"],
    tags: ["tower"],
  },
];

export function getEntry(slug: string) {
  return entries.find((e) => e.slug === slug);
}

export function getByCategory(category: Category) {
  return entries.filter((e) => e.category === category).sort((a, b) => a.name.localeCompare(b.name));
}

export function searchEntries(query: string) {
  const q = query.trim().toLowerCase();
  if (!q) return [];
  return entries.filter((e) => {
    const hay = [e.name, e.epithet, e.summary, e.era, ...e.tags, ...e.body].join(" ").toLowerCase();
    return hay.includes(q);
  });
}

export function relatedEntries(entry: Entry) {
  return entry.related
    .map((slug) => getEntry(slug))
    .filter((e): e is Entry => Boolean(e));
}

export const timeline = [
  {
    year: "S.A. 1600",
    title: "The One Ring is forged",
    slug: "one-ring",
    text: "In the fires of Orodruin, Sauron completes the master-ring and the long war for the other Rings begins in earnest.",
  },
  {
    year: "S.A. 3441",
    title: "Isildur takes the Ring",
    slug: "last-alliance",
    text: "The Last Alliance throws Sauron down. The Ring is cut from his hand and is not destroyed.",
  },
  {
    year: "T.A. 2941",
    title: "Bilbo finds the Ring",
    slug: "bilbo-baggins",
    text: "Beneath the Misty Mountains, a hobbit wins a riddle-game and a burden he does not yet understand.",
  },
  {
    year: "T.A. 3018",
    title: "The Council of Elrond",
    slug: "council-of-elrond",
    text: "The Free Peoples choose to unmake the Ring. Nine walkers set out from Rivendell.",
  },
  {
    year: "T.A. 3019 · Feb",
    title: "The Fellowship breaks",
    slug: "breaking-of-the-fellowship",
    text: "Moria’s loss is followed by treachery and death at Parth Galen. The Quest splits.",
  },
  {
    year: "T.A. 3019 · Mar 3",
    title: "Helm’s Deep",
    slug: "battle-of-helms-deep",
    text: "Rohan holds the Hornburg. Isengard’s host is broken at dawn.",
  },
  {
    year: "T.A. 3019 · Mar 15",
    title: "Pelennor Fields",
    slug: "pelennor-fields",
    text: "Minas Tirith is relieved. The Witch-king falls. The black ships are the King’s.",
  },
  {
    year: "T.A. 3019 · Mar 25",
    title: "The Ring is unmade",
    slug: "destruction-of-the-ring",
    text: "At Mount Doom the Precious is destroyed. The Dark Tower falls.",
  },
  {
    year: "T.A. 3019 · May 1",
    title: "Elessar is crowned",
    slug: "crowning-of-elessar",
    text: "The king returns to Gondor. The Fourth Age is nearly begun.",
  },
  {
    year: "T.A. 3019 · Nov",
    title: "The Shire is scoured",
    slug: "scouring-of-the-shire",
    text: "The four travelers free their own country from Sharkey’s little tyranny.",
  },
  {
    year: "T.A. 3021",
    title: "The Ring-bearers sail",
    slug: "grey-havens",
    text: "From Mithlond the white ship takes Frodo, Bilbo, and the keepers of the Three into the West.",
  },
];
