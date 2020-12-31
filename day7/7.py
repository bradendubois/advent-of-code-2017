from sys import stdin, unraisablehook

l = map(lambda line: line.split(" "), stdin.read().split("\n"))

V = set()
E = set()

scores = dict()

for line in l:
    
    name, value = line[:2]
    value = int(value[1:-1])

    scores[name] = value

    V.add(name)

    if "->" in line:
        children = list(map(lambda x: x.strip(","), line[3:]))
        E.update((name, child) for child in children)


# Part One
root = lambda v: len([e for e in E if e[1] == v]) == 0

print(x := next(filter(root, V)))

# Part Two
sum_scores = dict()

children = lambda v: [e[1] for e in E if e[0] == v]

def sum_score(v):
    if v in sum_scores:
        return sum_scores[v]
    
    score = scores[v]

    for c in children(v):
        score += sum_score(c)
    
    sum_scores[v] = score
    return score


queue = [v for v in V if len(children(v)) == 0]
top_V = []

while len(top_V) < len(V):

    cur = queue.pop(0)
    if cur not in top_V:
        top_V.append(cur)
        queue.extend([v for v in V if (v, cur) in E])


for v in top_V:

    C = children(v)

    s = [sum_score(c) for c in C]

    if len(set(s)) == 2:

        unbalanced = next(filter(lambda x: s.count(x) == 1, s))
        others = next(filter(lambda x: s.count(x) > 1, s))
        print(scores[C[s.index(unbalanced)]] + others - unbalanced)
        break
