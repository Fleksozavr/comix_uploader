import requests
import random
import logger


logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_random_num():
    try:
        response = requests.get('https://xkcd.com/info.0.json')
        response.raise_for_status()
        comic_num = response.json()
        max_num = comic_num['num']
        return random.randint(1, max_num)
    except requests.RequestException as e:
        logging.error(f'Ошибка при получении случайного номера комикса: {e}')
        return None


def download_comix(random_num):
    try:
        url = f'https://xkcd.com/{random_num}/info.0.json'
        response = requests.get(url)
        response.raise_for_status()

        comic_data = response.json()
        image_url = comic_data.get('img')
        author_text = comic_data.get('alt')

        if image_url and author_text:
            return image_url, author_text
        else:
            logging.error('Ошибка при извлечении атрибута')
            return None, None
    except requests.RequestException as e:
        logging.error(f'Ошибка при загрузке комикса с номером {random_num}: {e}')
        return None, None
