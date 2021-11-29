import sys
import requests

telegram_token = sys.argv[1]
telegram_chat_id = sys.argv[2]

telegram_response = requests.get(
        url=f'https://api.telegram.org/bot{telegram_token}/sendMessage',
        data={'chat_id': str(telegram_chat_id), 'text': 'Hello world'}
    ).json()

print(telegram_response)
