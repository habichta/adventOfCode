import collections as co, operator
from string import ascii_lowercase
def count_polymer(data,ign=''):
    stack = []
    for c in data:
        if c != ign.lower() and c != ign.upper():
            stack.append(c)
            if len(stack) > 1:
                x,y = stack[-1], stack[-2]
                while len(stack)> 1 and x != y and (x == y.upper() or x == y.lower()):
                    del stack[-2:]
                    if len(stack) > 1:
                        x,y  = stack[-1],stack[-2]
    return(len(stack))

with open('input.txt') as f:
    data, counter  = f.readlines()[0].rstrip(),co.defaultdict(lambda:0)
    print(count_polymer(data))
    print(min([count_polymer(data,c) for c in ascii_lowercase ]))
   
  