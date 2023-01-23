#!/usr/bin/env python

import sys
import urllib.parse

character, show, quote = sys.argv[1:]

bold = lambda s: f"**{s}**"
quoted = lambda s: f'"{s}"'

print()
print("> {}".format(quoted(quote)), end="\n\n")

print("&mdash;", end=" ")

character_url = "https://myanimelist.net/character.php?q={}&cat=character".format(
    urllib.parse.quote(character.encode("utf-8"))
)
print("[{}]({})".format(bold(character), character_url), end=", ")

show_url = "https://myanimelist.net/search/all?q={}&cat=all".format(
    urllib.parse.quote(show.encode("utf-8"))
)
print("[{}]({})".format(bold(show), show_url))
