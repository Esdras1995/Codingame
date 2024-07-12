last = {}

a1 = int(input())
n = int(input())

for i in range(1, n):
    idx = last.get(a1, i)
    last[a1] = i
    a1 = i - idx

print(a1)