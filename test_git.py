import os
import sys

def search_space(s):
    if s.find(" "):
        return True

def add_text(s):
    return s + "add text"

s = "Test git"

print(s)

print(search_space(s))
print(add_text(s))