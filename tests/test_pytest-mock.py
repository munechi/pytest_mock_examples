from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from hogelib.main import hoge


# テスト内部でモックオブジェクトを定義する
def test_pytest_mock(mocker: MockerFixture):
    fake_greet = mocker.patch("hogelib.main.greet")
    fake_greet.return_value = "mocked"

    assert hoge() == "mocked"
    fake_greet.assert_called_once_with()


# fixture としてモックオブジェクトを定義する
@pytest.fixture
def mock_greet(mocker: MockerFixture):
    return mocker.patch("hogelib.main.greet")


def test_pytest_mock_fixture(mock_greet: Mock):
    mock_greet.return_value = "mocked"

    assert hoge() == "mocked"
    mock_greet.assert_called_once_with()
