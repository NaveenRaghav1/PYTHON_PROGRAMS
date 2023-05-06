import random

def get_random_word():
    words = ['python', 'programming', 'computer', 'science', 'code']
    return random.choice(words)

def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    """            --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
    """,
    """

                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
    """,
    """            --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
    """
    ]
    return stages[tries]

def play_hangman():
    word = get_random_word()
    word_list = list(word)
    guesses = []
    tries = 8
    done = False
    
    print("Let's play hangman!")
    
    while not done:
        print(display_hangman(tries))
        for letter in word:
            if letter.lower() in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print('')
        
        guess = input(f"You have {tries} tries left. Enter a letter: ").lower()
        
        if guess in guesses:
            print(f"You already guessed {guess}. Try again.")
        elif guess in word_list:
            print(f"Good job! {guess} is in the word.")
            guesses.append(guess)
        else:
            print(f"Sorry, {guess} is not in the word.")
            tries -= 1
            
        if tries == 0:
            print(display_hangman(tries))
            print("Sorry, you ran out of tries. The word was", word)
            done = True
            
        if set(word_list) == set(guesses):
            print("Congratulations, you guessed the word", word)
            done = True

play_hangman()