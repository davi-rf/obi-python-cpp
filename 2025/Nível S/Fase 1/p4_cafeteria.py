min, max, cap, dose = [int(input()) for _ in range(4)]
print('S' if min + (cap - min)%dose <= max else 'N')