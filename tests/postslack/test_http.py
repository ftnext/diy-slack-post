from unittest import TestCase
from unittest.mock import MagicMock, patch

from postslack import http as h


class BuildHeaderAsDictTestCase(TestCase):
    """TestCase for HTTP Request headers for slack api"""

    @patch("postslack.http.os.environ")
    def test_should_return_header_when_environment_variable_set(
        self, os_environ
    ):
        token = os_environ.get.return_value
        expected = {
            "Authorization": f"Bearer {token}",
            "Content-type": "application/json",
        }

        actual = h._build_header_as_dict()

        os_environ.get.assert_called_once_with("SLACK_BOT_USER_TOKEN")
        self.assertEqual(actual, expected)

    @patch("postslack.http.os.environ")
    def test_should_raise_error_when_environment_variable_not_set(
        self, os_environ
    ):
        os_environ.get.return_value = None

        with self.assertRaises(RuntimeError) as cm:
            h._build_header_as_dict()

        os_environ.get.assert_called_once_with("SLACK_BOT_USER_TOKEN")
        self.assertEqual(
            str(cm.exception), "環境変数 SLACK_BOT_USER_TOKEN を指定してください"
        )


class BuildBodyAsBytesTestCase(TestCase):
    """TestCase for HTTP Request body for slack api as bytes"""

    @patch("postslack.http.json.dumps")
    def test_should_return_bytes_data(self, json_dumps):
        channel, message = MagicMock(spec=str), MagicMock(spec=str)
        data_dict = {"channel": channel, "text": message}
        data_str = json_dumps.return_value

        actual = h._build_body_as_bytes(channel, message)

        json_dumps.assert_called_once_with(data_dict)
        data_str.encode.assert_called_once_with()
        self.assertEqual(actual, data_str.encode.return_value)


class RequestToApiTestCase(TestCase):
    """TestCase for HTTP request to slack API"""

    @patch("postslack.http.urlopen")
    @patch("postslack.http.Request")
    def test_should_call_api(self, factory_request, urlopen):
        header, body = MagicMock(spec=dict), MagicMock(spec=bytes)
        request = factory_request.return_value

        h._request_to_api(header, body)

        factory_request.assert_called_once_with(
            "https://slack.com/api/chat.postMessage",
            data=body,
            method="POST",
            headers=header,
        )
        urlopen.assert_called_once_with(request)
