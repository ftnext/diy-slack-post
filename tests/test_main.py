from unittest import TestCase
from unittest.mock import call, patch

import main as m


class MainTestCase(TestCase):
    """TestCase for main.py, entrypoint script"""

    @patch("argparse.ArgumentParser")
    def test_should_parse_args(self, mock_argument_parser):
        parser = mock_argument_parser.return_value

        m.main()

        mock_argument_parser.assert_called_once()
        parser.add_argument.assert_has_calls(
            [call("channel"), call("message")]
        )
        parser.parse_args.assert_called_once()
