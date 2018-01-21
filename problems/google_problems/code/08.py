def find(a, b):
    if a == b:
        return 1
    
    if a > b:
        return 1 + find(a-b, b)
    else:
        return 1 + find(a, b-a)


test_number = input()
test_number = int(test_number)

for _ in range(test_number):

    arr = input()
    arr = arr.split()
    arr = [int(x) for x in arr]
    
    print(find(arr[0], arr[1]))

