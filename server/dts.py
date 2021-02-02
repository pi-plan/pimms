from server.base import BaseWebSocket


class DTS(BaseWebSocket):
    async def open(self):
        self.application.dts_instances.append(self)

    async def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        self.application.dts_instances.remove(self)
