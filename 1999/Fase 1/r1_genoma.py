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

ocCad1 = 0
ocInvCad1 = 0
indexOcCad1 = []
indexOcInvCad1 = []
for i in range(nCad2 - nCad1 + 1):
    seq = cad2[i:i+nCad1]
    if seq == cad1:
        ocCad1 += 1
        indexOcCad1.append(i + 1)
    if seq == invCad1:
        ocInvCad1 += 1
        indexOcInvCad1.append(i + 1)

print(ocCad1)
if ocCad1 == 0: print('N')
else: print(' '.join([str(x) for x in indexOcCad1]))
print(ocInvCad1)
if ocInvCad1 == 0: print('N')
else: print(' '.join([str(x) for x in indexOcInvCad1]))