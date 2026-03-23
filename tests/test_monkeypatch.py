from unittest.mock import Mock

from pytest import MonkeyPatch

from hogelib.main import hoge


def test_monkeypatch(monkeypatch: MonkeyPatch):
    fake_greet = Mock(return_value="mocked")
    monkeypatch.setattr("hogelib.main.greet", fake_greet)

    assert hoge() == "mocked"
    fake_greet.assert_called_once_with()
