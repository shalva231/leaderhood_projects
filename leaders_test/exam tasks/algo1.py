def dot(a,b):
    list = []
    for i in a:
        for j in b:
            list.append(i*j)
    return sum(list)

'''
1: [1, 2, 3] x [4, 5, 6]
2: [2, 3] x [4, 5]
3: [7, -2, 5] x [3, 4, 6]

'''

print(dot([1, 2, 3], [4, 5, 6]))
print(dot([ 2, 3], [4, 5]))
print(dot([7, -2, 5], [3, 4, 6]))