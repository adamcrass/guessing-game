import random
import nltk

nltk.download('words')

def generate_random_word():
    word_list = nltk.corpus.words.words()
    basic_english_words = [word for word in word_list if word.lower() in nltk.corpus.words.words('en-basic')]
    five_letter_basic_words = [word for word in basic_english_words if len(word) == 5]
    return random.choice(five_letter_basic_words)

random_word = generate_random_word()
print(random_word)
