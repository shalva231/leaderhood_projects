def walk(dir):
    if len(dir) != 10:
        return False
    
    north = dir.count("n")
    south = dir.count("s")
    east = dir.count("e")
    west = dir.count("w")

    if north - south == 0 and east - west == 0:
        return True
    else:
        return False

'''
Test Cases:
['w','e','w','e','w','e','w','e','w','e','w','e'] -> False
['n','s','n','s','n','s','n','s','n','s'] -> True
['n','n','n','s','n','s','n','s','n','s'] -> False
['e', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's'] -> False
['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'] -> True
'''

print(walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(walk(['n','s','n','s','n','s','n','s','n','s']))
print(walk(['n','n','n','s','n','s','n','s','n','s']))
print(walk(['e', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']))
print(walk(['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']))