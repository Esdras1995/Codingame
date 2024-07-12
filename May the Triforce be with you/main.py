n = int(input())

a = ''
c = 1
for i in range(0, 4*n):
    if i%2 == 1:
        if i >= 2*n+1:
            a += c*'*'+(i-c*2)*" "+c*'*'+'\n'
            c += 2
        else:
            a += i*"*"+'\n'
            if i == 1:
                a = '.'+a[1:]
    if i%2 == 0:
        a += int((4*n-1-i)/2) * ' '
        

print(a[:-1])