from domain.parser import parser

from infrastructure.http_client import make_http_call

URL = "https://en.wikipedia.org/w/api.php"


async def get_value_with_http(title: str = ''):
    params = {
        'action': 'query',
        'prop': 'revisions',
        'titles': title,
        'rvlimit': 1,
        'formatversion': 2,
        'format': "json",
        'rvprop': "content",
    }
    return parser(await make_http_call(URL, params))



