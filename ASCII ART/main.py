l = int(input())
h = int(input())
t = input().upper()

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
for i in range(h):
    row = input()
    result = ''
    for c in t:
        try:
            start = alpha.index(c)*l
        except ValueError:
            start = alpha.index('?')*l
        result += row[start:start+l]

    print(result)