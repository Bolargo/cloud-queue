from cloud_queue.queue_factory.queue_factory import QueueFactory
from cloud_queue.aws.queue_manager import QueueManager as AWSQueueManager
from cloud_queue.aws.queue import Queue as AWSQueue
from cloud_queue.azure.queue_manager import QueueManager as AzureQueueManager
from cloud_queue.azure.queue import Queue as AzureQueue
from uuid import uuid4
import os
import pytest

class TestQueueFactory:

    @classmethod
    def setup_class(cls):
        cls.queue_name = str(uuid4())
        cls.azure_queue_factory = QueueFactory(
            'Azure', os.environ['AZURE_URL'], os.environ['AZURE_TOKEN']
        )
        cls.azure_queue_factory.put(cls.queue_name)
        cls.aws_queue_factory = QueueFactory(
            'AWS', os.environ['AWS_URL'], os.environ['AWS_TOKEN']
        )
        cls.aws_queue_factory.put(cls.queue_name)

    @classmethod
    def teardown_class(cls):
        cls.azure_queue_factory.delete(cls.queue_name)
        cls.aws_queue_factory.delete(cls.queue_name)

    def test_if_giving_AWS_we_obtain_an_AWSQueueManager(self):
        queue_factory = QueueFactory('AWS')

        assert isinstance(queue_factory, AWSQueueManager)

    def test_if_giving_Azure_we_obtain_an_AzureQueueManager(self):
        queue_factory = QueueFactory('Azure')

        assert isinstance(queue_factory, AzureQueueManager)

    def test_if_return_None_when_no_AWS_nor_Azure_is_giving(self):
        queue_factory = QueueFactory('Dummy')

        assert queue_factory is None

    def test_if_giving_Azure_with_queue_name_we_obtain_Queue(self):
        queue_factory = QueueFactory(
            'Azure', os.environ['AZURE_URL'], os.environ['AZURE_TOKEN'], self.queue_name
        )

        assert isinstance(queue_factory, AzureQueue)

    def test_if_giving_AWS_with_queue_name_we_obtain_Queue(self):
        queue_factory = QueueFactory(
            'AWS', os.environ['AWS_URL'], os.environ['AWS_TOKEN'], self.queue_name
        )

        assert isinstance(queue_factory, AWSQueue)