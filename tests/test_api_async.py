import asyncio
from unittest.mock import AsyncMock, Mock

from pytest_mock import MockerFixture

from hogelib.api_async import hoge_api_async_1, hoge_api_async_2, hoge_api_async_3


class DummyResponse:
    def __init__(self, status_code: int, payload: dict):
        self.status_code = status_code
        self._payload = payload

    def json(self) -> dict:
        return self._payload


def test_hoge_api_async_1(mocker: MockerFixture):
    mock_response = DummyResponse(200, {"message": "ok"})
    mock_client = Mock()
    mock_client.post = AsyncMock(return_value=mock_response)

    mock_async_client = mocker.patch("hogelib.api_async.httpx.AsyncClient")
    mock_async_client.return_value.__aenter__ = AsyncMock(return_value=mock_client)
    mock_async_client.return_value.__aexit__ = AsyncMock(return_value=None)

    result = asyncio.run(hoge_api_async_1())

    assert result is mock_response
    assert result.status_code == 200
    assert result.json() == {"message": "ok"}
    mock_async_client.assert_called_once_with()
    mock_client.post.assert_awaited_once_with("/hoge", json={})


def test_hoge_api_async_2(mocker: MockerFixture):
    mock_response = DummyResponse(200, {"message": "ok"})
    mock_client = Mock()
    mock_client.post = AsyncMock(return_value=mock_response)

    mock_async_client = mocker.patch("hogelib.api_async.httpx.AsyncClient", return_value=mock_client)

    result = asyncio.run(hoge_api_async_2())

    assert result is mock_response
    assert result.status_code == 200
    assert result.json() == {"message": "ok"}
    mock_async_client.assert_called_once_with()
    mock_client.post.assert_awaited_once_with("/hoge", json={})


def test_hoge_api_async_3(mocker: MockerFixture):
    mock_response = DummyResponse(200, {"message": "ok"})
    mock_post_json_async = mocker.patch(
        "hogelib.api_async.post_json_async",
        new=AsyncMock(return_value=mock_response),
    )

    result = asyncio.run(hoge_api_async_3())

    assert result is mock_response
    assert result.status_code == 200
    assert result.json() == {"message": "ok"}
    mock_post_json_async.assert_awaited_once_with("/hoge", {})
