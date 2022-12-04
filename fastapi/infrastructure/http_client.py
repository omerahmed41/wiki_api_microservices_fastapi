import httpx


async def make_http_call(url, params):
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.text
    