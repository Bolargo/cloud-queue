from cloud_queue.interfaces.queue import IQueue
from typing import List
from abc import ABC, abstractmethod

class IQueueManager(ABC):
    """
    Url and Token attributes does not need to be set when created
    but if is a must to be set before calling to any method.
    If not is set it will raise an exception

    Attributes:
        url (str): Url or Token to access to the account
        token (str): Token to access to the account
    """

    @property
    @abstractmethod
    def client(self):
        """
        Client object with the configuration set from the Cloud Provider
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, name: str) -> None:
        """
        Delete the queue with the name given

        :Args:
         - name: The queue name that will be deleted
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, name: str) -> IQueue:
        """
        Getter to get the queue with the name given

        :Args:
         - name: The queue name that will be got
        """
        raise NotImplementedError

    @abstractmethod
    def list_queues_name(self) -> List[str]:
        """
        Get all the queue names in that Url (Bucket or Blob)
        """
        raise NotImplementedError

    @abstractmethod
    def put(self, name: str) -> None:
        """
        Create a queue with the name given for that Url

        :Args:
         - name: Queue name of the queue will be created
        """
        raise NotImplementedError
