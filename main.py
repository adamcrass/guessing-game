import random
import nltk

nltk.download('brown')
nltk.download('words')

difficulty = input("Please select a difficulty (1, 2, 3 or q to quit): ")

if difficulty != "q":

    if difficulty == "1":
        def generate_basic_word():
            basic_english_words = set(word.lower() for word in nltk.corpus.brown.words() if word.isalpha())
            five_letter_basic_words = [word for word in basic_english_words if len(word) == 5] 
            word_decided_on = random.choice(five_letter_basic_words)
            return word_decided_on
        
        final_word = generate_basic_word()

    if difficulty == "2":
        def generate_normal_word():
            basic_english_words = set(word.lower() for word in nltk.corpus.brown.words() if word.isalpha())
            word_decided_on = random.choice(list(basic_english_words))
            return word_decided_on
        
        final_word = generate_normal_word()

    if difficulty == "3":
        def generate_hard_word():
            word_list = nltk.corpus.words.words()
            word_decided_on = random.choice(word_list)
            return word_decided_on
        
        final_word = generate_hard_word()

    random_word = final_word
    print(random_word)



else:
    quit()
