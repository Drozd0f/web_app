from aiohttp import web

from config import BASE_DIR
from src import handlers

routes = [
    web.get(path='/', handler=handlers.reg),
    web.post(path='/', handler=handlers.reg),
    web.get(path='/users', handler=handlers.users_list),
    web.get(path='/ping', handler=handlers.ping),
    web.static('/static', BASE_DIR / 'src/static')
]
