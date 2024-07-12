occurences = {}
rules = {
    '1': 30.1,
    '2': 17.6,
    '3': 12.5,
    '4': 9.7,
    '5': 7.9,
    '6': 6.7,
    '7': 5.8,
    '8': 5.1,
    '9': 4.6
}
fraud = 'false'

n = int(input())
for i in range(n):
    transaction = input()
    j = 0
    while(not transaction[j].isnumeric() or transaction[j] == "0"):
        j = j + 1
    
    num = transaction[j]
    if num not in occurences:
        occurences[num] = 0
    
    occurences[num] = occurences[num]+1

for k, v in occurences.items():
    r = rules[k]
    percent = v*100/n
    
    if not ((r-10)  < percent < (r+10)):
        fraud = 'true'
        break

print(fraud)