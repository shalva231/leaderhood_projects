def unique_in_order(sequence):
    list = []
    ind = 0 
    for i in sequence:
        if i != list[ind]:
            list.append(i)
            index += 1
    return list
# failed
