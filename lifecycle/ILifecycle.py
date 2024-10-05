from middleware import ICommunicationClient


class ILifeCycle:
    def __init__(self, client: ICommunicationClient):
        self._client = client

    async def on_init(self, data):
        return await self._client.send_event("on_init", data)

    async def on_query(self, query):
        return await self._client.send_event("on_query", {"query": query})

    async def on_close(self, data):
        return await self._client.send_event("on_close")
