from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import json

class CORSHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "http://localhost:5173")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
    
    def options(self):
        self.set_status(204)
        self.finish()

    def get(self):
        self.write({"status": "ok"})
        self.finish()

app = Application([(r"/", CORSHandler)])
app.listen(8888)
print("✅ Listening on http://localhost:8888")
IOLoop.current().start()