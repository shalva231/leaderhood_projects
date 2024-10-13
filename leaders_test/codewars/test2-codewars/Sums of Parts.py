def parts_sums(ls):
    Sum_list = []
    Sum = sum(ls)
    for i in ls:
        Sum_list.append(Sum)
        Sum -= i
    Sum_list.append(0)
    return Sum_list