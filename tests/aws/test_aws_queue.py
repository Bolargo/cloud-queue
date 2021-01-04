from cloud_queue.aws.queue import Queue
from cloud_queue.aws.queue_manager import QueueManager
import pytest
import os
import uuid
import time


class TestQueue:

    def setup_method(self):
        self.queue_name = str(uuid.uuid4())
        self.queue_manager = QueueManager(
            os.environ['AWS_URL'], os.environ['AWS_TOKEN']
        )

        try:
            self.queue = self.queue_manager.put(self.queue_name)
        except Exception:
            self.queue = self.queue_manager.get(self.queue_name)

    def teardown_method(self):
        self.queue.clear()

        assert len(self.queue) == 0

        self.queue_manager.delete(self.queue_name)

    def test_if_queue_name_is_the_same_as_the_name_is_passed_when_creating_queue_by_queue_manager(self):
        assert self.queue.name == self.queue_name

    def test_if_num_of_msgs_returned_by_len_is_1_when_a_msg_is_inserted_in_batch_mode(self):
        self.queue.messages = ['dummy message content']

        self.queue.push()

        assert len(self.queue) == 1

    def test_if_num_of_msgs_returned_by_len_is_1_when_a_msg_is_inserted_sequentially(self):
        self.queue.messages = ['dummy message content', 'another dummy message']

        self.queue.push(False)

        assert len(self.queue) == 2

    def test_if_more_than_10_msgs_can_be_pushed_in_batch_mode(self):
        new_messages = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        self.queue.messages = new_messages

        self.queue.push()

        assert len(self.queue) == len(new_messages)

    def test_if_getting_only_one_msg_is_possible(self):
        self.queue.messages = ['1', '2', '3']

        self.queue.push()
        self.queue.get()

        assert len(self.queue.messages) == 1

    def test_if_getting_multiple_msgs_is_possible(self):
        new_messages, num_msg_to_retrieve = ['1', '2', '3'], 2
        self.queue.messages = new_messages

        self.queue.push()
        self.queue.get(num_msgs=num_msg_to_retrieve)

        assert len(self.queue.messages) == num_msg_to_retrieve

    def test_if_getting_more_than_10_msgs_is_possible(self):
        num_msgs = 12
        self.queue.messages = [
            str(i) for i in range(num_msgs)
        ]

        self.queue.push()
        time.sleep(1)
        self.queue.get(num_msgs=num_msgs)

        assert len(self.queue.messages) == num_msgs
