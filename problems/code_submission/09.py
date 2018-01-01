def find(arr):
    j_tab = [None] * len(arr)
    
    for i in reversed(range(len(arr))):
        if arr[i] == 0 or i == len(arr) - 1:
            j_tab[i] = 0
            continue
        if arr[i] >= len(arr) - i - 1:
            j_tab[i] = 1
            continue
        
        minn = j_tab[i + 1]
        checked = False
        for j in range(1, arr[i] + 1):
            checked = True
            minn = j_tab[i + j] if j_tab[i + j] < minn and j_tab[i + j] > 0 else minn
            
        j_tab[i] = minn + 1 if checked and minn != 0 else 0
    return j_tab[0] if j_tab[0] > 0 else -1 

    
test_number = input()
test_number = int(test_number)

for _ in range(test_number):
    size_sum = input()

    arr = input()
    arr = arr.split()
    arr = [int(x) for x in arr]
    
    print(find(arr))