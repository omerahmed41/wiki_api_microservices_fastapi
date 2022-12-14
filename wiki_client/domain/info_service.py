from domain.Exception import DomainException
from domain.httpHelper import get_value_with_http

from infrastructure.redis import redis_client

from domain.autocomplet_service import add_new_suggestions, get_suggestions


async def get_short_description(title: str = ''):
    redis_title = redis_client.get(title)
    if redis_title:
        return redis_title
    try:
        short_description = await get_value_with_http(title)
        redis_client.set(title, short_description)
        add_new_suggestions(title)
        return short_description
    except DomainException as e:
        suggestions = get_suggestions(title)
        return f"can't find data for {title} try search for: {suggestions}, more details {e.detail}"
