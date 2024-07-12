ve = []
n = int(input())
for i in range(n):
    v, e = [int(j) for j in input().split()]
    ve.append((v, e))

_min = 10000000 
for i in range(n):
    for j in range(i+1, n):
        v1 = ve[i][0]
        e1 = ve[i][1]
        
        v2 = ve[j][0]
        e2 = ve[j][1]
        if _min > abs(v2-v1)+abs(e2-e1):
            _min = abs(v2-v1)+abs(e2-e1)

print(_min)
