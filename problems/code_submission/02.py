def findKey(arr, key):
    l, r = 0, len(arr)-1
    while l < r:
        if arr[l] + arr[r] > key:
            r -= 1
        elif arr[l] + arr[r] < key:
            l += 1
        else :
            return True
    return False

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
    arr.sort()

    res = subArr(arr, val)

    if findKey(arr, val):
        print("Yes")
    else:
        print("No")
