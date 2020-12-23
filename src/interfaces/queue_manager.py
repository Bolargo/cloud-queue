from src.interfaces.queue import IQueue
from typing import List
from abc import ABC, abstractmethod

class IQueueManager(ABC):

    @property
    @abstractmethod
    def client(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self, name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, name: str) -> IQueue:
        raise NotImplementedError

    @abstractmethod
    def list_queues_name(self) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def put(self, name: str) -> None:
        raise NotImplementedError
