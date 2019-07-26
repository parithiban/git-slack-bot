from config import get_env
import requests
import json
import os


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

    def send_as_attachment(self, content, channel):

        url = "https://slack.com/api/files.upload"

        files = {
            'file': (content, open(content, 'rb'), 'csv')
        }

        payload = {
            "token": get_env('BOT_TOKEN'),
            "channels": channel,
            "filename": "git_users.csv",
            "title": "List of users in emisgroup organisation"
        }

        response = requests.request(
            "POST", url, data=payload, files=files)
        result = json.loads(response.text)

        if result["ok"]:
            os.remove(content)
