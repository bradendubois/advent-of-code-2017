from sys import stdin, unraisablehook

l = map(lambda line: line.split(" if "), stdin.read().split("\n"))

registers = dict()

mod = {
    "inc": 1,
    "dec": -1
}

def get(register):
    if register not in registers:
        registers[register] = 0
    return registers[register]


largest_ever = 0

for left, right in l:

    src_reg, chg, modify = left.split(" ")
    tgt_reg, cond, cond_val = right.split(" ")

    modify, cond_val = int(modify), int(cond_val)

    if eval(" ".join([str(get(tgt_reg)), cond, str(cond_val)])):
        registers[src_reg] = get(src_reg) + mod[chg] * modify

    largest_ever = max(largest_ever, *registers.values())


# Part One
print(max(registers.values()))

# Part Two
print(largest_ever)
