from src.azure.queue import Queue
from src.azure.queue_manager import QueueManager
from azure.core.exceptions import ResourceExistsError
import pytest
import os

class TestQueue:

    @classmethod
    def setup_class(cls):
        self.queue_name = 'dummyqueue1234'
        queue_manager = QueueManager(
            os.environ['URL'], os.environ['TOKEN']
        )

        try:
            self.queue = queue_manager.put(queue_name)
        except ResourceExistsError:
            self.queue = queue_manager.get(queue_name)

    @classmethod
    def teardown_class(cls):
        self.queue.clear()

        assert len(self.queue) == 0

    def test_if_queue_name_is_the_same_as_the_name_is_passed_when_creating_queue_by_queue_manager(self):
        assert self.queue.name == self.queue_name

    def test_if_num_of_msgs_returned_by_len_is_1_when_a_msg_is_inserted(self):
        new_messages = ['dummy message content']
        self.queue.messages = new_messages
        num_msgs_before_push = len(self.queue)

        self.queue.push()

        assert len(self.queue) == len(new_messages) + num_msgs_before_push
        
    def test_if_num_of_msgs_returned_by_len_is_1_when_a_msg_is_inserted_sequentially(self):
        new_messages = ['dummy message content', 'another dummy message']
        self.queue.messages = new_messages
        num_msgs_before_push = len(self.queue)

        self.queue.push(False)

        assert len(self.queue) == len(new_messages) + num_msgs_before_push
