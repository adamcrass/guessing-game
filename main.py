import random
import nltk

nltk.download('brown')
nltk.download('words')

correctly_guessed_positions = []

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

    while True:
        letter_guess = input("Guess a letter: ")

        if letter_guess.lower() == "what do i have so far":
            guessed_letters = [final_word[position - 1] for position in correctly_guessed_positions]
            print("Guessed letters:", guessed_letters)
            continue

        in_letter = [i + 1 for i, letter in enumerate(final_word) if letter == letter_guess]

        if in_letter:
            print(f"The letter '{letter_guess}' is the {' and '.join(map(str, in_letter))}{get_suffix(in_letter[0])} letter in the word.")
            correctly_guessed_positions.extend(in_letter)
        else:
            print(f"I'm sorry but '{letter_guess}' is not in the word. Try again")
