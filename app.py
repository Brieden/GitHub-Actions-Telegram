import sys
import requests

telegram_token = sys.argv[0]
telegram_chat_id = sys.argv[1]

response = requests.post(
        url=f'https://api.telegram.org/bot{telegram_token}/sendMessage',
        data={'chat_id': telegram_chat_id, 'text': 'Hello world'}
    ).json()

print(response)
