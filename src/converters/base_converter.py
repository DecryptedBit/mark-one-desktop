from abc import ABC, abstractmethod


class BaseConverter(ABC):
    @staticmethod
    @abstractmethod
    def get_name():
        pass

    @staticmethod
    @abstractmethod
    def get_from_types():
        pass

    @staticmethod
    @abstractmethod
    def get_to_types():
        pass

    @abstractmethod
    def convert(self, content):
        pass

    @abstractmethod
    def set_from_type(self, from_type_index):
        pass

    @abstractmethod
    def get_from_type(self):
        pass

    @abstractmethod
    def set_to_type(self, to_type_index):
        pass

    @abstractmethod
    def get_to_type(self):
        pass
