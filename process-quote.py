#!/usr/bin/env python

import sys
import urllib.parse

character, show, quote = sys.argv[1:]

quoted = lambda s: f'"{s}"'

print()
print(f"> {quoted(quote)}", end="\n\n")

print("&mdash;", end=" ")

urlencoded_character = urllib.parse.quote(quoted(character).encode("utf-8"))
character_url = f"https://anidb.net/search/fulltext/?adb.search={urlencoded_character}&do.search=1&entity.chartb=1"
print(f"[**{character}**]({character_url})", end=", ")

urlencoded_show = urllib.parse.quote(quoted(show).encode("utf-8"))
show_url = f"https://anidb.net/search/fulltext/?adb.search={urlencoded_show}&do.search=1&entity.animetb=1&"
print(f"[**{show}**]({show_url})")
