def calculate(a, b, c):
    sol = int(1)
    for _ in range(b):
        sol *= (a % c)
        sol %= c
        
    return sol


test_number = input()
test_number = int(test_number)

for _ in range(test_number):

    start = input()
    start = start.split()
    start = [int(x) for x in start]

    
    print(calculate(start[0], start[1], start[2]))