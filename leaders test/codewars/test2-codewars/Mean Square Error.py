def solution(array_a, array_b):
    ind = 0
    list = []
    for _ in range(len(array_a)):
        if array_a[ind] > array_b[ind]:
            list.append((array_a[ind] - array_b[ind]) ** 2)
            ind += 1
        else:
            list.append((array_b[ind] - array_a[ind]) ** 2)
            ind += 1
    
    return sum(list) / len(list)