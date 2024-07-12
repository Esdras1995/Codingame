m = ''
for c in input():
    m += '{0:07b}'.format(ord(c))
n = ''
p = ''
for i, b in enumerate(m):
    j = 0
    if b == '1' and not p == '1':
        n += ' 0 ' + m[i]
        j = 1
    if b == '0' and not p == '0':
        n += ' 00 ' + m[i]
        j = 1
    if not j:
        n += m[i]
    p = m[i]
print(n[1::].replace('1', '0'))