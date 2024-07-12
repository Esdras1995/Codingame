n = int(input())  # the number of temperatures to analyse
temp = 5526
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if abs(t) < abs(temp):
        temp = t
    elif abs(t) == abs(temp):
        temp = max(t, temp)

print(temp if n else 0)
