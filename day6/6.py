from sys import stdin

blocks = [int(x) for x in stdin.read().split("\t")]

seen = set()
last = dict()

while (rep := str(blocks)) not in seen:

    last[rep] = len(seen)

    seen.add(rep)

    i, largest = 0, 0
    for idx, value in enumerate(blocks):
        if value > largest:
            i = idx
            largest = value

    blocks[i] = 0
    i += 1
    i %= len(blocks)
    
    while largest:
    
        blocks[i] += 1

        largest -= 1
        i += 1
        i %= len(blocks)


# Part One
print(len(seen))

# Part Two
print(len(seen) - last[rep])
