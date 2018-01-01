def to_base_2(number):
    sol = []
    curr_number = int(number)
    while curr_number > 1:
#         sol = [curr_number % 2] + sol
        sol.append(curr_number % 2)
        curr_number = int(curr_number / 2)
    sol.append(curr_number % 2)
    return sol

def find(n1, n2):
    n1_2 = to_base_2(n1)
    n2_2 = to_base_2(n2)

#     n1_2.reverse()
#     n2_2.reverse()
    
    summ = 0
    
    longuest = n1_2 if len(n1_2) > len(n2_2) else n2_2
    shortest = n1_2 if len(n1_2) <= len(n2_2) else n2_2
    for i in range(len(shortest)):
        summ += 1 if shortest[i] != longuest[i] else 0
        
    idx = len(shortest)
    for j in range(len(longuest) - len(shortest)):
        summ += longuest[idx + j]
    
    return summ


def find_sum(arr):
    summ = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i):
            summ += 2 * find(arr[i], arr[i+j])
            
    return summ


test_number = input()
test_number = int(test_number)

for _ in range(test_number):
    size_sum = input()

    start = input()
    start = start.split()
    start = [int(x) for x in start]

    
    print(find_sum(start))




