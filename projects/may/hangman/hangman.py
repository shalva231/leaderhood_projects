import random

word_arr = [
    "apple", "banana", "cherry", "date", "elderberry", 
    "fig", "grape", "honeydew", "kiwi", "lemon", 
    "mango", "nectarine", "orange", "peach", "quince", 
    "raspberry", "strawberry", "tangerine", "watermelon", "apricot", 
    "blueberry", "cantaloupe", "dragonfruit", "guava", "jackfruit", 
    "kiwifruit", "lime", "melon", "papaya", "pineapple", 
    "raisin", "starfruit", "tomato", "avocado", "blackberry", 
    "coconut", "durian", "grapefruit", "jujube", "kumquat", 
    "lychee", "mulberry", "olive", "passionfruit", "plum", 
    "rambutan", "soursop", "tamarind", "ugli fruit", "yuzu", 
    "zucchini", "asparagus", "broccoli", "cabbage", "dill", 
    "eggplant", "fennel", "garlic", "horseradish", "jicama", 
    "kale", "leek", "mushroom", "onion", "parsnip", 
    "radish", "spinach", "turnip", "watercress", "artichoke", 
    "beet", "carrot", "daikon", "endive", "frisee", 
    "ginger", "jalapeno", "kohlrabi", "lettuce", "okra", 
    "parsley", "rutabaga", "squash", "taro", "yam", 
    "zucchini", "barley", "corn", "lentil", "millet", 
    "oat", "quinoa", "rice", "sorghum", "teff", 
    "wheat", "almond", "cashew", "hazelnut", "pecan", 
    "pistachio"
]

def display_hangman(tries):
    stages = [
        '''
        =========
        ''', 
        '''
            |
            |
            |
            |
            |
        =========
        ''', 
        '''
        +---+
            |
            |
            |
            |
            |
        =========
        ''', 
        '''
        +---+
        |   |
            |
            |
            |
            |
        =========''', 
        '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        ''', 
        '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        ''', 
        '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
        ''', 
        '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        ''', 
        '''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        ''', 
        '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        '''
    ]
    return stages[tries]

def random_word():
    return random.choice(word_arr).upper()

def hang_man():
    word = random_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 0

    print("!!! Let's play Hangman !!!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries < 9:
        guess = input("Please enter a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries += 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries += 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print("Congratulations, you guessed the word!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}.")

if __name__ == "__main__":
    hang_man()