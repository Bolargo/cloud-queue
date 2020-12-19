from src.azure.queue_manager import QueueManager
from src.interfaces.queue import IQueue
import pytest
import os

def test_if_a_queue_can_be_created_got_and_deleted(self):
    queue_manager = QueueManager(
        os.environ['URL'], os.environ['TOKEN']
    )
    queue_name = str(uuid.uuid4())

    queue_manager.put(queue_name)

    queues_name = queue_manager.list_queues_name()

    assert queues_name == [queue_name]

    queue_created = queue_manager.get(queue_name)

    assert queue_created.name == queue_name

    queue_manager.delete(queue_name)

    assert queue_manager.list_queues_name() == []

def test_if_raises_an_exception_when_trying_to_connect_when_account_url_is_empty(self):
    queue_manager = QueueManager(
        token=os.environ['TOKEN']
    )

    with pytest.raises(Exception):
        queue_manager_instance._QueueManager__connect()

def test_if_raises_an_exception_when_trying_to_connect_when_token_is_empty(self, queue_manager_instance):
    queue_manager = QueueManager(
        url=os.environ['URL']
    )

    with pytest.raises(Exception):
        queue_manager_instance._QueueManager__connect()
