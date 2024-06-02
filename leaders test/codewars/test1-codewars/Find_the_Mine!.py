def mine_location(field):
    for i_index,i in enumerate(field):
        for j_index,j in enumerate(i):
            if j == 1:
                return[i_index , j_index]