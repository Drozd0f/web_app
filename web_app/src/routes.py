from aiohttp import web
from src import handlers

routes = [
    web.get(path='/ping', handler=handlers.ping),
    web.get(path='/', handler=handlers.main_page)
]
