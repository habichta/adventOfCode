import collections as co
from heapq import heappush, heappop
class Step():
    def __init__(self):
        self.name=''
        self.depends_on = set()
        self.followed_by = set()


done = set()
cache = []
order = []
steps = co.defaultdict(lambda : Step())

def go(seen_i):
    if len(seen_i) > 0:
        next = heappop(seen_i)
        print(next)
        if all([i in done for i in steps[next].depends_on]):
            print(next)
            if next not in done:order.append(next)
            done.add(next)
            for follow_i in steps[next].followed_by: heappush(seen_i, follow_i)
            return seen_i
        else:
            seen_after = go(seen_i)
            heappush(seen_after,next)
            return seen_after
    else:
        return seen_i


with open('input.txt') as f:
    for line in f:
        l = line.rstrip().split(' ')
        steps[l[7]].name, steps[l[1]].name = l[7],l[1]
        steps[l[7]].depends_on.add(l[1])
        steps[l[1]].followed_by.add(l[7])

    start = [(name,obj) for name,obj in steps.items() if len(obj.depends_on) == 0]

    order.append(start[0][0])
    done.add(start[0][0])
    seen = []
    for follow in start[0][1].followed_by: heappush(seen,follow)
    while(len(seen) > 0):
        seen = go(seen)


    print(''.join(order))







    #while(len[seen] > 0):







