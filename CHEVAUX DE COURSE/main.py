n = int(input())
ch = []
for i in range(n):
    pi = int(input())
    ch.append(pi)

ch.sort()
_min = 10000001
for i in range(1, len(ch)):
    if (ch[i] - ch[i-1]) < _min:
        _min = ch[i] - ch[i-1]

print(_min)