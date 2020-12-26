from cloud_queue.azure.queue_manager import QueueManager
from cloud_queue.interfaces.queue import IQueue
import pytest
import os
import uuid

def test_if_a_queue_can_be_created_got_and_deleted():
    queue_manager = QueueManager(
        os.environ['AZURE_URL'], os.environ['AZURE_TOKEN']
    )
    queue_name = str(uuid.uuid4())
    before_put_queue_names = queue_manager.list_queues_name()

    queue_manager.put(queue_name)

    new_queues_name = queue_manager.list_queues_name()

    assert new_queues_name == before_put_queue_names + [queue_name]

    queue_created = queue_manager.get(queue_name)

    assert queue_created.name == queue_name

    queue_manager.delete(queue_name)

    assert queue_manager.list_queues_name() == before_put_queue_names

def test_if_raises_an_exception_when_trying_to_connect_when_account_url_is_empty():
    queue_manager_instance = QueueManager(
        token=os.getenv('AZURE_TOKEN')
    )

    with pytest.raises(ConnectionError):
        queue_manager_instance._QueueManager__connect()

def test_if_raises_an_exception_when_trying_to_connect_when_token_is_empty():
    queue_manager_instance = QueueManager(
        url=os.getenv('AZURE_URL')
    )

    with pytest.raises(ConnectionError):
        queue_manager_instance._QueueManager__connect()
