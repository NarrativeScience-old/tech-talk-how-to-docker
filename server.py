"""
Advanced hyper text transport protocol-based application programming
interface
"""
import logging
import os

from aiohttp import web


logging.basicConfig(level=logging.INFO)


async def hello(request):
    return web.Response(text=f"Hello, {os.environ.get('GUEST', 'World')}")


app = web.Application()
app.add_routes([web.get("/", hello)])

web.run_app(app)
