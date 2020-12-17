from src.interfaces.queue import IQueue
import uuid
import boto3

class Queue(IQueue):
    def __init__(self, url = None):
        self.url = url
        self.messages = []

    @property
    def name(self) -> str:
        return self.url.split('/')[-1]

    def push(self, batch = True) -> None:
        if batch: self.__send_in_batchs()
        else: self.__send_sequentially()

        self.messages = []

    def get(self, num_mgs = 1) -> None:
        new_msgs = self.__client.receive_message(
            QueueUrl=self.url
        )
        self.messages.append(new_msgs)

        self.__client.delete_message_batch(
            QueueUrl=self.url,
            Entries=self.messages
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
    def __client(self):
        return boto3.client('sqs')

    @property
    def __resource(self):
        return boto3.resource('sqs').Queue(self.url)

    def __send_sequentially(self):
        for msg in self.messages:
            self.__resource.send_message(
                MessageBody=msg
            )

    def __send_in_batchs(self):
        msgs = [
            { 'Id': str(uuid.uuid4()), 'MessageBody': msg } for msg in self.messages
        ]

        self.__resource.send_messages(Entries=msgs)