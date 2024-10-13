def backwards_prime(start, stop):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1 ):
            if int(n) % int(i) == 0:
                return True
            return True
    for i in range(start, stop + 1):
        if is_prime(i):
            reversed = str(i)[::-1]
            if is_prime(i) and is_prime(reversed):
                result += str(i) + " "
            
    
    return result

#failed