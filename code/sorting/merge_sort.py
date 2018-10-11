
def sort(tab):
    start, end = 0, len(tab) - 1
    return sort_aux(tab, start, end)

def merge(leftTab, rightTab):
    i, j = 0, 0
    res = []
    while i < len(leftTab) and j < len(rightTab):
        leftVal, rightVal = leftTab[i], rightTab[j]
        if leftVal <= rightVal:
            res.append(leftVal)
            i += 1
        else:
            res.append(rightVal)
            j += 1
    if i == len(leftTab):
        return res + rightTab[j:]
    return res + leftTab[i:]



def sort_aux(tab, start, end):
    if start == end:
        return [tab[start]]
    midIndex = int((end + start)/2) + 1
    left, right = sort_aux(tab, start, midIndex - 1), sort_aux(tab, midIndex, end)
    return merge(left, right)




if __name__ == '__main__':
    tabs = {
        'tab1': [8, 2, 6, 3, 1, 8, 5, 3],
        'tab2': [38, 27, 43, 3, 9, 82, 10]
    }
    sols = [(name, sorted(tab)) for name, tab in tabs.items()]
    results = {name: sort(tab) for name, tab in tabs.items()}

    for name, sol in sols:
        if results[name] == sol:
            print('{} SUCCESS'.format(name))
        else:
            print('{} FAIL'.format(name))
