obj = int(input())
k = int(input())

dia = 0
bac = 1
while bac*k <= obj:
    bac *= k
    dia += 1

print(dia)