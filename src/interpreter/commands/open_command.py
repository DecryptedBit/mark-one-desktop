from abc import abstractmethod

from src import file_handler
from src.interpreter import command_helper
from src.interpreter.commands.base_command import BaseCommand


class OpenCommand(BaseCommand):
    @staticmethod
    @abstractmethod
    def get_name():
        return 'open'

    @staticmethod
    @abstractmethod
    def run(args):
        linked_commands = command_helper.get_linked_commands(OpenCommand)

        if args:
            return linked_commands[args[0]].run(args[1:])
        else:
            return command_helper.incorrect_command_syntax_notice + OpenCommand.get_command_documentation(linked_commands)

    @staticmethod
    @abstractmethod
    def get_command_documentation(linked_commands=None):
        return command_helper.create_master_command_documentation(OpenCommand, "Open any of the following", linked_commands)


class OpenFileCommand(OpenCommand):
    @staticmethod
    def get_name():
        return 'file'

    @staticmethod
    def run(args):
        file_info = file_handler.open_file()
        return f'Opened the file called \'{file_info[0]}\' at {file_info[1]} with type {file_info[2]}.'

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        return f'{OpenFileCommand.get_name()}\tOpen a file.'
