def rot13(message):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y","Z"]
    for i in message:
        index = 0
        if i.upper() in alphabet:
            index = index + 13
            if index > 26:
                index = index - 26
                message.replace(i , alphabet[index])
            index += 1
        return message
    
    #failed