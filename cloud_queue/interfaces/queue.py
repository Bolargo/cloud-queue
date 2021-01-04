from typing import List
from abc import ABC, abstractmethod

class IQueue(ABC):

    @property
    @abstractmethod
    def messages(self) -> List[str]:
        """ Array of strings with messages will be pushed or were got from Queue """
        raise NotImplementedError

    @messages.setter
    @abstractmethod
    def messages(self, messages: List[str]) -> None:
        """ Setter of messages """
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        """ Queue Name """
        raise NotImplementedError

    @abstractmethod
    def push(self, msgs: List[str] = None) -> None:
        """
        Method which will push every message in messages property
        If msgs is set, this method will push every message in the argument but not in messages property
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, num_messages: int = 1, remove_msgs: bool = True) -> None:
        """
        Get <num_messages> from the queue and removes that msgs

        :Args:
         - num_messages: Number of messages will be got from the queue
         - remove_msgs: If True, it will remove that messages from the queue
        """
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        """
        Clear all the messages from the queue
        """
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the number of messages in that queue
        """
        raise NotImplementedError
