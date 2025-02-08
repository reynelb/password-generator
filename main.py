import random

random_words = [
    "apple", "banana", "cat", "dog", "egg", "fish", "grape", "hat", "ice", "jam",
    "kite", "lemon", "moon", "nose", "orange", "pencil", "queen", "rain", "sun", "tree",
    "umbrella", "violin", "water", "xray", "yellow", "zebra", "ant", "ball", "car", "desk",
    "elephant", "flower", "goat", "house", "island", "jump", "key", "lamp", "mouse", "net",
    "ocean", "pizza", "quilt", "rabbit", "snake", "turtle", "under", "van", "window", "xylophone",
    "yogurt", "zoo", "air", "book", "chair", "door", "ear", "fork", "garden", "heart",
    "iceberg", "jungle", "kettle", "lion", "milk", "nut", "open", "pillow", "quiet", "river",
    "stone", "table", "uncle", "vase", "whale", "xenon", "yawn", "zippy", "angel", "beach",
    "candy", "duck", "earth", "family", "gold", "honey", "idea", "joke", "kind", "leaves",
    "music", "night", "octopus", "party", "quick", "rainbow", "smile", "train", "understand", "vivid",
    "wonder", "xray", "yummy", "zesty", "big", "clap", "drum", "eat", "fast",
    "grin", "happy", "igloo", "jolly", "kitten", "love", "mango", "nap", "owl", "play",
    "quietly", "run", "sing", "top", "up", "visit", "whisper", "excite", "yarn", "zoom",
    "able", "baby", "cool", "dream", "easy", "fun", "gift", "hope", "inspire", "jumping",
    "kindness", "lucky", "magic", "nice", "peace", "quickly", "rest", "sunshine", "thankful",
    "unique", "victory", "warm", "excellent", "young", "zipper", "apron", "butter", "cup", "dance",
    "echo", "famous", "good", "harmony", "jewel", "light", "mirror", "nest",
    "opera", "puppy", "rose", "splash", "tender", "violet", "wave", "exciting",
    "zigzag", "amazing", "bright", "cloud", "delight", "enjoy", "friend", "giggle", "hug",
    "interesting", "joy", "laughter", "moment", "open", "pure", "quiet", "restful", "silly",
    "thrill", "victory", "wild", "exotic", "youth", "zen", "aroma", "bouncy", "cocoa", "doodle",
    "emerald", "frost", "glow", "mystic", "oasis", "peaceful", "refresh", "serene", "thrilling",
    "unicorn", "warm", "zebra", "arcade", "ballad", "crescent", "duet", "epic", "finesse",
    "groove", "hymn", "jazzy", "lyric", "melody", "noodle", "panorama", "quintet",
    "rhapsody", "sonnet", "tempo", "undertone", "whirl", "yodel", "zenith",
    "amaranth", "bliss", "celestial", "dewdrop", "ethereal", "fawn", "halcyon", "iridescent",
    "jubilant", "kindred", "luminescence", "mystic", "nirvana", "panache", "quintessence",
    "resplendent", "serenity", "tranquil", "umbra", "vernal", "whimsical", "xenon", "zephyr",
    "astral", "bewilder", "delirium", "eldritch", "fascination", "hazy", "illusory", "jittery",
    "lurid", "mystique", "nebulous", "phantom", "quirky", "reclusive", "spectral", "tenebrous",
    "uncanny", "vexing", "weird", "xenomorph", "yearning", "zealous", "alluring", "captivating",
    "dreamy", "fabled", "glistening", "imagine", "jeweled", "lively", "moonbeam", "nymph",
    "radiant", "soulful", "timeless", "unearthly", "wistful", "yearlong", "zesty",
    "bizarre", "charismatic", "dizzying", "enchanting", "glowing", "hushed", "joyous",
    "kismet", "legendary", "mesmerizing", "ominous", "peculiar", "resilient", "sublime",
    "thunderous", "unwavering", "vibrant", "wondrous", "zenith", "adorable", "brilliant",
    "cheerful", "dazzling", "exuberant", "fun-loving", "grateful", "hopeful", "intense",
    "jolly", "kindhearted", "majestic", "outstanding", "playful", "quick", "rejuvenated",
    "spirited", "trusting", "uplifted", "valiant", "wise", "exuberance", "youthful", "zany",
    "artistic", "breezy", "carefree", "delicate", "eager", "fearless", "genuine", "huggable",
    "ideal", "joyful", "keen", "limitless", "miraculous", "open", "perfect", "radiant",
    "satisfied", "tender", "universal", "vibrant", "warmhearted", "extraordinary",
    "yummy", "admirable", "brilliant", "delighted", "effortless", "festive", "genuine",
    "helpful", "innovative", "joyful", "kindness", "luminous", "magnificent", "noble",
    "outstanding", "playful", "radiant", "sublime", "thrilling", "unforgettable",
    "victorious", "whimsical", "zesty"
]

random_symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", 
    "[", "]", "{", "}", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", 
    "?", "/", "~", "`"
]

years = [
    1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909,
    1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919,
    1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929,
    1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939,
    1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949,
    1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959,
    1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969,
    1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979,
    1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
    1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
    2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
    2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
    2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029,
    2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039,
    2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049,
    2050
]

def random_generator():
    number = random.uniform(0,1)
    if number >= 0.5:
        return True
    elif number <= 0.5:
        return False

def pass_generator(custom_word, words_amount):
    
    password = ""
    words_to_use = []
    words_to_use.append(custom_word)
    
    for i in range(words_amount-1):
        words_to_use.append(random.choice(random_words))

    boolean = random_generator()
    
    while(len(words_to_use) != 0):
        word = random.choice(words_to_use)
        words_to_use.remove(word)
        #print(boolean)
        if boolean:
            word = word.capitalize() + random.choice(random_symbols)
        password += word
        
        boolean = not boolean
        

    password += str(random.choice(years))

    return password

password1 = pass_generator("hola", 3)
print(password1) 
