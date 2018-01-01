def swap(tab, dim, i1, j1, i2, j2):
    idx1 = i1*dim + j1
    idx2 = i2*dim + j2
    tab[idx1], tab[idx2] = tab[idx2], tab[idx1]
    return

def rotate(tab, dim):
    # transpose step 
    sol = list(tab)
    for i in range(dim):
        for j in range(dim):
            if i >= j:
                continue
            swap(sol, dim, i, j, j, i)
    
    # reverse col
    for raw in range(dim):
        for c in range(int(dim/2)):
            swap(sol, dim, raw, c, raw, dim - c - 1)
    
    return sol


test_number = input()
test_number = int(test_number)

for _ in range(test_number):

	dim = input()
	dim = int(dim)

	tab = input()
	tab = tab.split()
	tab = [int(x) for x in tab]

	sol = rotate(tab, dim)
	sol = [str(x) for x in sol]

	print(' '.join(sol))

