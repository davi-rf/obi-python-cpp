p = input().split()
gols_p = p[1:]
n_p = p[0]

c = input().split()
gols_c = c[1:]
n_c = c[0]

mins = sorted(gols_p + gols_c)

placar = [0, 0]
print(0, 0)
for m in mins:
    if m in gols_p: placar[0] += 1
    else: placar[1] += 1
    print(*map(str, placar))