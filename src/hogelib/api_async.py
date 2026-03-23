import httpx

from .http_client import post_json_async


async def hoge_api_async_1():
    async with httpx.AsyncClient() as client:
        response = await client.post("/hoge", json={})
        return response


async def hoge_api_async_2():
    response = await httpx.AsyncClient().post("/hoge", json={})
    return response


async def hoge_api_async_3():
    response = await post_json_async("/hoge", {})
    return response
