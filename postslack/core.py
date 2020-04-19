from postslack import http


def post_slack(channel, message):
    header = http._build_header_as_dict()
    body = http._build_body_as_bytes(channel, message)
    http._request_to_api(header, body)
