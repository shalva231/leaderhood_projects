def is_divisible(n, *hi):
    for i in hi:
        if n % i != 0:
            return False
    return True
    