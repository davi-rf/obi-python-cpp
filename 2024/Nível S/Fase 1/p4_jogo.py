lado, passos = [int(i) for i in input().split()]
matriz = [[int(i) for i in input()] for _ in range(lado)]

for _ in range(passos):
    nova = [[0]*lado for _ in range(lado)]

    for y in range(lado):
        for x in range(lado):
            viz_vivos = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0: continue
                    
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < lado and 0 <= nx < lado:
                        viz_vivos += matriz[ny][nx]

            if matriz[y][x] == 1 and viz_vivos in (2, 3): nova[y][x] = 1
            elif matriz[y][x] == 0 and viz_vivos == 3: nova[y][x] = 1
    
    matriz = nova

for linha in matriz:
    print(''.join([str(i) for i in linha]))