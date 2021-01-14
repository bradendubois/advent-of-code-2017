from sys import stdin
from operator import add

cubes = {
    "n": (1, -1, 0),
    "ne": (1, 0, -1),
    "se": (0, 1, -1),
    "s": (-1, 1, 0),
    "sw": (-1, 0, 1),
    "nw": (0, -1, 1)
}

def distance(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))

l = stdin.read().split(",")

start = (0, 0, 0)
c = start

furthest_away = 0

for direction in l:
    c = tuple(map(add, c, cubes[direction]))
    furthest_away = max(furthest_away, distance(start, c))

# Part One
print(distance(start, c))

# Part Two
print(furthest_away)
