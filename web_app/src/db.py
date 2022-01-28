import math
import logging
from dataclasses import dataclass

from aiohttp import web
from asyncpg.pool import Pool

from config import BASE_DIR


log = logging.getLogger(__name__)


@dataclass
class User:
    user_id: int
    name: str
    lastname: str


def get_query(query_name: str) -> str:
    try:
        with open(BASE_DIR / f'queries/{query_name}.sql', 'r') as file:
            return file.read()
    except FileNotFoundError:
        log.error(f'Query {query_name} not found')
        return ''


async def create_db(app: web.Application):
    print('create_db')
    pool: Pool = app['pool']
    async with pool.acquire() as connection:
        await connection.execute(get_query('init'))


async def create_user(pool: Pool, user):
    async with pool.acquire() as con:
        await con.execute(
            get_query('create_user'),
            user['name'], user['last_name']
        )


async def get_users_list(pool: Pool, page: int):
    async with pool.acquire() as con:
        rows = await con.fetch(
            get_query('get_list_users'),
            page
        )
    result = [User(*row) for row in rows]
    return result


async def get_total_page(pool: Pool):
    async with pool.acquire() as con:
        total_page = await con.fetchval(get_query('get_total_page'))
    return math.ceil(total_page / 10)


async def get_user(pool: Pool, user):
    async with pool.acquire() as con:
        user = await con.fetchrow(
            get_query('get_user'),
            user['name'], user['last_name']
        )
    if user is None:
        return None
    return User(*user)
