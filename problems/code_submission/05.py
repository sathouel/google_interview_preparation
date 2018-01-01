def rev_wis(s):
    lw = s.split(".")
    lw.reverse()
    return '.'.join(lw)

test_number = input()
test_number = int(test_number)

for _ in range(test_number):
    s = input()
    print(rev_wis(s))