import json
import websockets

from middleware import ICommunicationClient


class WebSocketClient(ICommunicationClient):
    def __init__(self, ws_url: str):
        self.ws_url = ws_url
        self.websocket = None

    async def connect(self):
        self.websocket = await websockets.connect(self.ws_url)

    async def send_event(self, event: str, data=None):
        if self.websocket is None:
            await self.connect()
        message = json.dumps({"event": event, "data": data})
        await self.websocket.send(message)
        response = await self.websocket.recv()
        return json.loads(response)

    async def close(self):
        if self.websocket:
            await self.websocket.close()
