s = set()
with open('input.txt') as f:
    for line in f:
        for i in range(len(line.rstrip())):
            l = line.rstrip()
            lstr = ''.join((l[:i] + '-' + l[i+1:]))
            if lstr in s:
                print(lstr.replace('-',''))
            else:
                s.add(lstr)