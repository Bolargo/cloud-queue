from src.aws.queue_manager import QueueManager
import uuid
import pytest

def test_if_a_queue_can_be_created_got_and_deleted(self):
    queue_manager = QueueManager()
    queue_name = str(uuid.uuid4())

    queue_manager.put(queue_name)

    queues_name = queue_manager.list_queues_name()

    assert queues_name = [queue_name]

    queue_created = queue_manager.get(queue_name)

    assert queue_created.name == queue_name

    queue_manager.delete(queue_name)

    assert queue_manager.list_queues_name() == []
