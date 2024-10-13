def repeats(arr):
    sum = 0
    for i in arr:
        count = arr.count(i)
        if count == 1:
            sum += i
    return sum