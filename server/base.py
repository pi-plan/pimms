import tornado.web
import tornado.websocket


class BaseHandler(tornado.web.RequestHandler):
    def succ(self, data):
        self.write({"status": 0, "msg": None, "data": data})

    def error(self, status: int, msg: str):
        self.write({"status": status, "msg": msg})


class BaseWebSocket(tornado.websocket.WebSocketHandler):
    pass
