from cloud_queue.aws.queue_manager import QueueManager as AWSQueueManager
from cloud_queue.azure.queue_manager import QueueManager as AzureQueueManager
from cloud_queue.interfaces.queue_manager import IQueueManager

class QueueFactory:

    def __new__(cls, cloud_provider: str, url: str = None, token: str = None) -> IQueueManager:
        if cloud_provider == 'AWS': return AWSQueueManager(url, token)
        elif cloud_provider == 'Azure': return AzureQueueManager(url, token)
