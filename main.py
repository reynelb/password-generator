import random

from constants import random_words, random_symbols

def random_year():
    return random.randint(1100, 2099)

def do_capitalize(word):
    x = random.randint(0,1)
    if x == 0:
        return word.capitalize()
    elif x == 1:
        return word


def pass_generator(custom_word, words_amount):
    password = ""
    random_words_to_use = random.sample(random_words, words_amount-1)
    words_to_use = [custom_word] + random_words_to_use
    symbols_nums_to_use = random.sample(random_symbols, words_amount-1) + [str(random_year())]     
    random.shuffle(words_to_use)
    random.shuffle(symbols_nums_to_use)

    for idx, word in enumerate(words_to_use):
        password = password + do_capitalize(word) + str(symbols_nums_to_use.pop(0))
    
    return password


test_password = pass_generator("first", 2)
print(test_password) 
