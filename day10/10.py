from sys import stdin
from functools import reduce
from operator import xor

f = stdin.read()

l = list(map(int, f.split(",")))

def tie(marks, lengths, rounds=1):

    N = len(marks)

    c = 0
    skip = 0

    for _ in range(rounds):

        for length in lengths:

            to = c + length - 1
            
            for i in range(length // 2):
                marks[(c+i)%N], marks[(to-i)%N] = marks[(to-i)%N], marks[(c+i)%N]

            c += length + skip
            c %= N
            skip += 1

    return marks

# Part One
m = list(range(256))
r = tie(m, l)
print(r[0] * r[1])

# Part Two
l = list(map(ord, f)) + [17, 31, 73, 47, 23]
m = list(range(256))

sparse = tie(m, l, rounds=64)

dense = map(str, map(hex, [reduce(xor, m[i*16:i*16+16]) for i in range(16)]))
dense = [x[2:] if len(x[2:]) == 2 else "0" + str(x[2:]) for x in dense]

print("".join(dense))


