n_div = int(input())
div = [int(x) for x in input().split()]

guardados = 0
for d in div: guardados += (d - 1)

print(guardados)