def luck_check(st):
    if st.isnumeric():
        if len(st) % 2 == 0:
            first = st[:len(st) // 2]
            second = st[len(st) // 2:]
        else:
            first = st[:len(st) // 2]
            second = st[len(st) // 2 + 1:]
        sum1 = 0
        sum2 = 0
        for i in first:
            sum1 += int(i)
        for i in second:
            sum2 += int(i)

        return sum1 == sum2
    else:
        raise ValueError