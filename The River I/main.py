r_1 = int(input())
r_2 = int(input())

def river(n):
   r = 0
   m = n
   # sum digits of number n. ex: 123 = 1+2+3=6
   while n:
       r, n = r + n % 10, n // 10
   # The river is : 6 + 123
   return r+m

while(r_1 != r_2):
    if r_1 < r_2:
        r_1 = river(r_1)
    else:
        r_2 = river(r_2)
    
print(r_1)