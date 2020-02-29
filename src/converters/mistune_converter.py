from abc import abstractmethod

import mistune

from src.converters.base_converter import BaseConverter


class MistuneConverter(BaseConverter):
    @staticmethod
    def get_name():
        return "Mistune"

    @staticmethod
    def get_from_types():
        return [("Markdown", "Markdown")]

    @staticmethod
    def get_to_types():
        return [("HTML", "HTML")]

    def __init__(self, from_type_index, to_type_index):
        self.set_from_type(from_type_index)
        self.set_to_type(to_type_index)

    def convert(self, content):
        markdown_parser = mistune.Markdown()
        converted_content = markdown_parser(content)
        return converted_content

    def set_from_type(self, from_type_index):
        self.from_type = self.get_from_types()[from_type_index]

    def get_from_type(self):
        return self.from_type

    def set_to_type(self, to_type_index):
        self.to_type = self.get_to_types()[to_type_index]

    def get_to_type(self):
        return self.to_type
