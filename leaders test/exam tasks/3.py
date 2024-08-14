def expand(num):
    if num // 10 == 0:
        return num
    

    str_num = str(num)
    list = []
    for i, digit in enumerate(str_num):
        if digit != 0:
            expanded = int(digit) * (10 ** (len(str_num) - i - 1))
            list.append(str(expanded))
    return  " + " .join(list)



'''
Test Cases:
70304 -> '70000 + 300 + 4'
42 -> '40 + 2'
710163 -> '700000 + 10000 + 100 + 60 + 3'
853546 -> '800000 + 50000 + 3000 + 500 + 40 + 6'
511604 -> '500000 + 10000 + 1000 + 600 + 4'
'''
print(expand(70304))
print(expand(42))
print(expand(710163))
print(expand(853546))
print(expand(511604))

