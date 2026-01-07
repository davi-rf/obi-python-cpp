qtd = int(input())
brinq = [int(i) for i in input().split()]

maior = max(brinq)
grafico = ['0'*(maior-b) + '1'*b for b in brinq]

for linha in zip(*grafico): print(*linha)