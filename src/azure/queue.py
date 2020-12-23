from src.interfaces.queue import IQueue

class Queue(IQueue):

    def __init__(self, queue):
        self.__queue = queue
        self.messages = []

    @property
    def name(self) -> str:
        return self.__queue.queue_name

    def push(self) -> None:
        for msg in self.messages:
            self.__queue.send_message(msg)

        self.messages = []

    def get(self, num_msgs: int = 1) -> None:
        msgs = self.__queue.receive_messages(messages_per_page=num_messages)

        new_pages = msgs.by_page().next()
        self.messages.append(new_pages)

        for msg in new_pages:
            self.__queue.delete_message(msg)

    def clear(self) -> None:
        self.__queue.clear_messages()

    def __len__(self) -> int:
        return self.__queue.get_queue_properties().approximate_message_count