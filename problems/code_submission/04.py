def nge(arr):
    ng = []
    sol = []
    for i in reversed(range(len(arr))):
        if i == len(arr) - 1:
            sol.append(-1)
            ng.append(arr[i])
            continue
        while ng and arr[i] >= ng[-1]:
            ng.pop()
        if ng:
            sol.append(ng[-1])
        else:
            sol.append(-1)
        ng.append(arr[i])
    return sol

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

    res = nge(arr)
    res.reverse()
    res = [str(x) for x in res]
    res = ' '.join(res)
    print(res)