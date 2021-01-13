import asyncio

from tornado.websocket import websocket_connect


async def main():
    conn = await websocket_connect("ws://127.0.0.1:8888/heartbeat")
    while True:
        await conn.write_message("ok")
        msg = await conn.read_message()
        if msg is None:
            break
        print(msg)

        break
        # Do something with msg


asyncio.run(main())
