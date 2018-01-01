def find4(str1, str2):
    x = len(str1) + 1
    y = len(str2) + 1
    
    tab = [[None] * y for _ in range(x)]
    
    for i, l in enumerate(tab):
        for j in range(y):
            if i == 0 or j == 0:
                tab[i][j] = 0
                continue
            if str1[i - 1] == str2[j - 1]:
                tab[i][j] = tab[i-1][j-1] + 1
                continue
            tab[i][j] = max(tab[i][j-1], tab[i-1][j])
    return tab[x-1][y-1]

    
test_number = input()
test_number = int(test_number)

for _ in range(test_number):
    size_sum = input()
    # size_sum = size_sum.split(" ")
    # size_sum = [int(x) for x in size_sum]
    # val = size_sum[1]

    str1 = input()
    str2 = input()
    
    print(find4(str1, str2))