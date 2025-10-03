import sqlite3
from basehandler import BaseHandler
from response import DirectorsResponse

class DirectorsHandler(BaseHandler):
    def get(self):
        cur = sqlite3.connect('movies.db').cursor()
        cur.execute("SELECT * FROM directors")
        directors = cur.fetchall()
        directors_list = [DirectorsResponse(id=row[0], name=row[1], birth_year=row[2]) for row in directors]
        self.write({"objects": directors_list})