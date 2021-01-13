import json

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.locks


class PiMMS(tornado.web.Application):
    def __init__(self, db):
        self.db = db
        handlers = [
            (r"/", Home),
            (r"/heartbeat", Heartbeat),
            (r"/meta/(\w+)", Meta),
        ]
        super().__init__(handlers)


class Home(tornado.web.RequestHandler):
    async def get(self):
        self.write("Welcome PiMMS.")


class Heartbeat(tornado.websocket.WebSocketHandler):
    async def open(self):
        print("WebSocket opened")

    async def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")


class Meta(tornado.web.RequestHandler):
    async def get(self, path):
        data = json.load(open("./demo.json"))
        has_db = bool(int(self.get_argument("has_db", "0")))
        if path not in data.keys():
            self.set_status(404)
            self.finish()
            return
        self.write({path: data[path]})


async def main():
    app = PiMMS(None)
    app.listen(8888)
    shutdown_event = tornado.locks.Event()
    await shutdown_event.wait()


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
