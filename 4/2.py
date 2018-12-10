import re, datetime as dt, collections as co, operator
lazy_guard, max_min, guards_dict, guard_state, time_start,curr_guard =-1, [-1,-1,-1], co.defaultdict(lambda: co.defaultdict(int)), 0, 0,-1
with open('input.txt') as f:
    data = sorted([[(r.group(1),r.group(2)) for r in  [re.match(r'\[(.*)\] (.*)',line)]] for line in f],key=lambda d: dt.datetime.strptime(d[0][0], "%Y-%m-%d %H:%M"))
    for ts in ((d[0].split(' '),d[1]) for sl in data for d in sl):
        new_guard_re = re.search(r'(#\d*) ',ts[1])
        guard,guard_state = (int(new_guard_re.group(1)[1:]),0) if new_guard_re else (-1,(1^guard_state))
        curr_guard = guard if guard != -1 else curr_guard
        if guard == -1 and guard_state == 1:
            time_start = int(ts[0][1].split(':')[1])
        elif guard == -1 and guard_state == 0:
            time_end = int(ts[0][1].split(':')[1])
            sleep_span = list(range(time_start,time_end))
            for t in sleep_span:
                guards_dict[curr_guard][t] += 1
                guards_dict[curr_guard]['st'] -= len(sleep_span)
                max_min_ind = max(guards_dict[curr_guard].items(), key=operator.itemgetter(1))[0]
                if lazy_guard == 0 or guards_dict[curr_guard]['st'] < guards_dict[lazy_guard]['st']: lazy_guard = curr_guard
                if guards_dict[curr_guard][max_min_ind]> max_min[2]: max_min = [curr_guard,max_min_ind,guards_dict[curr_guard][max_min_ind]]  
print(lazy_guard* max(guards_dict[lazy_guard].items(), key=operator.itemgetter(1))[0], max_min[0]*max_min[1])
       


            
        
        

    