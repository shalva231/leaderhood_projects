def variance(numbers): 
    mean = sum(numbers) / len(numbers)
    
    variance = 0
    for x in numbers:
        variance += (x - mean ) ** 2
    return variance / len(numbers)