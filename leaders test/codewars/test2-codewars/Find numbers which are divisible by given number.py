def divisible_by(numbers, divisor):
    new_list = []
    for i in numbers:
        if i % divisor == 0:
            new_list.append(i)
    return new_list