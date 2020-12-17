from src.interfaces.queue_manager import IQueueManager
from src.interfaces.queue import IQueue
from .queue import Queue
from typing import List
import boto3

class QueueManager(IQueueManager):
    @property
    def client(self):
        return boto3.client('sqs')

    def delete(self, name: str) -> None:
        self.client.delete_queue(
            QueueUrl=self.__get_queue_url(name)['QueueUrl']
        )

    def get(self, name:str) -> IQueue:
        return Queue(
            self.__get_queue_url(name)
        )

    def list_queues_name(self) -> List[str]:
        queues = self.client.list_queues()

        return [
            url.split('/')[-1] for url in queues['QueueUrls']
        ]

    def put(self, name: str) -> None:
        aws_queue = self.client.create_queue(
            QueueName=name
        )

        return Queue(aws_queue['QueueUrl'])

    def __get_queue_url(self, name: str):
        return self.client.get_queue_url(
            QueueName=name
        )