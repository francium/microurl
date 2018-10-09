import random
import string


def random_words(length):
    '''
        Return a string of random words concatenated together.
    '''
    words = [get_word().capitalize() for i in range(length)]
    # Make first letter of first word lower case
    words[0] = words[0][0].lower() + words[0][1:]
    return ''.join(words)


def get_word(word_length=5):
    '''
        Get a random word.
    '''
    return ''.join([random.choice(string.ascii_letters) for _ in range(word_length)])
