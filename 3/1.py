import re
def calc_overlap(sq,asq): #(O(1))
    y_i = set(range(sq[2],sq[2]+sq[4])).intersection(range(asq[2],asq[2]+asq[4]))
    x_i = set(range(sq[1],sq[1]+sq[3])).intersection(range(asq[1],asq[1]+asq[3]))
    return [(x,y) for x in x_i for y in y_i]   
overlap, active= set(),list()
with open('input.txt') as f:
    data = sorted([[int(n) for n in re.split(' @ |#|x|,|: ' , l.strip()) if n.isdigit() ] for l in f],key=lambda e: (e[2]))
    for sq in data: #naive: (O(n^2) worst case, O(n log(n)) with Segment trees (Scan Line Method)
        active_tmp = [s for s in active if (s[2]+s[4]) > sq[2]]
        for asq in active_tmp:
            overlap.update(calc_overlap(sq,asq))
        active = (active_tmp+[sq])
print(len(overlap))