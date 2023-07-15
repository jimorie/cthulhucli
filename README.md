Cthulhu CLI
===========

A command line interface for browsing cards for [Call of Cthulhu LCG and CCG](https://www.fantasyflightgames.com/en/products/call-of-cthulhu-lcg/).

Why?
----

Because [CardGameDB](http://www.cardgamedb.com) does not list cards from the CCG era.

Cthulhu CLI also has the ability produce card count breakdowns based on a selected field, with the `--count` option.

Install
-------

Cthulhu CLI can be installed from [PyPI](https://pypi.python.org/pypi/cthulhucli) using pip:

    sudo pip install cthulhucli

Options
-------

Cthulhu CLI has the following options as given by the --help option:

    $ cthulhucli --help
    Usage: cthulhucli [OPTIONS] [SEARCH]...

      A command line interface for Call of Cthulhu LCG and CCG.

      The default search argument matches cards against their name, text or
      subtypes. See below for more options.

      Options marked with inclusive or exclusive can be repeated to further
      include or exclude cards, respectively.

      For help and bug reports visit the project on GitHub:
      https://github.com/jimorie/cthulhucli

    Options:
      --brief                         Show brief card data.
      --case                          Use case sensitive matching.
      --cost NUMBER COMPARISON        Find cards whose cost matches the expression
                                      (inclusive).
      --count TEXT                    Show card count breakdown for given field.
                                      Increase verbosity to also show individual
                                      cards. Possible fields are: arcane, combat,
                                      cost, faction, investigation, name,
                                      restricted, skill, terror, type, unique,
                                      era.
      --exact                         Use exact matching.
      -f, --faction TEXT              Find cards with given faction (inclusive).
                                      Possible factions are: Agency, Cthulhu,
                                      Hastur, Lodge, Miskatonic University,
                                      Neutral, Shub-Niggurath, Silver Twilight,
                                      Syndicate, The Agency, Yog-Sothoth.
      --faction-isnt TEXT             Find cards with other than given faction
                                      (exclusive).
      --group TEXT                    Sort resulting cards by the given field and
                                      print group headers. Possible fields are:
                                      arcane, combat, cost, faction,
                                      investigation, name, restricted, skill,
                                      terror, type, unique, era.
      --inclusive                     Treat multiple options of the same type as
                                      inclusive rather than exclusive. (Or-logic
                                      instead of and-logic.)
      --include-draft                 Include cards only legal in draft format.
      --name TEXT                     Find cards with matching name. (This is the
                                      default search.)
      --non-unique                    Find non-unique cards.
      -r, --regex                     Use regular expression matching.
      --set TEXT                      Find cards from matching expansion sets
                                      (inclusive). Implies --include-draft.
      --show TEXT                     Show only given fields in non-verbose mode.
                                      Possible fields are: arcane, combat, cost,
                                      faction, investigation, name, restricted,
                                      skill, terror, type, unique, era.
      --sort TEXT                     Sort resulting cards by the given field.
                                      Possible fields are: arcane, combat, cost,
                                      faction, investigation, name, skill, terror,
                                      type.
      --skill NUMBER COMPARISON       Find cards whose Skill matches the
                                      expression (inclusive).
      --terror NUMBER COMPARISON      Find cards whose Terror matches the
                                      expression (inclusive).
      --combat NUMBER COMPARISON      Find cards whose Combat matches the
                                      expression (inclusive).
      --arcane NUMBER COMPARISON      Find cards whose Arcane matches the
                                      expression (inclusive).
      --investigation NUMBER COMPARISON
                                      Find cards whose Investigation matches the
                                      expression (inclusive).
      --text TEXT                     Find cards with matching text (exclusive).
      --text-isnt TEXT                Find cards without matching text
                                      (exclusive).
      --subtype TEXT                  Find cards with matching subtype
                                      (exclusive).
      --subtype-isnt TEXT             Find cards without matching subtype
                                      (exclusive).
      --keyword TEXT                  Find cards with matching keyword
                                      (exclusive). Possible fields are: fast,
                                      steadfast, toughness, transient, willpower,
                                      heroic, villainous, invulnerability, loyal.
      --keyword-isnt TEXT             Find cards without matching keyword
                                      (exclusive). Possible fields are: fast,
                                      steadfast, toughness, transient, willpower,
                                      heroic, villainous, invulnerability, loyal.
      -t, --type TEXT                 Find cards with matching card type
                                      (inclusive). Possible types are: Character,
                                      Conspiracy, Event, Story, Support.
      --unique                        Find unique cards.
      -v, --verbose                   Show more card data.
      --era [All|CCG|LCG]             Specify which era of cards to search.
                                      [default: LCG]
      --version                       Show the cthulhucli version: 0.1.0.
      --help                          Show this message and exit.

Examples
--------

Find a card by its name:

    $ cthulhucli Carl
    Carl Stanford: Unique. Cthulhu. Character. 3 Cost. 3 Skill. (T)(A).
    Carl Stanford: Unique. Silver Twilight. Character. 3 Cost. 3 Skill. (C)(A)(I).

Use the -v flag to show more card data:

    $ cthulhucli Carl -v
    Carl Stanford
    Deathless Fanatic
    Sorcerer.
    Invulnerability.
    Action: Sacrifice a Cultist character or Mask card to have Carl Stanford gain (C)(C)(A)(A) until the end of the phase.
    Unique: Yes
    Faction: Cthulhu
    Type: Character
    Cost: 3
    Skill: 3
    Icons: (T)(A)

    Carl Stanford
    Sinister, not necessarily Evil
    Lodge. Sorcerer.
    The cost of non-[Silver Twilight] characters cannot be lowered.
    Action: Pay 1 to choose a Spell or Ritual card in your discard pile and add it to your hand. Limit once per turn.
    Unique: Yes
    Faction: Silver Twilight
    Type: Character
    Cost: 3
    Skill: 3
    Icons: (C)(A)(I)

    Total count: 2

Use it multiple times for even more card data:

    $ cthulhucli Carl -vv
    Carl Stanford
    Deathless Fanatic
    Sorcerer.
    Invulnerability.
    Action: Sacrifice a Cultist character or Mask card to have Carl Stanford gain (C)(C)(A)(A) until the end of the phase.
    Unique: Yes
    Faction: Cthulhu
    Type: Character
    Cost: 3
    Transient: No
    Steadfast: No
    Skill: 3
    Icons: (T)(A)
    Era: LCG
    Set: Secrets of Arkham
    Card #: 028
    Illustrator: Sylvain Vialla
    Restricted: No
    Banned: No

    Carl Stanford
    Sinister, not necessarily Evil
    Lodge. Sorcerer.
    The cost of non-[Silver Twilight] characters cannot be lowered.
    Action: Pay 1 to choose a Spell or Ritual card in your discard pile and add it to your hand. Limit once per turn.
    Unique: Yes
    Faction: Silver Twilight
    Type: Character
    Cost: 3
    Transient: No
    Steadfast: No
    Skill: 3
    Icons: (C)(A)(I)
    Era: LCG
    Set: Seekers of Knowledge
    Card #: 051
    Illustrator: Bryce Cook
    Restricted: No
    Banned: No

    Total count: 2

Use filtering options to limit the results.

    $ cthulhucli --subtype investigator --combat ">=2" --faction-isnt neutral --non-unique
    Peeler: The Agency. Character. 2 Cost. 1 Skill. (C)(C).
    Freelance Photographer: Syndicate. Character. 4 Cost. 2 Skill. (C)(C)(I).
    Safari Hunter: The Agency. Character. 3 Cost. 3 Skill. (C)(C)(C).
    Night-shift Security: The Agency. Character. 3 Cost. 3 Skill. (C)(C)(C).
    Keen-eyed Detective: The Agency. Character. 3 Cost. 3 Skill. (C)(C).
    Crooked Cop: The Agency. Character. 3 Cost. 2 Skill. (C)(C).

    Total count: 6

Use `--sort` to sort the results.

    $ cthulhucli --subtype investigator --combat ">=2" --faction-isnt neutral --non-unique --sort cost
    Peeler: The Agency. Character. 2 Cost. 1 Skill. (C)(C).
    Safari Hunter: The Agency. Character. 3 Cost. 3 Skill. (C)(C)(C).
    Night-shift Security: The Agency. Character. 3 Cost. 3 Skill. (C)(C)(C).
    Keen-eyed Detective: The Agency. Character. 3 Cost. 3 Skill. (C)(C).
    Crooked Cop: The Agency. Character. 3 Cost. 2 Skill. (C)(C).
    Freelance Photographer: Syndicate. Character. 4 Cost. 2 Skill. (C)(C)(I).

    Total count: 6

Use `--group` to visibly divide the results:

    $ cthulhucli --subtype investigator --combat ">=2" --faction-isnt neutral --non-unique --group faction --group cost
    [ Syndicate | 4 Cost ]

    Freelance Photographer: Syndicate. Character. 4 Cost. 2 Skill. (C)(C)(I).

    [ The Agency | 2 Cost ]

    Peeler: The Agency. Character. 2 Cost. 1 Skill. (C)(C).

    [ The Agency | 3 Cost ]

    Safari Hunter: The Agency. Character. 3 Cost. 3 Skill. (C)(C)(C).
    Night-shift Security: The Agency. Character. 3 Cost. 3 Skill. (C)(C)(C).
    Keen-eyed Detective: The Agency. Character. 3 Cost. 3 Skill. (C)(C).
    Crooked Cop: The Agency. Character. 3 Cost. 2 Skill. (C)(C).

    Total count: 6

Use `--count` to break down the results into statistics.

    $ cthulhucli -f misk --count keyword --count icons
    [ Keyword counts ]

    Willpower:       11
    Heroic:          8
    Loyal:           6
    Toughness:       5
    Fast:            2
    Invulnerability: 2
    Villainous:      1
    Resilient:       1

    [ Icons counts ]

    (A)(I):          23
    (I):             10
    (C)(A)(I):       7
    (A)(I)(I):       7
    No Icons:        6
    (I)(I):          6
    (A)(A)(I):       6
    (A):             5
    (A)(A):          5
    (C)(I)(I):       3
    (C)(I):          3
    (A)(A)(A):       2
    (C):             2
    (C)(C)(A):       2
    (A)(A)(I)(I):    2
    (C)(A):          2
    (C)(C)(I):       1
    (C)(C)(A)(I):    1
    (I)(I)(I):       1
    (C)(C):          1
    (C)(A)(A)(I):    1
    (A)(A)(I)(I)(I): 1

    Total count: 97

Use `--regex` for advanced search patterns.

    $ cthulhucli --text 'put into play .*? from your hand' --regex -v
    Rampaging Dark Young
    Servitor. Dark Young.
    Toughness +2.
    Response: After Rampaging Dark Young is placed in the discard pile from play, put into play a character with printed cost 3 or lower from your hand or discard pile.
    Unique: No
    Faction: Shub-Niggurath
    Type: Character
    Cost: 5
    Skill: 5
    Icons: (C)

    Shub-Niggurath
    Dark Mistress of the Woods
    Ancient One.
    Villainous. Invulnerability.
    Action: Pay 2 to put into play any number of Dark Young characters from your hand and discard pile.
    Unique: Yes
    Faction: Shub-Niggurath
    Type: Character
    Cost: 6
    Skill: 8
    Icons: (T)(T)(C)(C)(A)

    The Tablets of Nhing
    Lost Knowledge
    Artifact.
    Fated 3.
    Response: After a character you control is destroyed, exhaust The Tablets of Nhing to put into play a character from your hand whose cost is lower than the destroyed character. Then, place
    1 success token on The Tablets of Nhing.
    Unique: Yes
    Faction: Silver Twilight
    Type: Support
    Cost: 2

    Total count: 3

Use `--era` to search old CCG cards as well.

    $ cthulhucli --era ccg --count set
    [ Set counts ]

    Arkham Edition:           251
    Eldritch Edition:         251
    Unspeakable Tales:        145
    Forbidden Relics:         145
    Masks of Nyarlathotep:    145
    Forgotten Cities:         144
    Promos:                   23
    Dunwich Denizens:         20
    Conspiracies of Chaos:    20
    Spawn of Madness:         20
    Kingsport Dreams:         20
    Arkham Premium Edition:   10
    Eldritch Premium Edition: 10

    Total count: 1204

Credits
-------

* All card data is copyright by [Fantasy Flight Games](https://www.fantasyflightgames.com/).
* Cthulhu CLI is written by [Petter Nyström](mailto:jimorie@gmail.com).
