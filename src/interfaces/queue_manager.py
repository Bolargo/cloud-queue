from src.interfaces.queue import IQueue
from typing import List
import abc

class IQueueManager(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def delete(self, name: str) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, name: str) -> IQueue:
        raise NotImplementedError

    @abc.abstractmethod
    def list_queues_name(self) -> List[str]:
        raise NotImplementedError

    @abc.abstractmethod
    def put(self, name: str) -> None:
        raise NotImplementedError
