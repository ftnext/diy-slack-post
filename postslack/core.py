from postslack import http


def post_slack(channel, message):
    header = http._build_header()
    body = http._build_body(channel, message)
    http._request_to_api(header, body)
