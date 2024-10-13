def min_sum(arr):
    sum = 0
    arr.sort()
    
    for i in range(len(arr) // 2):
        sum += arr[i] * arr[-(i + 1)]
    return sum