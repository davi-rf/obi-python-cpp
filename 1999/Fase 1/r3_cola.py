entrada = input()
if entrada == '0': exit()
k, a, b, c, d = [float(i) for i in entrada.split()]

trem = round(a + b*k, 2)
caminhao = round(c + d*k, 2)

if abs(trem - caminhao) < 1 or trem < caminhao: 
    print('T')
else:
    print('C')