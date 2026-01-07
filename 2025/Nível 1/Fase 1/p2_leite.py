min, max, cap, cafe = [int(input()) for _ in range(4)]
print('S' if min <= cap - cafe <= max else 'N')