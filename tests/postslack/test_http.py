from unittest import TestCase
from unittest.mock import MagicMock, patch

from postslack import http as h


class BuildBodyTestCase(TestCase):
    """TestCase for postslack.http._build_body_bytes_data"""

    @patch("postslack.http.json.dumps")
    def test_should_return_bytes_data(self, json_dumps):
        channel, message = MagicMock(spec=str), MagicMock(spec=str)
        data_dict = {"channel": channel, "text": message}
        data_str = json_dumps.return_value

        actual = h._build_body_bytes_data(channel, message)

        json_dumps.assert_called_once_with(data_dict)
        data_str.encode.assert_called_once_with()
        self.assertEqual(actual, data_str.encode.return_value)
