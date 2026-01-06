n_cands, aprov = [int(i) for i in input().split()]
cands = [int(i) for i in input().split()]
print(sorted(cands)[-aprov])