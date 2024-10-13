# write the function is_anagram
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    test = "".join(sorted(test))
    original = "".join(sorted(original))
        
        
    if test == original:
        return True
    else:
        return False
            