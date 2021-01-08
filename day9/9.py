from sys import stdin

l = stdin.read()

garbage = False

score = 0
depth = 1
garbage_characters = 0

i = 0
while i < len(l):

    c = l[i]

    if c == "!":
        i += 2
        continue

    elif garbage and c != ">":
        garbage_characters += 1

    elif c == ">":
        garbage = True
    
    elif c == ">":
        garbage = False
    
    elif c == "{":
        score += depth
        depth += 1
    
    elif c == "}":
        depth -= 1

    i += 1


# Part One
print(score)

# Part Two
print(garbage_characters)
