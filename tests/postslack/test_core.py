from unittest import TestCase
from unittest.mock import MagicMock, patch

from postslack import core as c


class PostSlackTestCase(TestCase):
    """TestCase for postslack.core.post_slack"""

    @patch("postslack.http._request_to_api")
    @patch("postslack.http._build_body_bytes_data")
    @patch("postslack.http._build_header")
    def test_should_send_message(
        self, build_header, build_body, request_to_api
    ):
        channel, message = MagicMock(spec=str), MagicMock(spec=str)
        header = build_header.return_value
        body = build_body.return_value

        c.post_slack(channel, message)

        build_header.assert_called_once_with()
        build_body.assert_called_once_with(channel, message)
        request_to_api.assert_called_once_with(header, body)
