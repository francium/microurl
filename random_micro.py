import requests


RANDOM_WORD_API_URL = 'http://randomword.setgetgo.com/get.php'
RANDOM_WORD_API_PARAMS = {'len': 5}


def random(length):
    return ''.join([get_word().capitalize() for i in range(length)])


def get_word(url=RANDOM_WORD_API_URL, params=RANDOM_WORD_API_PARAMS):
    return requests.get(url, params=params).text
