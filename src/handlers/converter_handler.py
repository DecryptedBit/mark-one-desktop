import importlib
import pkgutil

from src import converters
from src.converters import base_converter

converter_dictionary = {}


def initialize():
    global converter_dictionary

    # Import all converters
    package = converters
    for importer, converter_module, is_package in pkgutil.walk_packages(
            path=package.__path__, prefix=package.__name__ + '.', onerror=lambda x: None):
        try:
            module_source = importlib.import_module(converter_module)
            print(f'Found converter module: {converter_module}')
        except Exception as e:
            print(f'Something went wrong in {converter_module} - {e}')

    converter_dictionary = {converter.get_name(): converter for converter in base_converter.BaseConverter.__subclasses__()}


def get_converter(converter_name):
    return converter_dictionary[converter_name]
