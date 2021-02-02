import tornado.ioloop

from server.main import main


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
