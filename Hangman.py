import random
lives = 6

Words = ['wares', 'soup', 'mount', 'extend', 'brown', 'expert', 'tired',
         'humidity', 'backpack', 'crust', 'dent', 'market', 'knock', 'smite',
         'windy', 'coin', 'throw', 'silence', 'bluff', 'downfall', 'climb',
         'lying', 'weaver', 'snob', 'kickoff', 'match', 'quaker', 'foreman',
         'excite', 'thinking', 'mend', 'allergen', 'pruning', 'coat', 'affirm',
         'captive', 'flipping', 'prolong', 'main', 'coral', 'dinner', 'rabbit',
         'chill', 'seed', 'born', 'shampoo', 'italian', 'giggle', 'roost', 'palm',
         'globe', 'wise', 'grandson', 'running', 'sunlight', 'spending', 'crunch',
         'tangle', 'forego', 'tailor', 'divinity', 'probe', 'bearded', 'premium',
         'featured', 'serve', 'borrower', 'examine', 'draw', 'anchovy', 'scream',
         'blush', 'hybrid', 'buffet', 'lively']

HangMan = ["""
            _________
            |       |
            |
            |
            |
            |
            |
       -----------
""", """
            _________
            |       |
            |       O
            |
            |
            |
            |
       -----------
""", """
            _________
            |       |
            |       O
            |       |
            |       |
            |       |
            |
       -----------
""", """
            _________
            |       |
            |       O
            |      /|
            |       |
            |       |
            |
       -----------
""", """
            _________
            |       |
            |       O
            |      /|\\
            |       |
            |       |
            |
       -----------
""", """
            _________
            |       |
            |       O
            |      /|\\
            |       |
            |      /|
            |
       -----------
""", """
            _________
            |       |
            |       O
            |      /|\\
            |       |
            |      /|\\
            |
       -----------
"""]


def play():
    try:
        word_choose = random.choice(Words)
        word_len = list("_" * len(word_choose))
        guessed = False
        curr_guess = 1
        guessed_letters = []
        while not guessed:
            print("\t\tWelcome to the Hangman Game")
            print(f"You have to guess a word, and to guess a word you will be given {lives} chances to guess correct word")
            print("Everytime, you opt in wrong word your chances will be reduced.")
            print("Get ready to play....")
            while curr_guess < lives:
                print(HangMan[curr_guess-1])
                print(''.join(word_len))
                print("Enter a letter: ", end="")
                letter = input()
                if letter.isalpha() and len(letter) == 1 and letter not in guessed_letters:
                    if letter in word_choose:
                        for i in range(len(word_choose)):
                            if word_choose[i] == letter:
                                word_len[i] = letter
                                ver = ''.join(word_len)
                                if ver == word_choose:
                                    print(f"You have correctly guessed the word '{word_choose}'")
                                    return guessed is True
                                else:
                                    guessed_letters.append(letter)
                    else:
                        print("Oops! you guesses wrong...")
                        curr_guess += 1
                        if curr_guess == 6:
                            guessed = True
                            print(HangMan[curr_guess-1])
                            print("Out of lives...")
                else:
                    if len(letter) > 1:
                        print("PLease enter 1 word only")
                    elif letter in guessed_letters:
                        print("You have already guessed this letter")
                    else:
                        print("Please enter words only...")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == '__main__':
    play()
