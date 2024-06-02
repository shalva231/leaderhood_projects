def generate_hashtag(s):
    s = s.strip()
    if not s:
        return False
    
    words = s.split()
    capitalized_words  = []
    for word in words:
        capitalized_words.append(word.capitalize())
        
    hashtag = "".join(capitalized_words)
    hashtag = "#" + hashtag
    
    if len(hashtag) > 140:
        return False
    return hashtag