import requests
import json

from src.data_utils import get_data


def send_msg_to_discord(msg, key_path="KEY/discord_bot_key.json"):
    key_data = get_data(key_path)
    webhook_url = key_data['webhook_url']
    message = {
        "content": msg
    }

    response = requests.post(webhook_url, json=message)

    if response.status_code == 204:
        print("Successful sending messsage to discord bot")
    else:
        print(f"Failed sending message: {response.status_code}")