import sqlite3
from basehandler import BaseHandler
from response import GenresResponse

class GenresHandler(BaseHandler):
    def get(self):
        cur = sqlite3.connect('movies.db').cursor()
        cur.execute("SELECT * FROM genres")
        genres = cur.fetchall()
        genres_list = [GenresResponse(id=row[0], name=row[1]) for row in genres]
        self.write({"objects": genres_list})