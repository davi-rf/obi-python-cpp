r, lim = [int(i) for i in input().split()]
cal = 0
for ref in range(r):
    p, g, c = [int(i) for i in input().split()]
    cal += p*4 + g*9 + c*4

print(lim - cal)