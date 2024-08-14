def check(arr):
    if not arr:
        return True
    for i in arr:
        if type(i) == int:
            pass
        elif type(i) == float:
            if not i.is_integer():
                return False
        else:
            return False
    return True

'''
Test cases:
[] -> True
[1, 2, 3, 4] -> True
[1.0, 2.0, 3.0] -> True
[1.0, 2.0, 3.0001] -> False
["-1"] -> False
'''
print(check([]))
print(check([1, 2, 3, 4]))
print(check([1.0, 2.0, 3.0]))
print(check([1.0, 2.0, 3.0001]))
print(check(["-1"]))
