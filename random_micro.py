import requests


RANDOM_WORD_API_URL = 'http://setgetgo.com/randomword/get.php'
RANDOM_WORD_API_PARAMS = {'len': 5}


def random(length):
    '''
        Return a string of random words concatenated together.
    '''
    words = [get_word().capitalize() for i in range(length)]
    # Make first letter of first word lower case
    words[0] = words[0][0].lower() + words[0][1:]
    return ''.join(words)


def get_word(url=RANDOM_WORD_API_URL, params=RANDOM_WORD_API_PARAMS):
    '''
        Get a random word.
    '''
    return requests.get(url, params=params).text
