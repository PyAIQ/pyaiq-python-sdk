from lifecycle import ILifeCycle
from middleware import WebSocketClient


class WebSocketEvent(ILifeCycle):
    def __init__(self, ws_url: str):
        client = WebSocketClient(ws_url)
        super().__init__(client)
