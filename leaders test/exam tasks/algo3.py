def binary(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    list = []
    while num > 0:
        list.append(str(num%2))
        num = num // 2

    list.reverse()
    return "".join(list)

print(binary(32))
print(binary(8))
print(binary(31))
