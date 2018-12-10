from itertools import cycle
seen = set()
sum = 0
with open('input') as f:
    for line in cycle(f):
        sum += int(line)
        if sum in seen:
            print(sum)
            break
        else:
            seen.add(sum)

        




