#!/usr/bin/env python

import sys
import urllib.parse

character, show, quote = sys.argv[1:]

bold = lambda s: f"**{s}**"
quoted = lambda s: f'"{s}"'

print()
print("> {}".format(quoted(quote)), end="\n\n")

print("&mdash;", end=" ")

character_query = " AND ".join(character.split(" "))
character_url = (
    "https://anidb.net/search/fulltext/?adb.search={}&do.search=1&entity.chartb=1".format(
        urllib.parse.quote(character_query.encode("utf-8"))
    )
)
print("[{}]({})".format(bold(character), character_url), end=", ")

show_query = " AND ".join(show.split(" "))
show_url = "https://anidb.net/search/fulltext/?adb.search={}&do.search=1&entity.animetb=1".format(
    urllib.parse.quote(show_query.encode("utf-8"))
)
print("[{}]({})".format(bold(show), show_url))
