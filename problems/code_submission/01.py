def subArr(arr, val):
    l, r = 0, 0
    summ = arr[0]
    while r < len(arr) and l < len(arr):
        if summ < val:
            r += 1
            if r >= len(arr):
                break
            summ += arr[r]
        elif summ > val:
            if l == r:
                r += 1
                if r >= len(arr):
                    break
                summ += arr[r]
            else :
                summ -= arr[l]
                l += 1
        else:
            return l, r
        
    return -1

test_number = input()
test_number = int(test_number)

for _ in range(test_number):
    size_sum = input()
    size_sum = size_sum.split(" ")
    size_sum = [int(x) for x in size_sum]
    val = size_sum[1]

    arr = input()
    arr = arr.split(" ")
    arr = [int(x) for x in arr]

    res = subArr(arr, val)

    if type(res) is tuple:
        print(res[0]+1, res[1]+1)
    else:
        print(res)
