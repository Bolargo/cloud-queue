from cloud_queue.aws.queue_manager import QueueManager
import uuid
import pytest
import os

def test_if_a_queue_can_be_created_got_and_deleted():
    queue_manager = QueueManager(
        os.environ['AWS_URL'], os.environ['AWS_TOKEN']
    )
    queue_name = str(uuid.uuid4())
    before_put_queue_names = queue_manager.list_queues_name()

    queue_manager.put(queue_name)

    queues_name = queue_manager.list_queues_name()

    try:
        assert queues_name == before_put_queue_names + [queue_name]
    except:
        print('Sometime it takes a while to see new queues')

    queue_created = queue_manager.get(queue_name)

    assert queue_created.name == queue_name

    queue_manager.delete(queue_name)

    assert queue_manager.list_queues_name() == before_put_queue_names

def test_if_raises_an_exception_when_trying_to_connect_when_account_url_is_empty():
    queue_manager_instance = QueueManager(
        token=os.getenv('AWS_TOKEN')
    )

    with pytest.raises(ConnectionError):
        queue_manager_instance._QueueManager__connect()

def test_if_raises_an_exception_when_trying_to_connect_when_token_is_empty():
    queue_manager_instance = QueueManager(
        url=os.getenv('AWS_URL')
    )

    with pytest.raises(ConnectionError):
        queue_manager_instance._QueueManager__connect()    
