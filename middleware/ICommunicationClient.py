from abc import ABC, abstractmethod


class ICommunicationClient(ABC):
    @abstractmethod
    async def send_event(self, event: str, data=None):
        pass
