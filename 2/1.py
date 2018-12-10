from collections import Counter
threes,twos=0,0
with open('input.txt') as f:
    for line in f:
        c = set(Counter(line).values())
        if 3 in c:
            threes += 1
        if 2 in c:
            twos += 1
print(twos*threes)
     