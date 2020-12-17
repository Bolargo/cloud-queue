import abc

class IQueue(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def push(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, num_messages = 1) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def clear(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError
