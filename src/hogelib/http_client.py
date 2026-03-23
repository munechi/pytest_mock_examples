import httpx


def post_json(path: str, payload: dict) -> httpx.Response:
    with httpx.Client() as client:
        response = client.post(path, json=payload)
        return response


async def post_json_async(path: str, payload: dict) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        response = await client.post(path, json=payload)
        return response
