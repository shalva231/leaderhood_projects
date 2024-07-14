def dating_range(age):
    if age <=14:
        min = age - 0.1 * age
        max = age + 0.1 * age
    else:
        min = 7 + (age//2) 
        max = (age-7)*2
    return f"{int(min)}-{int(max)}"