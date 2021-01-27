from sys import stdin
from string import ascii_lowercase

l = stdin.read().split(",")


def dance(prog):

    p = prog.copy()

    for command in l:

        move, data = command[0], command[1:]

        if move == "s":
            p = p[-int(data):] + p[:-int(data)]

        elif move == "x":
            s, t = [int(x) for x in data.split("/")]
            #print(s, t)
            p[s], p[t] = p[t], p[s]

        else:
            A, B = data.split("/")
            A_ind, B_ind = p.index(A), p.index(B)
            p[A_ind], p[B_ind] = p[B_ind], p[A_ind]

    return p


programs = list(ascii_lowercase[:ascii_lowercase.index("p")+1])

# Part One
print("".join(dance(programs)))

# Part Two
seen = ["".join(programs)]

i = 0
while True:
    i += 1
    programs = dance(programs)
    r = "".join(programs)
    if r == seen[0]:
        break
    seen.append(r)

offset = 1000000000 - ((1000000000 // i) * i)
print(seen[offset])
