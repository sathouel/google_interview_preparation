def find(arr):
    l = 0
    l_best = l
    best = arr[0]
    
    # step 1 : go to first non negative element
    for i in range(len(arr)):
        l = i
        l_best = l_best if best > arr[i] else l
        best = best if best > arr[i] else arr[i]
        if arr[i] > 0:
            break
    
    r, r_best = l, l_best
    curr = best
    
    while r < len(arr) - 1:
        
        if curr + arr[r+1] >= 0:
            curr += arr[r+1]
            r += 1
        elif curr + arr[r+1] < 0:
            r += 2
            l = r
            if l < len(arr):
                curr = arr[l]
        
        l_best = l_best if best > curr else l
        r_best = r_best if best > curr else r
        best = best if best > curr else curr
        
    return l_best, r_best, best
        
def find_final(arr):
    step1_arr = [-x for x in arr]
    start_max = find(arr)[2] < 0
    if start_max:
        step1_arr = arr
    
    # STEP 1
    step1_sol = find(step1_arr)
    tab1 = step1_arr[step1_sol[0]:step1_sol[1]+1]
    if not start_max:
        tab1 = [-x for x in tab1]
    
    # STEP 2
    step2_arr = [-x for x in step1_arr]  
    sol_left_arr, best_left = None, None
    left_arr = []
    if step1_sol[0] > 0:
        left_arr = step2_arr[:step1_sol[0]]
        sol_left_arr = find(left_arr)
        best_left = sol_left_arr[2]
        sol_left_arr = left_arr[sol_left_arr[0]:sol_left_arr[1]+1]
        
    sol_right_arr, best_right = None, None
    right_arr = []
    if step1_sol[1] < len(arr) - 1:
        right_arr = step2_arr[step1_sol[1]+1:]
        sol_right_arr = find(right_arr)
        best_right = sol_right_arr[2]
        sol_right_arr = right_arr[sol_right_arr[0]:sol_right_arr[1]+1]
        
    if sol_left_arr is None:
        if not start_max:
            return tab1, sol_right_arr
        else:
            sol_right_arr = [-x for x in sol_right_arr]
            return sol_right_arr, tab1
    elif sol_right_arr is None:
        if not start_max:
            return tab1, sol_left_arr
        else:
            sol_left_arr = [-x for x in sol_left_arr]
            return sol_left_arr, tab1
    else:
        best_arr = sol_left_arr if best_left > best_right else sol_right_arr
        if not start_max:
            return tab1, best_arr
        else:
            best_arr = [-x for x in best_arr]
            return best_arr, tab1


test_number = input()
test_number = int(test_number)

for _ in range(test_number):

    lst_len = input()

    lst = input()
    lst = list(lst)
    arr = []
    for j, i in enumerate(lst):
        if i.isdigit():
            if j > 0 and lst[j-1] == '-':
                arr.append(-int(i))
            else:
                arr.append(int(i))
    # print(arr)
    sol = find_final(arr)
    print(abs(sum(sol[0]) - sum(sol[1])))