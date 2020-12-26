from cloud_queue.queue_factory.queue_factory import QueueFactory
from cloud_queue.aws.queue_manager import QueueManager as AWSQueueManager
from cloud_queue.aws.queue import Queue as AWSQueue
from cloud_queue.azure.queue_manager import QueueManager as AzureQueueManager
from cloud_queue.azure.queue import Queue import AzureQueue
import os
import pytest

class TestQueueFactory:
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
            'Azure', os.environ['AZURE_URL'], os.environ['AZURE_TOKEN'], os.environ['AZURE_QUEUE_NAME']
        )

        assert isinstance(queue_factory, AzureQueue)

    def test_if_giving_AWS_with_queue_name_we_obtain_Queue(self):
        queue_factory = QueueFactory(
            'AWS', os.environ['AWS_URL'], os.environ['AWS_TOKEN'], os.environ['AWS_QUEUE_NAME']
        )

        assert isinstance(queue_factory, AWSQueue)