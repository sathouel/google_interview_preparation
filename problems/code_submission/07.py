def find1(arr):
    mins = []
    max_positions = {}
    for val in arr:
#         print("mins : ", mins)
#         print("max_positions : ", max_positions)
        if len(mins) == 0:
            mins.append(val)
            max_positions[val] = 0
            continue
        for i in reversed(range(len(mins))):
            if val > mins[i]:
                max_positions[val] = i + 1
                if i + 1 >= len(mins):
                    mins.append(val)
                else:
                    mins[i+1] = val if val < mins[i+1] else mins[i+1]
                break
            if i-1 < 0:
                mins[i] = val
    sol = -1
    for k in max_positions:
        sol = max_positions[k] if max_positions[k] > sol else sol
    
    return sol + 1
        

test_number = input()
test_number = int(test_number)

for _ in range(test_number):
    size_sum = input()
    # size_sum = size_sum.split(" ")
    # size_sum = [int(x) for x in size_sum]
    # val = size_sum[1]

    arr = input()
    arr = arr.split()
    arr = [int(x) for x in arr]

    res = find(arr)
    print(res)