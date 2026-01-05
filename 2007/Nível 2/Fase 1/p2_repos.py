n_pcs, n_net = map(int, input().split())
pcs = [list(map(int, input().split())) for _ in range(n_pcs)]

net = {}
for _ in range(n_net):
    p, v = [int(i) for i in input().split()]
    net[p] = max(net.get(p, 0), v)

resp = []
for p, v in pcs:
    if p in net and v < net[p]:
        resp.append([p, net[p]])

for p, v in sorted(resp): print(p, v)