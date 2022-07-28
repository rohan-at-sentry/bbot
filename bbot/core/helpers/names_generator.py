import random

adjectives = [
    "acute",
    "adhesive",
    "adorable",
    "affectionate",
    "aggravated",
    "atrocious",
    "awkward",
    "bighuge",
    "black",
    "blazed",
    "bloodshot",
    "brilliant",
    "brown",
    "cheeky",
    "chewy",
    "childish",
    "cold",
    "corrupted",
    "crafty",
    "creamy",
    "crispy",
    "crumbly",
    "crunchy",
    "cuddly",
    "cunning",
    "cute",
    "dark",
    "dastardly",
    "deep",
    "demonic",
    "depraved",
    "derogatory",
    "despicable",
    "devilish",
    "devious",
    "diabolic",
    "diabolical",
    "difficult",
    "disturbed",
    "embarrassing",
    "esoteric",
    "ethereal",
    "euphoric",
    "evil",
    "exquisite",
    "extreme",
    "feathery",
    "ferocious",
    "fiendish",
    "fierce",
    "fleecy",
    "flirtatious",
    "frothy",
    "furry",
    "fuzzy",
    "genius",
    "gentle",
    "giddy",
    "gluey",
    "glutinous",
    "gooey",
    "goofy",
    "goopy",
    "great",
    "grievous",
    "gummy",
    "hard",
    "harmful",
    "heated",
    "hectic",
    "heightened",
    "heinous",
    "hellish",
    "immoral",
    "infernal",
    "ingenious",
    "inquisitive",
    "insidious",
    "insightful",
    "insolent",
    "intelligent",
    "intensified",
    "intensive",
    "inventive",
    "loveable",
    "malevolent",
    "malicious",
    "manic",
    "moist",
    "monstrous",
    "mushy",
    "naughty",
    "nefarious",
    "overwhelming",
    "pasty",
    "pernicious",
    "perturbed",
    "perverse",
    "pillowy",
    "pixilated",
    "playful",
    "plump",
    "profound",
    "psychic",
    "psychedelic" "puffy",
    "pure",
    "raging",
    "rambunctious",
    "roguish",
    "sadistic",
    "satanic",
    "savvy",
    "severe",
    "shaggy",
    "sinful",
    "sinister",
    "slippery",
    "sly",
    "sneaky",
    "soft",
    "sophisticated",
    "spiteful",
    "squishy",
    "steamy",
    "sticky",
    "stoned",
    "strenuous",
    "stuffed",
    "subtle",
    "sudden",
    "surreal",
    "sweet",
    "tense",
    "terrible",
    "terrific",
    "thick",
    "thoughtful",
    "tricky",
    "tufty",
    "ugly",
    "unabated",
    "unholy",
    "unmelted",
    "unworthy",
    "utmost",
    "vehement",
    "vicious",
    "vigorous",
    "vile",
    "violent",
    "viscous",
    "vivid",
    "wet",
    "whimsical",
    "white",
    "wicked",
    "wild",
    "wispy",
    "witty",
    "woolly",
]

names = [
    "aaron",
    "abigail",
    "adam",
    "alan",
    "albert",
    "alex",
    "alexander",
    "alexis",
    "alice",
    "allen",
    "allison",
    "alyssa",
    "amanda",
    "amber",
    "amy",
    "andrea",
    "andrew",
    "angela",
    "ann",
    "anna",
    "anne",
    "annie",
    "anthony",
    "antonio",
    "aragorn",
    "arthur",
    "arwen",
    "ashley",
    "audrey",
    "austin",
    "baggins",
    "barbara",
    "benjamin",
    "betty",
    "beverly",
    "bilbo",
    "billy",
    "bobby",
    "bombadil",
    "bonnie",
    "boromir",
    "bradley",
    "brandon",
    "brandybuck",
    "brenda",
    "brian",
    "brianna",
    "brittany",
    "bruce",
    "bryan",
    "caleb",
    "cameron",
    "carl",
    "carlos",
    "carol",
    "carolyn",
    "carrie",
    "catherine",
    "charles",
    "charlotte",
    "cheryl",
    "christian",
    "christina",
    "christine",
    "christopher",
    "cindy",
    "clara",
    "clarence",
    "cody",
    "connie",
    "courtney",
    "craig",
    "crystal",
    "curtis",
    "cynthia",
    "dale",
    "daniel",
    "danielle",
    "danny",
    "david",
    "dawn",
    "deborah",
    "debra",
    "deckard",
    "denethor",
    "denise",
    "dennis",
    "diana",
    "diane",
    "donald",
    "donna",
    "doris",
    "dorothy",
    "douglas",
    "dylan",
    "earl",
    "edith",
    "edna",
    "edward",
    "elaine",
    "eleanor",
    "elendil",
    "elijah",
    "elizabeth",
    "ella",
    "ellen",
    "elrond",
    "emily",
    "emma",
    "eomer",
    "eomund",
    "eothain",
    "eowyn",
    "eric",
    "erin",
    "ernest",
    "esther",
    "ethan",
    "ethel",
    "eugene",
    "eva",
    "evan",
    "evelyn",
    "faramir",
    "florence",
    "frances",
    "francis",
    "frank",
    "fred",
    "frederick",
    "frodo",
    "gabriel",
    "galadriel",
    "gandalf",
    "gary",
    "george",
    "gerald",
    "gimli",
    "gladys",
    "glenn",
    "glorfindel",
    "gloria",
    "goldberry",
    "gollum",
    "grace",
    "gregory",
    "hannah",
    "harold",
    "harry",
    "hazel",
    "heather",
    "helen",
    "henry",
    "howard",
    "irene",
    "isaac",
    "isabella",
    "isildur",
    "jack",
    "jacob",
    "jacqueline",
    "james",
    "jamie",
    "jane",
    "janet",
    "janice",
    "jasmine",
    "jason",
    "jean",
    "jeffrey",
    "jennifer",
    "jeremy",
    "jerry",
    "jesse",
    "jessica",
    "jimmy",
    "joan",
    "joe",
    "joel",
    "john",
    "johnny",
    "jonathan",
    "jordan",
    "jose",
    "joseph",
    "josephine",
    "josh",
    "joyce",
    "juan",
    "judith",
    "judy",
    "julia",
    "julie",
    "justin",
    "karen",
    "katherine",
    "kathleen",
    "kathryn",
    "kathy",
    "kayla",
    "keith",
    "kelly",
    "kenneth",
    "kevin",
    "kimberly",
    "kyle",
    "lantern",
    "larry",
    "laura",
    "lauren",
    "lawrence",
    "legolas",
    "leonard",
    "leslie",
    "lillian",
    "linda",
    "lisa",
    "logan",
    "lois",
    "lori",
    "louis",
    "louise",
    "luis",
    "luke",
    "madison",
    "margaret",
    "maria",
    "marie",
    "marilyn",
    "marjorie",
    "mark",
    "martha",
    "martin",
    "marvin",
    "mary",
    "mason",
    "matthew",
    "megan",
    "melissa",
    "melvin",
    "merry",
    "michael",
    "michelle",
    "mildred",
    "monica",
    "nancy",
    "natalie",
    "nathan",
    "nathaniel",
    "nazgul",
    "nicholas",
    "nicole",
    "noah",
    "norma",
    "norman",
    "olivia",
    "obama",
    "pamela",
    "patricia",
    "patrick",
    "paul",
    "paula",
    "peggy",
    "peter",
    "philip",
    "phillip",
    "phyllis",
    "pippin",
    "rachel",
    "radagast",
    "ralph",
    "randy",
    "raymond",
    "rebecca",
    "richard",
    "rita",
    "robert",
    "robin",
    "rodney",
    "roger",
    "ronald",
    "rose",
    "roy",
    "ruby",
    "russell",
    "ruth",
    "ryan",
    "samantha",
    "samuel",
    "samwise",
    "sandra",
    "sapper",
    "sara",
    "sarah",
    "saruman",
    "sauron",
    "scott",
    "sean",
    "shannon",
    "sharon",
    "shawn",
    "shelob",
    "shirley",
    "sophia",
    "stanley",
    "stephanie",
    "stephen",
    "steven",
    "susan",
    "tammy",
    "taylor",
    "teresa",
    "terry",
    "theoden",
    "theresa",
    "thomas",
    "tiffany",
    "timothy",
    "tina",
    "todd",
    "tony",
    "tracy",
    "travis",
    "treebeard",
    "tyler",
    "tyrell",
    "valerie",
    "vanessa",
    "victor",
    "victoria",
    "vincent",
    "virginia",
    "wallace",
    "walter",
    "wanda",
    "wayne",
    "wendy",
    "william",
    "willie",
    "wormtongue",
    "zachary",
]


def random_name():
    name = f"{random.choice(adjectives)}_{random.choice(names)}"
    if name == "white_lantern":
        name = "black_lantern"
    return name