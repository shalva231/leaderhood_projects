def capitalize(s):
    index = 0
    even = ""
    odd = ""
    for i in s:
        if index % 2 == 0:
            odd += i.upper()
            even += i
        else:
            odd += i
            even += i.upper()
        index += 1
    return [odd, even]