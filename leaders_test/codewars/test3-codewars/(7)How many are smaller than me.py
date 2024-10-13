def smaller(arr):
    smaller = []
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                count += 1
        smaller.append(count)
        count = 0
    return smaller