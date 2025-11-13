"""
This file creates a dict that stores the structure of the One Piece anime chronologically.

The order is structured like so:
    1. Main Saga (e.g. Sea of Survival: Super Rookies Saga)
        2. Sub Saga (e.g. East Blue Saga)
            3. Sub-Saga arcs and their episodes (e.g. Romance Dawn ep. 1-3)

structure = {
    str: {                     # Main Saga (key)
        str: [                 # Sub-Saga (key)
            {                  # Arc (dict in list)
                "name": str,
                "display": str,
                "start": int,
                "end": int or None
            },
            { ... },
            ...
        ],
        str: [ ... ],
        ...
    },
    str: { ... }
}

Source: https://onepiece.fandom.com/wiki/Episode_Guide
"""

op_structure = {
    "1. Sea of Survival - Super Rookies Saga [Pre-time-skip]":{
        "1. East Blue Saga":{
            [
                {"name": "1. Romance Dawn Arc", "display": "Romance Dawn", "start": 1, "end": 2},
                {"name": "2. Orange Town Arc", "display": "Orange Town", "start": 4, "end": 8},
                {"name": "3. Syrup Village Arc", "display": "Syrup Village Arc", "start": 9, "end": 18},
                {"name": "4. Baratie Arc", "display": "Baratie Arc", "start": 19, "end": 30},
                {"name": "5. Arlong Park Arc", "display": "Arlong Park Arc", "start": 31, "end":45},
                {"name": "6. Buggy Side Story Arc", "display": "Buggy Side Story Arc", "start": 46, "end": 47},
                {"name": "7. Logue Town Arc", "display": "Logue Town Arc", "start": 48, "end": 53},
                {"name": "8. Warship Island Arc", "display": "Warship Island Arc", "start": 54, "end": 61}

            ]
        },

        "2. Arabasta Saga":{
            [
                {"name": "1. Reverse Mountain Arc", "display": "Reverse Mountain Arc", "start": 62, "end": 63},
                {"name": "2. Whisky Peak Arc", "display": "Whisky Peak", "start": 64, "end": 67},
                {"name": "3. Koby and Helmeppo Arc", "display": "Koby and Helmeppo Arc", "start": 68, "end": 69},
                {"name": "4. Little Garden Arc", "display": "Little Garden Arc", "start": 70, "end": 77},
                {"name": "5. Drum Island Arc", "display": "Drum Island Arc", "start": 78, "end": 91},
                {"name": "6. Arabasta Arc", "display": "Arabasta Arc", "start": 92, "end": 130},
                {"name": "7. Post-Arabasta Arc", "display": "Post-Arabasta", "start": 131, "end": 135}
            ]
        },

        "3. Sky Island Saga":{
            [
                {"name": "1. Goat Island Arc", "display": "Goat Island Arc", "start": 136, "end": 138},
                {"name": "2. Ruluka Island Arc", "display": "Ruluka Island Arc", "start": 139, "end": 143},
                {"name": "3. Jaya Arc", "display": "Jaya Arc", "start": 144, "end": 152},
                {"name": "4. Skypiea Arc", "display": "Skypiea", "start": 153, "end": 195},
                {"name": "5. G-8 Arc", "display": "G-8 Arc", "start": 196, "end": 206}
            ]
        },

        "4. Water 7 Saga":{
            [
                {"name": "1. Long Ring Long Land Arc", "display": "Long Ring Long Land Arc", "start": 207, "end": 219},
                {"name": "2. Ocean's Dream Arc", "display": "Ocean's Dream Arc", "start": 220, "end": 224},
                {"name": "3. Foxy's Return Arc", "display": "Foxy's Return Arc", "start": 225, "end": 263},
                {"name": "4. Ennies Lobby Arc", "display": "Ennies Lobby Arc", "start": 264, "end": 312},
                {"name": "5. Post-Ennies Lobby Arc", "display": "Post Ennies Lobby Arc", "start": 313, "end": 325}
            ]
        },

        "5. Thriller Bark Saga":{
            [
                {"name": "1. Ice Hunter Arc", "display": "Ice Hunter Arc", "start": 326, "end": 336},
                {"name": "2. Thriller Bark Arc", "display": "Thriller Bark Arc", "start": 337, "end": 381},
                {"name": "3. Spa Island Arc", "display": "Spa Island Arc", "start": 382, "end": 384}
            ]
        },

        "6. Summit War Saga":{
            [
                {"name": "1. Sabaody Archipelago Arc", "display": "Sabaody Archipelago Arc", "start": 385, "end": 405},
                {"name": "2. Special Historical Arc [Filler]", "display": "Special Historical Arc [Filler]", "start": 406, "end": 407},
                {"name": "3. Amazon Lily Arc", "display": "Amazon Lily Arc", "start": 408, "end": 421},
                {"name": "4. Impel Down Arc [Part 1]", "display": "Impel Down Arc [Part 1]", "start": 422, "end": 425},
                {"name": "5. Little East Blue Arc", "display": "Little East Blue Arc", "start": 426, "end": 429},
                {"name": "6. Impel Down Arc [Part 2]", "display": "Impel Sown Arc [Part 2]", "start": 430, "end": 456},
                {"name": "7. Marineford Arc", "display": "Marineford Arc", "start": 457, "end": 489},
                {"name": "8. Post War Arc", "display": "Post War Arc", "start": 490, "end": 516}
            ]
        }
    },
    "2. The Final Sea - The New World Saga [Post-time-skip]":{
        "1. Fish-man Island Saga": {[
            {"name": "1. Return to Sabaody Arc", "display": "Return to Sabaody Arc", "start": 517, "end": 522},
            {"name": "2. Fish-man Island Arc", "display": "Fish-man Island Arc", "start": 523, "end": 574}
        ]},

        "2. Dressrosa Saga": {[
            {"name": "1. Z's Ambition Arc", "display": "Z's Ambition Arc", "start": 575, "end": 578},
            {"name": "2. Punk Hazard Arc", "display": "Punk Hazard Arc", "start": 579, "end": 625},
            {"name": "3. Caesar's Retrieval Arc", "display": "Caesar's Retrieval Arc", "start": 626, "end": 628},
            {"name": "4. Dressrosa Arc", "display": "Dressrosa Arc", "start": 629, "end": 746}
        ]},

        "3. Whole Cake Island Saga": {[
            {"name": "1. Silver Mine Arc", "display": "Silver Mine Arc", "start": 747, "end": 750},
            {"name": "2. Zou Arc", "display": "Zou Arc", "start": 751, "end": 779},
            {"name": "3. Marine Rookie Arc", "display": "Marine Rookie Arc", "start": 780, "end": 782},
            {"name": "4. Whole Cake Island Arc", "display": "Whole Cake Island Arc", "start": 783, "end": 877},
            {"name": "5. Levely Arc", "display": "Levely Arc", "start": 878, "end": 889}
        ]},

        "4. Wano Country Saga": {[
            {"name": "1. Wano Country Arc [Part 1]", "display": "Wano Country Arc [Part 1]", "start": 890, "end": 894},
            {"name": "2. Cidre Guild Arc", "display": "Cidre Guild Arc", "start": 895, "end": 896},
            {"name": "3. Wano Country Arc [Part 2]", "display": "Wano Country Arc [Part 2]", "start": 897, "end": 1028},
            {"name": "4. Uta's Past Arc", "display": "Uta's Past Arc", "start": 1029, "end": 1030},
            {"name": "5. Wano Country Arc [Part 3]", "display": "Wano Country Arc [Part 3]", "start": 1031, "end": 1085}
        ]},

        "5. The Final Saga": {[
            {"name": "1. Egghead Island Arc", "display": "Egghead Island Arc", "start": 1086, "end": None}
            #Elbaph Island Arc will be added here once Egghead Island is complete
        ]}
    }
}