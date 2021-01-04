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

    def push(self, msgs: List[str] = None, batch: bool = True) -> None:
        if batch: self.__send_in_batchs(msgs)
        else: self.__send_sequentially(msgs)

        if not msgs: self.__messages = []

    def get(self, num_msgs: int = 1, remove_msgs: bool = True) -> None:
        for i in range(num_msgs):
            new_msgs = self.__client.receive_message(
                QueueUrl=self.url
            )['Messages']
            self.__messages += [
                msg['Body'] for msg in new_msgs
            ]

            if remove_msgs:
                self.__client.delete_message_batch(
                    QueueUrl=self.url,
                    Entries=[
                        { 'Id': msg['MessageId'], 'ReceiptHandle': msg['ReceiptHandle'] } for msg in new_msgs
                    ]
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

    def __send_sequentially(self, msgs: List[str] = None):
        msgs = self.messages if not msgs else msgs

        for msg in msgs:
            self.__resource.send_message(
                MessageBody=msg
            )

    def __send_in_batchs(self, msgs: List[str] = None):
        msgs = self.messages if not msgs else msgs
        num_max_of_msgs_each_batch = 10
        batchs = [
            msgs[i: i + num_max_of_msgs_each_batch] for i in range(0, len(self.__messages), num_max_of_msgs_each_batch)
        ]

        for batch in batchs:
            msgs = [
                { 'Id': str(uuid.uuid4()), 'MessageBody': msg } for msg in batch
            ]

            self.__resource.send_messages(Entries=msgs)