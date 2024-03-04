import random
import nltk

nltk.download('brown')
nltk.download('words')

correctly_guessed_letters = ""

while True:
    difficulty = input("Please select a difficulty (1, 2, 3 or q to quit): ")

    if difficulty.lower() == "q":
        break

    if difficulty == "1":
        def generate_basic_word():
            basic_english_words = set(word.lower() for word in nltk.corpus.brown.words() if word.isalpha())
            short_basic_words = [word for word in basic_english_words if len(word) <= 5] 
            word_decided_on = random.choice(short_basic_words)
            return word_decided_on
        
        final_word = generate_basic_word()

    elif difficulty == "2":
        def generate_normal_word():
            basic_english_words = set(word.lower() for word in nltk.corpus.brown.words() if word.isalpha())
            word_decided_on = random.choice(list(basic_english_words))
            return word_decided_on
        
        final_word = generate_normal_word()

    elif difficulty == "3":
        def generate_hard_word():
            word_list = nltk.corpus.words.words()
            word_decided_on = random.choice(word_list)
            return word_decided_on
        
        final_word = generate_hard_word()

    else:
        print("Invalid input. Please enter 1, 2, 3, or q to quit.")
        continue

    while True:
        letter_guess = input("Guess a letter: ")

        in_letter = [i + 1 for i, letter in enumerate(final_word) if letter == letter_guess]

        if in_letter:
            print(f"The letter '{letter_guess}' is the {' and '.join(map(str, in_letter))}st letter in the word.")
            correctly_guessed_letters += str(letter_guess)


        if letter_guess == "what do i have so far":
            print(correctly_guessed_letters)

        else:
            print(f"I'm sorry but '{letter_guess}' is not in the word. Try again")
