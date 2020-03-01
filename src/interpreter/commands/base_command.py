from abc import ABC, abstractmethod


class BaseCommand(ABC):
    @staticmethod
    @abstractmethod
    def get_name():
        pass

    @staticmethod
    @abstractmethod
    def run(args):
        pass

    @staticmethod
    @abstractmethod
    def get_documentation():
        pass
