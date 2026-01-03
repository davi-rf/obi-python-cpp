lin, col = [int(i) for i in input().split()]
if lin < 1 or col < 1: exit()
imagem = [[int(i) for i in input().split()] for _ in range(lin)]

contrucoes = 0
mapeadas = []

for y in range(lin):
    for x in range(col):
        if imagem[y][x] >= 1 and (y, x) not in mapeadas:
            contrucoes += 1
            fila = [(y, x)]
            while fila:
                cy, cx = fila.pop(0)
                if (cy, cx) in mapeadas: continue
                
                mapeadas.append((cy, cx))
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        ny, nx = cy + dy, cx + dx

                        if 0 <= ny < lin and 0 <= nx < col and imagem[ny][nx] >= 1 and (ny, nx) not in mapeadas:
                            fila.append((ny, nx))
print(contrucoes)