import asyncio

from tornado.websocket import websocket_connect


class Client(object):

    async def reg_dts(self):
        self.conn = await websocket_connect(
                "ws://127.0.0.1:8888/instance/dts/")
        await self.conn.write_message("node")
        while True:
            await self.conn.write_message("ok")
            msg = await self.conn.read_message()
            if msg is None:
                break
            print(msg)

asyncio.run(main())
