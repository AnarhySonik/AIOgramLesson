import requests
import time
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
BOT_TOKEN: str = os.getenv('API_TOKEN')
API_URL: str = 'https://api.telegram.org/bot'
TEXT: str = 'Update!'
MAX_COUNTER: int = 10

offset: int = -2
counter: int = 0
chat_id: int

while counter < MAX_COUNTER:

    print('attempt =', counter)

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1
