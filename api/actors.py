import sqlite3
from basehandler import BaseHandler
from response import ActorsResponse

class ActorsHandler(BaseHandler):
    def get(self, id = None):
        cur = sqlite3.connect('movies.db').cursor()
        cur.execute("SELECT * FROM actors")
        actors = cur.fetchall()
        actors_list = [
            ActorsResponse(id=row[0], name=row[1], birth_year=row[2]) for row in actors
        ]
        self.write({"objects": actors_list})