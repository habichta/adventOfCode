import re, collections as c
active, overlap_c= list(),c.defaultdict(lambda: 0)
def updt_overlap(sq,asq):
    y_i = set(range(sq[2],sq[2]+sq[4])).intersection(range(asq[2],asq[2]+asq[4]))
    x_i = set(range(sq[1],sq[1]+sq[3])).intersection(range(asq[1],asq[1]+asq[3]))
    if len(x_i) > 0 and len(y_i) > 0: overlap_c[sq[0]], overlap_c[asq[0]] = 1,1
def updt_active(active):
    removed_tmp,active_tmp=[],[]
    for s in active:
            target = active_tmp if (s[2]+s[4]) > sq[2]  else removed_tmp
            target.append(s)
    return active_tmp,removed_tmp
with open('input.txt') as f:
    data = sorted([[int(n) for n in re.split(' @ |#|x|,|: ' , l.strip()) if n.isdigit() ] for l in f],key=lambda e: (e[2]))
    for sq in data:
        active_tmp,removed_tmp = updt_active(active)
        for rem in removed_tmp:
            if overlap_c[rem[0]] == 0: print(rem[0])
        for asq in active_tmp: updt_overlap(sq,asq)
        active = (active_tmp+[sq])