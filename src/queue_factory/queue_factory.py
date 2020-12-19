from src.aws.queue_manager import QueueManager as AWSQueueManager
from src.azure.queue_manager import QueueManager as AzureQueueManager
from src.interfaces.queue_manager import IQueueManager

class QueueFactory:

    def __new__(cls, cloud_provider: str, url: str = None, token: str = None) -> IQueueManager:
        if cloud_provider == 'AWS': return AWSQueueManager()
        elif cloud_provider == 'Azure': return AzureQueueManager(url, token)
