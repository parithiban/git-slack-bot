from config import get_env
import requests
import json


class SlackHelper:

    def send_message(self, message, url):

        payload = {
            "text": message,
            "response_type": "in_channel",
            "mrkdwn": True
        }

        payload = json.dumps(payload)
        print(payload)
        headers = {
            'Content-Type': "application/json"
        }

        requests.request("POST", url, data=payload, headers=headers)
