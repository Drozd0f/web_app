import aiohttp_jinja2
from aiohttp import web, hdrs

from src import db


async def ping(request: web.Request) -> web.Response:
    return web.json_response({'msg': 'pong'})


async def reg_user(request: web.Request):
    pool = request.app['pool']
    data = await request.post()
    user = await db.get_user(pool, data)
    print(data)
    if user is None:
        await db.create_user(pool, data)
        return f'Привіт {data["name"]} {data["last_name"]}'
    return f'Вже бачилися {user.name} {user.lastname}'


async def get_users_list(request: web.Request, page: int) -> int:
    pool = request.app['pool']
    return await db.get_users_list(pool, page - 1)


async def get_pages(request: web.Request, current_page: int) -> tuple:
    pool = request.app['pool']
    total_page = await db.get_total_page(pool)
    if total_page > 5:
        pages = []
        left_side, right_side = current_page - 2, current_page + 2
        for page in range(left_side, right_side + 1):
            if page > total_page:
                left_side -= 1
                pages.append(left_side)
            elif page <= 0:
                right_side += 1
                pages.append(right_side)
            else:
                pages.append(page)
        pages.sort()
        return pages, total_page
    return [page + 1 for page in range(total_page)], total_page


@aiohttp_jinja2.template('reg.jinja2')
async def reg(request: web.Request):
    popup_text = ''

    if request.method == hdrs.METH_POST:
        popup_text = await reg_user(request)

    return {
        'popup_text': popup_text
    }


@aiohttp_jinja2.template('users_list.jinja2')
async def users_list(request: web.Request):
    current_page = int(request.query.get('page', '1'))

    users = await get_users_list(request, current_page)
    pages, total_page = await get_pages(request, current_page)
    return {
        'users': users,
        'paginator': {
            'current_page': current_page,
            'pages': pages,
            'total_pages': total_page
        },
    }
