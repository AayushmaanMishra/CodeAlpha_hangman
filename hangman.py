import random

def hangman():
    countries = {
        'canada': 'Known for maple syrup and hockey',
        'brazil': 'Home to the Amazon rainforest',
        'japan': 'Land of the rising sun',
        'egypt': 'Famous for pyramids and the Nile River',
        'italy': 'Shaped like a boot and known for pizza',
        'australia': 'Home to kangaroos and the Great Barrier Reef',
        'norway': 'Land of fjords and the midnight sun',
        'kenya': 'Famous for safari and the Maasai Mara'
    }
    
    secret_word = random.choice(list(countries.keys()))
    hint = countries[secret_word]
    guessed_letters = []
    max_attempts = 6
    attempts_left = max_attempts
    word_progress = ['_'] * len(secret_word)
    hint_given = False
    
    print("Welcome to Country Hangman!")
    print("Guess the country name one letter at a time. You have 6 incorrect guesses allowed.")
    print(" ".join(word_progress))
    
    while attempts_left > 0 and '_' in word_progress:
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    word_progress[i] = guess
            print("Correct!")
        else:
            attempts_left -= 1
            print(f"Wrong! You have {attempts_left} attempts left.")
            
            if not hint_given and attempts_left <= max_attempts - 2:
                print(f"Hint: {hint}")
                hint_given = True
        
        print(" ".join(word_progress))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
    
    if '_' not in word_progress:
        print(f"Congratulations! You guessed the country: {secret_word.capitalize()}")
    else:
        print(f"Game over! The country was: {secret_word.capitalize()}")

hangman()