from functools import reduce
with open('input.txt') as f:
    sum =reduce((lambda x,y: int(x) + int(y)), f)
    print(sum)
   