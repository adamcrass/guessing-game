import random
import nltk

nltk.download('brown')
nltk.download('words')

correctly_guessed_letters = set()

# Function to get the appropriate suffix for a position
def get_suffix(position):
    if 10 <= position % 100 <= 20:
        suffix = "th"
    else:
        suffixes = {1: "st", 2: "nd", 3: "rd"}
        suffix = suffixes.get(position % 10, "th")
    return suffix

while True:
    difficulty = input("Please select a difficulty (1, 2, 3 or q to quit): ")

    if difficulty.lower() == "q":
        break

    if difficulty == "1":
        def generate_basic_word():
            basic_english_words = set(word.lower() for word in nltk.corpus.brown.words() if word.isalpha())
            short_basic_words = [word for word in basic_english_words if len(word) <= 5] 
            return random.choice(short_basic_words)
        
        final_word = generate_basic_word()

    elif difficulty == "2":
        def generate_normal_word():
            basic_english_words = set(word.lower() for word in nltk.corpus.brown.words() if word.isalpha())
            return random.choice(list(basic_english_words))
        
        final_word = generate_normal_word()

    elif difficulty == "3":
        def generate_hard_word():
            word_list = nltk.corpus.words.words()
            return random.choice(word_list)
        
        final_word = generate_hard_word()

    else:
        print("Invalid input. Please enter 1, 2, 3, or q to quit.")
        continue

    max_guesses = len(set(final_word)) + 5
    remaining_guesses = max_guesses
    correctly_guessed_letters = set()

    while remaining_guesses > 0:
        letter_guess = input("Guess a letter: ")

        if letter_guess.lower() == "what do i have so far":
            print("Guessed letters:", sorted(correctly_guessed_letters))
            continue

        if len(letter_guess) != 1 or not letter_guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
            continue

        if letter_guess in correctly_guessed_letters:
            print(f"You've already guessed '{letter_guess}'. Try again.")
            continue

        if letter_guess in final_word:
            positions = [i + 1 for i, letter in enumerate(final_word) if letter == letter_guess]
            print(f"The letter '{letter_guess}' is in the word at position(s) {', '.join(map(str, positions))}{get_suffix(positions[0])}")
            correctly_guessed_letters.add(letter_guess)
        else:
            remaining_guesses -= 1
            print(f"I'm sorry but '{letter_guess}' is not in the word. You have {remaining_guesses} guesses remaining.")
            
        if set(correctly_guessed_letters) == set(final_word):
            print(f"Congratulations! You guessed the word '{final_word}' correctly!")
            break

    if remaining_guesses == 0:
        print(f"Sorry, you've run out of guesses. The word was '{final_word}'.")
