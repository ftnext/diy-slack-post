import json
import os
from urllib.request import Request, urlopen


def _build_header_as_dict():
    """return HTTP request header as dict

    token to call API is specified
    as a environment variable `SLACK_BOT_USER_TOKEN`.
    """
    token = os.environ.get("SLACK_BOT_USER_TOKEN")
    if token is None:
        raise RuntimeError("環境変数 SLACK_BOT_USER_TOKEN を指定してください")
    return {
        "Authorization": f"Bearer {token}",
        "Content-type": "application/json",
    }


def _build_body_as_bytes(channel, message):
    """return HTTP request body as bytes, utf-8 encoded"""
    data_dict = {"channel": channel, "text": message}
    data_str = json.dumps(data_dict)
    return data_str.encode()


def _request_to_api(header, body):
    uri = "https://slack.com/api/chat.postMessage"
    request = Request(uri, data=body, headers=header, method="POST")
    urlopen(request)
