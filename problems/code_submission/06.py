def find(arr):
    l = 0
    r = 0
    max_sum = curr_sum = arr[0]
    while l < len(arr) and r < len(arr):
        max_sum = curr_sum if curr_sum > max_sum else max_sum
        
        if curr_sum >= 0:
            r += 1
            curr_sum += arr[r] if r < len(arr) else 0
            continue
        else:
            
            if l == r :
                l += 1
                r += 1
                curr_sum = arr[r] if r < len(arr) else 0
                continue 
                
            while curr_sum < 0 and l < r:
                curr_sum -= arr[l]
                l += 1
    
    return max_sum 


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