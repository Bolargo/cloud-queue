from src.azure.queue import Queue
from src.azure.queue_manager import QueueManager
from azure.core.exceptions import ResourceExistsError
import pytest
import os
import uuid

class TestQueue:

    @classmethod
    def setup_class(cls):
        cls.queue_name = str(uuid.uuid4())
        cls.queue_manager = QueueManager(
            os.environ['AZURE_URL'], os.environ['AZURE_TOKEN']
        )

        try:
            cls.queue = cls.queue_manager.put(cls.queue_name)
        except ResourceExistsError:
            cls.queue = cls.queue_manager.get(cls.queue_name)

    @classmethod
    def teardown_class(cls):
        cls.queue.clear()

        assert len(cls.queue) == 0

        cls.queue_manager.delete(cls.queue_name)

    def test_if_queue_name_is_the_same_as_the_name_is_passed_when_creating_queue_by_queue_manager(self):
        assert self.queue.name == self.queue_name

    def test_if_num_of_msgs_returned_by_len_is_1_when_a_msg_is_inserted(self):
        new_messages = ['dummy message content']
        self.queue.messages = new_messages
        num_msgs_before_push = len(self.queue)

        self.queue.push()

        assert len(self.queue) == len(new_messages) + num_msgs_before_push
