import json
from server.dts import DTS
from server.meta import Meta

import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.locks


class PiMMS(tornado.web.Application):
    def __init__(self):
        self.db = json.load(open("./demo.json"))
        self.dts_instances = []
        self.dal_instances = []
        self.ugw_instances = []
        handlers = [
            (r"/", Home),
            (r"/instance/dts/", DTS),
            (r"/meta/zones/(\d+)/(\d*)", Meta),
        ]
        super().__init__(handlers)


class Home(tornado.web.RequestHandler):
    async def get(self):
        self.write("Welcome PiMMS.")


async def main():
    app = PiMMS()
    app.listen(8888)
    shutdown_event = tornado.locks.Event()
    await shutdown_event.wait()
