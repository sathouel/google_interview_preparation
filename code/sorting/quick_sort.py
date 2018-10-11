def sort(tab):
    start, end = 0, len(tab) - 1
    new_tab = tab.copy()
    sort_aux(new_tab, start, end)
    return new_tab

def sort_aux(tab, start, end):
    if start >= end:
        return 
    pivot_index = end
    new_pivot_index = partition(tab, start, end, pivot_index)
    sort_aux(tab, start, new_pivot_index - 1)
    sort_aux(tab, new_pivot_index + 1, end)
    
    
def partition_space(tab, start, end, pivot_index):
    lower, higher = [], []
    pivot = tab[pivot_index]
    for rel_index in range(end - start + 1):
        abs_index = start + rel_index
        val = tab[abs_index]
        if abs_index == pivot_index:
            continue
        elif val <= pivot:
            lower.append(val)
        else:
            higher.append(val)
    tab[start: end + 1] = lower + [pivot] + higher
    return start + len(lower)


def partition(tab, start, end, pivot_index):
    tab[pivot_index], tab[end] = tab[end], tab[pivot_index]
    pivot = tab[pivot_index]
    start_it, end_it = start, end - 1 
    while end_it != start_it:
        val = tab[start_it]
        if val <= pivot:
            start_it += 1
            continue
        else:
            tab[start_it], tab[end_it] = tab[end_it], tab[start_it]
            end_it -= 1
            continue
    last_val = tab[end_it]
    if last_val <= pivot:
        tab[end] = tab[end_it + 1]
        tab[end_it + 1] = pivot
        return end_it + 1
    else:
        tab[end] = tab[end_it]
        tab[end_it] = pivot
        return end_it



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
