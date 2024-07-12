
n = int(input())


def fib(n):
    if (n == 0 or n == 1):
        return n
        
    # Finds the greatest Fibonacci Number smaller
    # than n.
    f1, f2, f3 = 0, 1, 1
    while (f3 <= n):
        f1 = f2
        f2 = f3
        f3 = f1 + f2
    return f2

def zeckendorf(n):
     
    while (n>0):
 
        # Find the greates Fibonacci Number smaller
        # than or equal to n
        f = fib(n)
  
        print (f,end="")

        n = n-f
        
        if n > 0:
            print("+", end='')
 
zeckendorf(n)