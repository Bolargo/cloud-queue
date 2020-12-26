from cloud_queue.interfaces.queue import IQueue
from typing import List

class Queue(IQueue):

    def __init__(self, queue):
        self.__queue = queue
        self.__messages = []

    @property
    def name(self) -> str:
        return self.__queue.queue_name

    @property
    def messages(self) -> List[str]:
        return self.__messages

    @messages.setter
    def messages(self, messages: List[str]) -> None:
        self.__messages = messages

    def push(self) -> None:
        for msg in self.__messages:
            self.__queue.send_message(msg)

        self.__messages = []

    def get(self, num_msgs: int = 1) -> None:
        msgs = self.__queue.receive_messages(messages_per_page=num_messages)

        new_pages = msgs.by_page().next()
        self.__messages.append(new_pages)

        for msg in new_pages:
            self.__queue.delete_message(msg)

    def clear(self) -> None:
        self.__queue.clear_messages()

    def __len__(self) -> int:
        return self.__queue.get_queue_properties().approximate_message_count