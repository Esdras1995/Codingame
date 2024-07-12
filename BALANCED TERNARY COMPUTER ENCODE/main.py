n = int(input())

def decimal_to_balanced_ternary(n):
    if n == 0:
        return '0'
    
    digits = []
    
    while n != 0:
        remainder = n % 3
        n = n // 3
        
        if remainder == 2:
            remainder = -1
            n += 1
        elif remainder == -2:
            remainder = 1
            n -= 1
        
        if remainder == -1:
            digits.append('T')
        else:
            digits.append(str(remainder))
    
    # The digits are collected in reverse order, so we need to reverse them at the end
    return ''.join(digits[::-1])

print(decimal_to_balanced_ternary(n))