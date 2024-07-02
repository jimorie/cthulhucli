#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json
import re
import sys


FACTIONS = {
    "_": "The Agency",
    "{": "Miskatonic University",
    "}": "Syndicate",
    "[": "Cthulhu",
    "]": "Hastur",
    "<": "Yog-Sothoth",
    ">": "Shub-Niggurath",
    "8": "Neutral",
    "---": None,
}

ICONS = {
    "@": "(T)",
    "#": "(C)",
    "$": "(A)",
    "%": "(I)",
}

SETS = {
    "AE": "Arkham Edition",
    "UT": "Unspeakable Tales",
    "FR": "Forbidden Relics",
    "AP": "Arkham Premium Edition",
    "EE": "Eldritch Edition",
    "MN": "Masks of Nyarlathotep",
    "FC": "Forgotten Cities",
    "EP": "Eldritch Premium Edition",
    "SM1": "Spawn of Madness",
    "KD2": "Kingsport Dreams",
    "CC3": "Conspiracies of Chaos",
    "DD4": "Dunwich Denizens",
    "PR": "Promos",
}

BOOSTER_PAT = re.compile(r"(\n|^)((?:\([TCIA]\))+)(\n|$)")


def tryint(s, default=None):
    try:
        return int(s)
    except ValueError:
        if s == "X":
            return s
        return default


def decode(text):
    text = text.replace("<br>", "\n")
    for a, b in ICONS.items():
        text = text.replace(a, b)
    for a, b in FACTIONS.items():
        text = text.replace(a, f"TMP1{b}TMP2")
    text = text.replace("TMP1", "[")
    text = text.replace("TMP2", "]")
    text = fix_boosters(text)
    return text


def fix_boosters(text):
    def replace(m):
        return (
            m.group(1) + m.group(2).replace("(", "((").replace(")", "))") + m.group(3)
        )

    return BOOSTER_PAT.sub(replace, text)


def main(sourcefile, targetfile):
    with open(sourcefile, "r", encoding="utf-8") as fd:
        reader = csv.DictReader(fd, dialect="excel-tab")
        with open(targetfile, "w") as out:
            for row in reader:
                if not row["TITLE"]:
                    continue
                if not row["TYPE"]:
                    continue
                if "<br>" in row["TITLE"]:
                    name, descriptor = row["TITLE"].split("<br>", 1)
                    descriptor = descriptor.strip()
                elif ', "' in row["TITLE"]:
                    name, descriptor = row["TITLE"].split(",", 1)
                    descriptor = descriptor.strip()
                else:
                    name, descriptor = row["TITLE"], None
                name = name.strip()
                if name.startswith("\uf020") or name.startswith("\uf076"):
                    banned = True
                    name = name.strip("\uf020\uf076").strip()
                else:
                    banned = False
                steadfast = []
                for code, faction in FACTIONS.items():
                    if name.startswith(code):
                        tmp = name.strip(code)
                        steadfast.append([faction, len(name) - len(tmp)])
                        name = tmp.strip()
                steadfast = steadfast or None
                unique = name.startswith("*")
                name = name.strip("*").strip()
                faction = FACTIONS[row["F"].strip()]
                icons = "".join(row[i] for i in "ICONS" if row[i])
                json.dump(
                    {
                        "name": name,
                        "descriptor": descriptor or None,
                        "type": row["TYPE"],
                        "faction": faction,
                        "unique": unique,
                        "subtypes": row["SUBTYPE"].replace("<br>", " ").strip(),
                        "text": decode(row["TEXTBOX"]),
                        "cost": tryint(row["COST"]),
                        "skill": tryint(row["SK"]),
                        "terror": icons.count("@"),
                        "combat": icons.count("#"),
                        "arcane": icons.count("$"),
                        "investigation": icons.count("%"),
                        "transient": (
                            "TRANSIENT" in row["OTHER"] if row["OTHER"] else False
                        ),
                        "steadfast": steadfast,
                        "era": "CCG",
                        "id": None,
                        "set": row["AP"].strip(),
                        "setname": SETS[row["AP"].strip()],
                        "setid": None,
                        "flavor": None,
                        "illustrator": None,
                        "max": 4,
                        "banned": banned,
                        "restricted": False,
                    },
                    out,
                )
                out.write("\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
