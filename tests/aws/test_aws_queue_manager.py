from cloud_queue.aws.queue_manager import QueueManager
from uuid import uuid4
import time
import pytest
import os

class TestAWSQueueManager:

    @pytest.fixture
    def queue_manager(self) -> QueueManager:
        return QueueManager(
            os.environ['AWS_URL'], os.environ['AWS_TOKEN']
        )

    @pytest.fixture
    def create_queue(self, queue_manager: QueueManager):
        queue_name = str(uuid4())
        queue_manager.put(queue_name)

        yield queue_name

        queue_manager.delete(queue_name)

    def test_if_a_queue_can_be_created_and_deleted(self, queue_manager: QueueManager):
        queue_name = str(uuid4())
        before_put_queue_names = queue_manager.list_queues_name()

        queue_manager.put(queue_name)

        time.sleep(10) # Sometime it takes a while to see new queues

        queues_name = queue_manager.list_queues_name()
        queue_manager.delete(queue_name)

        print(f'Queues name: {queues_name}')
        print(f'Before put queue names: {before_put_queue_names}')
        print(f'Queue name: {queue_name}')

        assert queues_name == before_put_queue_names + [queue_name]

    def test_if_a_queue_can_be_got(self, queue_manager: QueueManager, create_queue: str):
        queue_created = queue_manager.get(create_queue)

        assert queue_created.name == create_queue

    def test_if_a_queue_can_be_deleted(self, queue_manager: QueueManager):
        before_put_queue_names = queue_manager.list_queues_name()
        queue_name = str(uuid4())
        queue_manager.put(queue_name)
        queue_manager.delete(queue_name)

        assert queue_manager.list_queues_name() == before_put_queue_names

    def test_if_raises_an_exception_when_trying_to_connect_when_account_url_is_empty(self):
        queue_manager_instance = QueueManager(
            token=os.getenv('AWS_TOKEN')
        )

        with pytest.raises(ConnectionError):
            queue_manager_instance._QueueManager__connect()

    def test_if_raises_an_exception_when_trying_to_connect_when_token_is_empty(self):
        queue_manager_instance = QueueManager(
            url=os.getenv('AWS_URL')
        )

        with pytest.raises(ConnectionError):
            queue_manager_instance._QueueManager__connect()    
