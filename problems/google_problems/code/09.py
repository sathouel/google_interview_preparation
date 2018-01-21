def add_nei(graph, grid, i, j):
    x, y = len(grid), len(grid[0])
    if j != 0 and grid[i][j-1] == 'X':
        graph[(i, j)].append((i, j-1))
    
    if j != y-1 and grid[i][j+1] == 'X':
        graph[(i, j)].append((i, j+1))
        
    if i != 0 and grid[i-1][j] == 'X':
        graph[(i, j)].append((i-1, j))
        
    if i != x-1 and grid[i+1][j] == 'X':
        graph[(i, j)].append((i+1, j))


def BFS(graph, checker, start):
    checker[start] = 0
    queue = []
    for nei in graph[start]:
        queue.append(nei)
        checker[nei] = checker[start] + 1
        
    while len(queue) != 0:
        new_node = queue.pop(0)
        for nei in graph[new_node]:
            if checker[nei] is not None:
                continue
            checker[nei] = checker[new_node] + 1
            queue.append(nei)

def find(grid):
    # INIT
    x, y = len(grid), len(grid[0])
    graph = {}
    checker = {}
	for i in range(x):
		for j in range(y):
			if grid[i][j] == 'X':
				graph[(i, j)] = list()
				checker[(i, j)] = None
				add_nei(graph, grid, i, j)

    # find sol
    
    counter = 0
    for k in graph:
        if checker[k] is None:
            BFS(graph, checker, k)
            counter += 1
    return counter

test_number = input()
test_number = int(test_number)

for _ in range(test_number):
    sizes = input()

    arr = input()
    arr = arr.split(' ')
    arr = [list(x) for x in arr]
    
    print(find(arr))