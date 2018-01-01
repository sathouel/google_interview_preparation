def find(start, end):
    grps = [list() for _ in range(len(start))]
    for i, s, e in zip(range(len(start)), start, end):
        if i == len(start) - 1:
            break
            
        for j, s_tmp, e_tmp in zip(range(1, len(start[i:])),start[i+1:], end[i+1:]):
            if (s < s_tmp and e > s_tmp) or (s < e_tmp and e > e_tmp):
                grps[i].append(j + i)
                grps[j + i].append(i)
        
    max_len = len(grps[0])
    for grp in grps:
        max_len = len(grp) if len(grp) > max_len else max_len
        
    return max_len + 1

test_number = input()
test_number = int(test_number)

for _ in range(test_number):
    size_sum = input()

    start = input()
    start = start.split()
    start = [int(x) for x in start]

    end = input()
    end = end.split()
    end = [int(x) for x in end]
    
    print(find(start, end))