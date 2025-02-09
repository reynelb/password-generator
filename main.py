import random

from constants import random_words, random_symbols

def random_number():
    return random.randint(0, 2099)

def do_capitalize(word):
    x = random.randint(0,1)
    if x == 0:
        if word.isalpha():
            return word.capitalize()
        else: 
            return word
    elif x == 1:
        return word


def pass_generator(custom_word, words_amount):
    password = ""
    random_words_to_use = random.sample(random_words, words_amount-1)
    rdm_idx_to_capitalize = random.randint(0, len(random_words_to_use)-1)
    random_words_to_use[rdm_idx_to_capitalize] = random_words_to_use[rdm_idx_to_capitalize].capitalize()
    words_to_use = [custom_word] + random_words_to_use + random.sample(random_symbols, words_amount-1) + [str(random_number())]    
    random.shuffle(words_to_use)

    for idx, word in enumerate(words_to_use):
        password = password + do_capitalize(word)
    
    return password


test_password = pass_generator("karlitonic", 3)
print(test_password) 
