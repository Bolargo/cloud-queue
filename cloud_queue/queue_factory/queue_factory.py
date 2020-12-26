from cloud_queue.aws.queue_manager import QueueManager as AWSQueueManager
from cloud_queue.azure.queue_manager import QueueManager as AzureQueueManager
from cloud_queue.interfaces.queue_manager import IQueueManager

class QueueFactory:

    def __new__(cls, cloud_provider: str, url: str = None, token: str = None, queue_name: str = None) -> IQueueManager:
        queue_manager = None

        if cloud_provider == 'AWS': queue_manager = AWSQueueManager(url, token)
        elif cloud_provider == 'Azure': queue_manager = AzureQueueManager(url, token)

        return queue_manager.get(queue_name) if queue_name else queue_manager