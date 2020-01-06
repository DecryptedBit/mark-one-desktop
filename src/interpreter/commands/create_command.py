from abc import abstractmethod

from src import file_handler
from src.interpreter import command_helper
from src.interpreter.commands.base_command import BaseCommand


class CreateCommand(BaseCommand):
    @staticmethod
    @abstractmethod
    def get_name():
        return 'create'

    @staticmethod
    @abstractmethod
    def run(args):
        linked_commands = command_helper.get_linked_commands(CreateCommand)

        if args:
            return linked_commands[args[0]].run(args[1:])
        else:
            return command_helper.incorrect_command_syntax_notice + CreateCommand.get_command_documentation(linked_commands)

    @staticmethod
    @abstractmethod
    def get_command_documentation(linked_commands=None):
        return command_helper.create_master_command_documentation(CreateCommand, "Create any of the following", linked_commands)


class CreateFileCommand(CreateCommand):
    @staticmethod
    def get_name():
        return 'file'

    @staticmethod
    def run(args):
        file_handler.create_file()
        return "Created a file called 'New file'."

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        return f'{CreateFileCommand.get_name()}\tCreate a new file.'
