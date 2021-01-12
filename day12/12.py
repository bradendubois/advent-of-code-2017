from sys import stdin
from random import choice

l = stdin.read().split("\n")

programs = dict()

for line in l:

    left, right = line.split(" <-> ")
    left = int(left)
    right = [int(r) for r in right.split(", ")]

    programs[left] = right


def group_search(S, F):

    seen = set()

    queue = [S]
    count = 0

    while len(queue):

        c = queue.pop()

        if c in seen:
            continue

        count += 1
        seen.add(c)

        queue.extend(F[c])

    return seen


# Part One
print(len(group_search(0, programs)))

# Part Two
V = set(programs.keys())

groups = 0

while len(V):
    groups += 1
    V -= group_search(choice(list(V)), programs)

print(groups)
