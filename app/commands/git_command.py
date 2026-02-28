from abc import ABC, abstractmethod

class GitCommand(ABC):
    @abstractmethod
    def validate_args(self, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def process(self, **kwargs):
        raise NotImplementedError("Subclasses must implement this method")