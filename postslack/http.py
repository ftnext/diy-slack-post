import json


def _build_header():
    raise NotImplementedError


def _build_body_bytes_data(channel, message):
    """return HTTP request body as bytes, utf-8 encoded"""
    data_dict = {"channel": channel, "text": message}
    data_str = json.dumps(data_dict)
    return data_str.encode()


def _request_to_api(header, body):
    raise NotImplementedError
