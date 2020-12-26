from typing import List
from abc import ABC, abstractmethod

class IQueue(ABC):

    @property
    @abstractmethod
    def messages(self) -> List[str]:
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def push(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, num_messages = 1) -> None:
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError
