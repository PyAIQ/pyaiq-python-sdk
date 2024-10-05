import requests

from middleware import ICommunicationClient


class RESTClient(ICommunicationClient):
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def send_event(self, event: str, data=None):
        url = f"{self.base_url}/{event}"
        if data is None:
            data = {}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
