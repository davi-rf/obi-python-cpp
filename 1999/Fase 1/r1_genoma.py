nCad1, nCad2 = [int(i) for i in input().split()]
if nCad1 < 1 or nCad2 < 1: exit()
cad1 = input()
cad2 = input()

invCad1 = []
for gen in cad1:
    if gen == 'A': invCad1.insert(0, 'T')
    elif gen == 'T': invCad1.insert(0, 'A')
    elif gen == 'C': invCad1.insert(0, 'G')
    elif gen == 'G': invCad1.insert(0, 'C')
invCad1 = ''.join(invCad1)

oc = 0
ocInv = 0
indexOc = []
indexOcInv = []
for i in range(nCad2 - nCad1 + 1):
    seq = cad2[i:i+nCad1]
    if seq == cad1:
        oc += 1
        indexOc.append(i + 1)
    if seq == invCad1:
        ocInv += 1
        indexOcInv.append(i + 1)

print(oc)
print(' '.join([str(x) for x in indexOc]) if oc else 0)
print(ocInv)
print(' '.join([str(x) for x in indexOcInv]) if ocInv else 0)