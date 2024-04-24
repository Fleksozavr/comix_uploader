import requests
import random
from aiogram import Router, types


def get_random_num():
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()
    max_num = response.json()['num']
    return random.randint(1, max_num)


def download_comix(random_num):
    url = f'https://xkcd.com/{random_num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        author_text = response.json()['alt']
        image_url = response.json()['img']
        try:
            return image_url, author_text
        except AttributeError as err:
            print('Ошибка при извелчении атрибута:', err)


