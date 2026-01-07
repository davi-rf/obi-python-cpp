qtd = int(input())
alturas = [int(a) for a in input().split()][::-1]

maior = alturas[0]
nao_ve = 0
for altura in alturas[1:]:
    if altura > maior: maior = altura
    else: nao_ve += 1

print(nao_ve)