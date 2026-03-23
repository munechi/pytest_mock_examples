from unittest.mock import patch

from hogelib.main import hoge


def test_unittest():
    with patch("hogelib.main.greet", return_value="mocked") as mock_greet:
        assert hoge() == "mocked"
        mock_greet.assert_called_once_with()
