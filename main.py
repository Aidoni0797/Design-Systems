import os
import requests
from googleapiclient.discovery import build


api_key = 'AIzaSyB1BmsQNVHohOPw7xiaT_QxJsb-TzwsSVc'

youtube = build('youtube', 'v3', developerKey=api_key)


video_id = '6Sw6onqyfcA'

BOT_TOKEN = '8178967594:AAE14G4kmVksV-Y3oyZNBQkxe98JDYQgzws'
CHAT_ID = '1163463444'


def get_video_stats(video_id):
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    response = request.execute()

    if 'items' in response:
        stats = response['items'][0]['statistics']
        return stats
    else:
        return None



def print_video_stats():
    stats = get_video_stats(video_id)
    if stats:
        message = f"Views: {stats['viewCount']}"

        # Отправка сообщения в Telegram
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        params = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }
        requests.get(url, params=params)
    else:
        message = "I have problem"

        # Отправка сообщения в Telegram
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        params = {
            'chat_id': CHAT_ID,
            'text': message,
            'parse_mode': 'Markdown'
        }
        requests.get(url, params=params)



