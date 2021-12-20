import requests
import arrow
import json
from pathlib import Path

def post_message_to_slack(text):
    token = eval(Path("/etc/sre/slack.conf").read_text())['token']
    return requests.post('https://hooks.slack.com/services/' + token, json={
        "text": text,
        })


def on_message(client, msg, payload=None):
    if '/slack/notify' in msg.topic:
        data = json.loads(msg.payload)
        msg = f"{data['module']}: {data['value']}"
        post_message_to_slack(msg)
