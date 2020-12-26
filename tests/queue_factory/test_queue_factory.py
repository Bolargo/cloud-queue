from cloud_queue.queue_factory.queue_factory import QueueFactory
from cloud_queue.aws.queue_manager import QueueManager as AWSQueueManager
from cloud_queue.azure.queue_manager import QueueManager as AzureQueueManager
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