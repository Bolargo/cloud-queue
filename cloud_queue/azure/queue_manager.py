from src.interfaces.queue_manager import IQueueManager
from src.interfaces.queue import IQueue
from .queue import Queue
from azure.storage.queue import QueueClient, QueueServiceClient
from typing import List
import boto3

class QueueManager(IQueueManager):

    def __init__(self, url: str = None, token: str = None):
        self.url = url
        self.token = token
        self.__client = None

    @property
    def client(self):
        return self.__client

    def delete(self, name: str) -> None:
        self.__connect()

        self.__client.delete_queue(name)

    def get(self, name: str) -> IQueue:
        self.__connect()

        return Queue(
            queue=self.__client.get_queue_client(name)
        )

    def list_queues_name(self) -> List[str]:
        self.__connect()

        return [
            queue['name'] for queue in self.__client.list_queues()
        ]

    def put(self, name: str) -> None:
        self.__connect()

        return Queue(
            queue=self.client.create_queue(name)
        )

    def __connect(self) -> None:
        if not self.__client:
            if self.url and self.token:
                self.__client = QueueServiceClient(
                    account_url=self.url, credential=self.token
                )
            else:
                raise ConnectionError('Credentials are not set when conneting to Azure Queue Manager')