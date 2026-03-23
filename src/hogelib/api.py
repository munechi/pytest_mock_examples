import httpx

from .http_client import post_json


def hoge_api_1():
    with httpx.Client() as client:
        response = client.post("/hoge", json={})
        return response


def hoge_api_2():
    response = httpx.Client().post("/hoge", json={})
    return response


def hoge_api_3():
    response = post_json("/hoge", {})
    return response
