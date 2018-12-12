import collections as co
from heapq import heappush
class Step():
    def __init__(self):
        self.name=''
        self.depends_on = list()
        self.followed_by = list()

steps = co.defaultdict(lambda : Step())
seen = list()

def dfs_rec(start,path):
    path = path + [start]
    for follow in steps[start].followed_by: seen.append(follow)
    for edge in sorted(seen):
        if edge not in path and all([x in path for x in steps[edge].depends_on]):
            seen.pop(0)
            path = dfs_rec(edge,path)
    return path

with open('input.txt') as f:
    for line in f:
        l = line.rstrip().split(' ')
        steps[l[7]].name, steps[l[1]].name = l[7],l[1]
        heappush(steps[l[7]].depends_on,l[1])
        heappush(steps[l[1]].followed_by,l[7])
    starts = [(name,obj) for name,obj in steps.items() if len(obj.depends_on) == 0]
    for l in starts:
        heappush(steps[l[0]].depends_on, '0')
        heappush(steps['0'].followed_by, l[0])
    print(''.join(dfs_rec('0',[])))





