from lifecycle import ILifeCycle
from middleware import RESTClient


class RESTEvent(ILifeCycle):
    def __init__(self, base_url: str):
        client = RESTClient(base_url)
        super().__init__(client)
