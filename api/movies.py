import sqlite3
from basehandler import BaseHandler
from response import MoviesResponse
class MoviesHandler(BaseHandler):
    def get(self):
        cur = sqlite3.connect('movies.db').cursor()
        cur.execute("SELECT * FROM movies")
        movies = cur.fetchall()
        movies_list = [MoviesResponse(id=row[0], title=row[1], release_year=row[2]) for row in movies]
        self.write({"objects": movies_list})