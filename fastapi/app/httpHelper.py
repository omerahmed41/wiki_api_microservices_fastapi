import httpx
from app.parser import parser

URL = "https://en.wikipedia.org/w/api.php"


async def get_value_with_http(title: str = ''):
    async with httpx.AsyncClient() as client:
        params = {
            'action': 'query',
            'prop': 'revisions',
            'titles': title,
            'rvlimit': 1,
            'formatversion': 2,
            'format': "json",
            'rvprop': "content",
        }
        response = await client.get(URL, params=params)

        return parser(response.text)
