from cloud_queue.interfaces.queue import IQueue
from typing import List
import uuid
import boto3

class Queue(IQueue):

    def __init__(self, client, url = None):
        self.url = url
        self.__messages = []
        self.__client = client

    @property
    def name(self) -> str:
        return self.url.split('/')[-1]

    @property
    def messages(self) -> List[str]:
        return self.__messages

    @messages.setter
    def messages(self, messages: List[str]) -> None:
        self.__messages = messages

    def push(self, batch: bool = True) -> None:
        if batch: self.__send_in_batchs()
        else: self.__send_sequentially()

        self.__messages = []

    def get(self, num_mgs: int = 1) -> None:
        new_msgs = self.__client.receive_message(
            QueueUrl=self.url
        )
        self.__messages.append(new_msgs)

        self.__client.delete_message_batch(
            QueueUrl=self.url,
            Entries=self.__messages
        )

    def clear(self) -> None:
        self.__client.purge_queue(
            QueueUrl=self.url
        )

    def __len__(self) -> int:
        return int(
            self.__resource.attributes['ApproximateNumberOfMessages']
        )

    @property
    def __resource(self):
        return boto3.resource('sqs').Queue(self.url)

    def __send_sequentially(self):
        for msg in self.__messages:
            self.__resource.send_message(
                MessageBody=msg
            )

    def __send_in_batchs(self):
        num_max_of_msgs_each_batch = 10
        batchs = [self.__messages[i: i + num_max_of_msgs_each_batch] for i in range(0, len(self.__messages), num_max_of_msgs_each_batch)]

        for batch in batchs:
            msgs = [
                { 'Id': str(uuid.uuid4()), 'MessageBody': msg } for msg in batch
            ]

            self.__resource.send_messages(Entries=msgs)