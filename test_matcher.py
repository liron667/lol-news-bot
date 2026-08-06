"""Minimal check for the relevance filter. Run: python test_matcher.py"""
from bot import matches

KW = ["League of Legends", "LEC", "LCK", "LPL", "LCS", "Worlds"]
EX = []

assert matches("G2 win the LEC spring final", KW, EX)
assert matches("League of Legends patch 16.3 notes", KW, EX)
assert not matches("New Valorant agent revealed", KW, EX)   # different game, no keyword
print("ok")
