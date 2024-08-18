import math
def going(n):
    sum = 0
    for i in range(1, n+1):
        sum += math.factorial(i)
    
    n = math.factorial(n)
    
    return sum / n