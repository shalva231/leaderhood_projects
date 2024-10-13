def multiply_all(arr):
    def second(n):
        result = []
        for i in arr:
            result.append(i*n)
        return result
    return second
        