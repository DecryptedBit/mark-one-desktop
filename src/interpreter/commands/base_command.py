from abc import ABC, ABCMeta, abstractmethod


class BaseCommand(ABC):
    __metaclass__ = ABCMeta

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
    def get_command_documentation():
        pass
