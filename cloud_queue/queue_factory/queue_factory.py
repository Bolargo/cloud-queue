from cloud_queue.aws.queue_manager import QueueManager as AWSQueueManager
from cloud_queue.azure.queue_manager import QueueManager as AzureQueueManager
from cloud_queue.interfaces.queue_manager import IQueueManager

class QueueFactory:

    def __new__(cls, cloud_provider: str, url: str = None, token: str = None, queue_name: str = None) -> IQueueManager:
        """
        Factory to create a QueueManager or Queue from AWS (boto3) or Azure

        :Args:
         - cloud_provider: Only AWS and Azure are allowed (if not it will return None)
         - url: Url or token to access to the account
         - token: Token to access to the account
         - queue_name: If set it will return a Queue object, but a QueueManager will be returned
        """
        queue_manager = None

        if cloud_provider == 'AWS': queue_manager = AWSQueueManager(url, token)
        elif cloud_provider == 'Azure': queue_manager = AzureQueueManager(url, token)

        return queue_manager.get(queue_name) if queue_name else queue_manager