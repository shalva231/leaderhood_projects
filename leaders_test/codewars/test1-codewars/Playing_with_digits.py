def dig_pow(n, p):
    digits = str(n)
    total = 0
    
    for i,digit in enumerate(digits):
        total += int(digit) ** (p + i)
    
    if total % n == 0:
        return total / n
    else:
        return -1
    
