from fastapi.responses import JSONResponse

from domain.autocomplet_service import add_new_suggestions, get_suggestions
from infrastructure.setting import my_fastapi_app

from domain.info_service import get_short_description


@my_fastapi_app.get('/search')
async def search(title: str = 'Yoshua_Bengio'):
    return await get_short_description(title)


@my_fastapi_app.get('/add')
async def add_to_dict(name: str = ''):
    add_new_suggestions(name)
    return f"Added: {name}"


@my_fastapi_app.get('/suggestions')
async def get_suggestions_api(prefix):
    return JSONResponse(get_suggestions(prefix))


def main():
    print("app is ready")
