from unittest.mock import Mock

#
# Mock() の引数の使い方
#


def test_return_value_returns_same_value_every_time():
    mock_greet = Mock(return_value="mocked")

    assert mock_greet() == "mocked"
    assert mock_greet() == "mocked"
    assert mock_greet.call_count == 2


def test_side_effect_function_can_use_arguments():
    def fake_greet(name: str) -> str:
        return f"Hello, {name}"

    mock_greet = Mock(side_effect=fake_greet)

    assert mock_greet("ojisama") == "Hello, ojisama"
    mock_greet.assert_called_once_with("ojisama")


def test_side_effect_exception_can_raise_error():
    mock_greet = Mock(side_effect=RuntimeError("boom"))

    try:
        mock_greet()
        assert False, "RuntimeError should be raised"
    except RuntimeError as exc:
        assert str(exc) == "boom"


def test_side_effect_list_can_change_return_value_each_time():
    mock_greet = Mock(side_effect=["a", "b", "c"])

    assert mock_greet() == "a"
    assert mock_greet() == "b"
    assert mock_greet() == "c"
    assert mock_greet.call_count == 3
