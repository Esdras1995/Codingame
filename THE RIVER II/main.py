r_1 = int(input())
is_r = 'NO'
for v in range(r_1, 1, -1):
    if sum([int(c) for c in str(v)])+v == r_1:
        is_r = 'YES'
        break

print(is_r)
