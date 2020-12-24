from src.interfaces.queue_manager import IQueueManager
from src.interfaces.queue import IQueue
from .queue import Queue
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

        self.__client.delete_queue(
            QueueUrl=self.__get_queue_url(name)['QueueUrl']
        )

    def get(self, name: str) -> IQueue:
        self.__connect()

        return Queue(
            self.__client, self.__get_queue_url(name)['QueueUrl']
        )

    def list_queues_name(self) -> List[str]:
        self.__connect()
        queues = self.__client.list_queues()

        return [
            url.split('/')[-1] for url in queues['QueueUrls']
        ]

    def put(self, name: str) -> None:
        self.__connect()
        aws_queue = self.__client.create_queue(
            QueueName=name
        )

        return Queue(self.client, aws_queue['QueueUrl'])

    def __connect(self) -> None:
        if not self.__client:
            if self.url and self.token:
                self.__client = boto3.client(
                    'sqs', aws_access_key_id=self.url, aws_secret_access_key=self.token
                )
            else:
                raise ConnectionError('Credentials are not set when conneting to Azure Queue Manager')

    def __get_queue_url(self, name: str):
        return self.__client.get_queue_url(
            QueueName=name
        )