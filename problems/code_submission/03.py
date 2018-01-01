def sortt(arr):
    zeros = []
    ones = []
    twos = []
    for val in arr:
        if val == 0:
            zeros.append(val)
        elif val == 1:
            ones.append(val)
        else :
            twos.append(val)
    return zeros + ones + twos


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

    res = sortt(arr)
    res = [str(x) for x in res]
    res = ' '.join(res)
    print(res)