#!/usr/bin/env python

import sys
import urllib.parse

character, show, quote = sys.argv[1:]

print()
print(f'> "{quote}"', end="\n\n")

character = " ".join(reversed(character.split(" ")))  # reverse character name
urlencoded_character = urllib.parse.quote(character.encode("utf-8"))
character_url = f"https://anidb.net/perl-bin/animedb.pl?adb.search={urlencoded_character}&show=characterlist&do.search=1&cleanurl=1"
urlencoded_show = urllib.parse.quote(show.encode("utf-8"))
show_url = f"https://anidb.net/perl-bin/animedb.pl?adb.search={urlencoded_show}&show=animelist&do.search=1&cleanurl=1"

print(f"&mdash; [**{character}**]({character_url}), [**{show}**]({show_url})")
