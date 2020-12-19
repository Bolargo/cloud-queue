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
        self.queue_service = None

    def delete(self, name: str) -> None:
        if not self.queue_service: self.__connect()

        self.queue_service.delete_queue(name)

    def get(self, name: str) -> IQueue:
        if not self.queue_service: self.__connect()

        return Queue(
            queue=self.queue_service.get_queue_client(name)
        )

    def list_queues_name(self) -> List[str]:
        if not self.queue_service: self.__connect()

        return [
            queue['name'] for queue in self.queue_service.list_queues()
        ]

    def put(self, name: str) -> None:
        if not self.queue_service: self.__connect()

        return Queue(
            queue=self.queue_service.create_queue(name)
        )

    def __connect(self) -> None:
        if self.url and self.token:
            self.queue_service = QueueServiceClient(
                account_url=self.url, credential=self.token
            )
        else:
            raise Exception('Credentials are not set when conneting in Azure Queue Manager')