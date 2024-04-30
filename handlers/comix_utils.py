import requests
import random


def get_random_num():
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()
    comic_num = response.json()
    max_num = comic_num['num']
    return random.randint(1, max_num)


def download_comix(random_num):
    url = f'https://xkcd.com/{random_num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    
    if response.status_code != 200:
        print(f'Ошибка загрузки комикса с номером {random_num}')
        return None, None
    
    comic_data = response.json()
    image_url = comic_data.get('img')
    author_text = comic_data.get('alt')
    
    if image_url and author_text:
        return image_url, author_text
    else:
        print('Ошибка при извлечении атрибута')
        return None, None


