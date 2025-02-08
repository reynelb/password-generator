import random

from constants import random_words, random_symbols

def random_year():
    return random.randint(1100, 2099)


def pass_generator(custom_word, words_amount):
    password = ""
    random_words_to_use = random.sample(random_words, words_amount-1)
    words_to_use = [custom_word] + random_words_to_use
    capitalised_word_pos = random.randint(0, words_amount-1)        
    random.shuffle(words_to_use)

    for idx, word in enumerate(words_to_use):
        current_word = word
        if idx == capitalised_word_pos:
            current_word = word.capitalize() + random.choice(random_symbols)
        password += current_word
    
    password += str(random_year())
    return password


test_password = pass_generator("firstTry", 2)
print(test_password) 
