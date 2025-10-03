import asyncio
import tornado
import sqlite3
from actors import ActorsHandler
from basehandler import BaseHandler
from movies import MoviesHandler
from directors import DirectorsHandler
from genres import GenresHandler


def make_app():
    return tornado.web.Application([
        (r"/actors", ActorsHandler),
        (r"/directors", DirectorsHandler),
        (r"/genres", GenresHandler),
        (r"/movies", MoviesHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()

if __name__ == "__main__":
    asyncio.run(main())
