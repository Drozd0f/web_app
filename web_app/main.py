import os
import asyncio

import asyncpg
import aiohttp_jinja2
import jinja2
from aiohttp import web

from src.routes import routes
from config import BASE_DIR
from src.db import create_db


def create_app() -> web.Application:
    app = web.Application()
    loop = asyncio.get_event_loop()
    app['pool'] = loop.run_until_complete(asyncpg.create_pool(
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_DATABASE'],
        host=os.environ['DB_HOST']
    ))
    app.add_routes(routes)
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(BASE_DIR / 'src/templates')
    )
    app['static_root_url'] = '/static'
    app.on_startup.append(create_db)
    return app


def main():
    app = create_app()
    web.run_app(host='0.0.0.0', port=8000, app=app)


if __name__ == '__main__':
    main()
