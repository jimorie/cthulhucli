#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import html
import json
import re
import sys


TAG_PATTERN = re.compile("<.*?>")


def tryint(s, default=0):
    try:
        return int(s)
    except (ValueError, TypeError):
        if s == "X":
            return s
        return default


def trybool(s):
    if s in ("Yes", "yes", "Y", "y"):
        return True
    if s in ("No", "no", "N", "n"):
        return False
    return bool(s)


def decode(text):
    text = text.replace("&copy;", "(C)")
    text = html.unescape(text)
    text = text.replace("<BR>", "\n").replace("<br />", "\n")
    text = text.replace("\ufffc", "")
    text = text.strip()
    text = strip_markup(text)
    return text


def strip_markup(text):
    return TAG_PATTERN.sub("", text)


def decode_html(text):
    cur = None
    beg = 0
    while True:
        end = text.find("<", beg)
        if end >= 0:
            if cur:
                yield f"<{cur}>{text[beg:end]}</{cur}>"
            else:
                yield text[beg:end]
            beg = end
            end = text.index(">", beg) + 1
            tag = text[beg:end]
            if "italic" in tag:
                cur = "subtype"
            elif "bold" in tag:
                cur = "keyword"
            else:
                cur = None
            beg = end
        else:
            if beg < len(text):
                if cur:
                    yield f"<{cur}>{text[beg:]}</{cur}>"
                else:
                    yield text[beg:]
            break


def main(sourcefile, targetfile):
    with open(sourcefile, "r", encoding="utf-8") as cards_fd:
        cards = json.load(cards_fd)
        with open(targetfile, "w") as fd:
            for card in cards:
                if not card["name"]:
                    continue
                if not card["type"]:
                    continue
                subtypes = card["subtype"].strip()
                if subtypes and not subtypes.endswith("."):
                    subtypes += "."
                if card["type"] == "Story":
                    if card["faction"] == "Neutral":
                        card["faction"] = None
                    else:
                        print("Story with faction:", card)
                    card["cost"] = None
                    card["skill"] = None
                json.dump(
                    {
                        "name": decode(card["name"]),
                        "descriptor": decode(card["descriptor"]) or None,
                        "type": card["type"],
                        "faction": card["faction"],
                        "unique": trybool(card["unique"].strip()),
                        "subtypes": decode(subtypes),
                        "text": decode(card["text"]),
                        "cost": (
                            tryint(card["cost"])
                            if card["type"]
                            in {"Character", "Support", "Event", "Conspiracy"}
                            else None
                        ),
                        "skill": (
                            tryint(card["skill"])
                            if card["type"] == "Character"
                            else None
                        ),
                        "terror": (
                            tryint(card["terror"])
                            if card["type"] == "Character"
                            else None
                        ),
                        "combat": (
                            tryint(card["combat"])
                            if card["type"] == "Character"
                            else None
                        ),
                        "arcane": (
                            tryint(card["arcane"])
                            if card["type"] == "Character"
                            else None
                        ),
                        "investigation": (
                            tryint(card["investigation"])
                            if card["type"] == "Character"
                            else None
                        ),
                        "transient": "Transient" in card["attribute"],
                        "steadfast": (
                            [[card["steadfastfaction"], card["steadfastcount"]]]
                            if "Steadfast" in card["attribute"]
                            else None
                        ),
                        "era": "LCG",
                        "id": card["num"],
                        "set": decode(card["set"]),
                        "setname": decode(card["setname"]),
                        "setid": card["setid"],
                        "flavor": decode(card["flavor"]) or None,
                        "illustrator": decode(card["illustrator"]) or None,
                        "max": tryint(card["max"]),
                        "banned": trybool(card["banned"]),
                        "restricted": card["rabbr"] == "R",
                    },
                    fd,
                )
                fd.write("\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
