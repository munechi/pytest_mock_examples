from unittest.mock import Mock

from pytest_mock import MockerFixture

from hogelib.api import hoge_api_1, hoge_api_2, hoge_api_3


class DummyResponse:
    def __init__(self, status_code: int, payload: dict):
        self.status_code = status_code
        self._payload = payload

    def json(self) -> dict:
        return self._payload


def test_hoge_api_1(mocker: MockerFixture):
    mock_response = DummyResponse(200, {"message": "ok"})
    mock_client = Mock()
    mock_client.post.return_value = mock_response

    mock_http_client = mocker.patch("hogelib.api.httpx.Client")
    mock_http_client.return_value.__enter__.return_value = mock_client
    mock_http_client.return_value.__exit__.return_value = None

    result = hoge_api_1()

    assert result is mock_response
    assert result.status_code == 200
    assert result.json() == {"message": "ok"}
    mock_http_client.assert_called_once_with()
    mock_client.post.assert_called_once_with("/hoge", json={})


def test_hoge_api_2(mocker: MockerFixture):
    mock_response = DummyResponse(200, {"message": "ok"})
    mock_client = Mock()
    mock_client.post.return_value = mock_response

    mock_http_client = mocker.patch(
        "hogelib.api.httpx.Client", return_value=mock_client
    )

    result = hoge_api_2()

    assert result is mock_response
    assert result.status_code == 200
    assert result.json() == {"message": "ok"}
    mock_http_client.assert_called_once_with()
    mock_client.post.assert_called_once_with("/hoge", json={})


def test_hoge_api_3(mocker: MockerFixture):
    mock_response = DummyResponse(200, {"message": "ok"})
    mock_post_json = mocker.patch("hogelib.api.post_json", return_value=mock_response)

    result = hoge_api_3()

    assert result is mock_response
    assert result.status_code == 200
    assert result.json() == {"message": "ok"}
    mock_post_json.assert_called_once_with("/hoge", {})
