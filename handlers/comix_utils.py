import requests
import random
from random import randint
from aiogram import Router, F, types


class Image:


    def get_random_num(self):
        response = requests.get('https://xkcd.com/info.0.json')
        response.raise_for_status()
        max_num = response.json()['num']
        return random.randint(1, max_num)


    def download_comix(self):
        random_num = self.get_random_num()
        url = f'https://xkcd.com/{random_num}/info.0.json'
        response = requests.get(url)
        response.raise_for_status()

        try:
            data = response.json()
            image_url = data['img']
            return image_url

        except Exception as err:
            print('Error when receiving picture:', err)


    def get_author_comment(self):
        random_num = self.get_random_num()
        url = f'https://xkcd.com/{random_num}/info.0.json'
        response = requests.get(url)
        response.raise_for_status()

        try:
            author_text = response.json()['alt']
            return author_text

        except Exception as err:
            print('Error when receiving text:', err)
