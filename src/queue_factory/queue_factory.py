from src.aws.queue_manager import QueueManager as AWSQueueManager
from src.azure.queue_manager import QueueManager as AzureQueueManager
from src.interfaces.queue_manager import IQueueManager

class QueueFactory:

    @classmethod
    def create_cloud_factory(cls, cloud_provider: str, url = None: str, token = None: str) -> IQueueManager:
        if cloud_provider == 'AWS': return AWSQueueManager()
        elif cloud_provider == 'Azure': return AzureQueueManager(url, token)
