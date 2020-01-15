from abc import abstractmethod

from src import file_handler
from src.interpreter import command_helper
from src.interpreter.commands.base_command import BaseCommand


class FileCommand(BaseCommand):
    @staticmethod
    @abstractmethod
    def get_name():
        return 'file'

    @staticmethod
    @abstractmethod
    def run(args):
        linked_commands = command_helper.get_linked_commands(FileCommand)

        if args:
            return linked_commands[args[0]].run(args[1:])
        else:
            return command_helper.incorrect_command_syntax_notice + FileCommand.get_command_documentation(linked_commands)

    @staticmethod
    @abstractmethod
    def get_command_documentation(linked_commands=None):
        return command_helper.create_master_command_documentation(FileCommand, "Do any of the following file actions", linked_commands)


class FileCreateCommand(FileCommand):
    @staticmethod
    def get_name():
        return 'create'

    @staticmethod
    def run(args):
        file_handler.create_file()
        return "Created a file called 'New file'."

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        return f'{FileCreateCommand.get_name()}\tCreate a new file.'


class FileOpenCommand(FileCommand):
    @staticmethod
    def get_name():
        return 'open'

    @staticmethod
    def run(args):
        file_info = file_handler.open_file()
        return f'Opened a file called \'{file_info[0]}\' at {file_info[1]} with type {file_info[2]}.'

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        return f'{FileOpenCommand.get_name()}\tOpen a file.'


class FileSaveCommand(FileCommand):
    @staticmethod
    def get_name():
        return 'save'

    @staticmethod
    def run(args):
        instance_info = file_handler.save_file()

        if instance_info is None:
            return f'This action is not available at the moment'

        file_info = instance_info[1]
        return f'Saved a file with id {instance_info[0]} called \'{file_info[0]}\' at {file_info[1]} with type {file_info[2]}.'

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        return f'{FileSaveCommand.get_name()}\tSave a file.'


class FileSaveAsCommand(FileCommand):
    @staticmethod
    def get_name():
        return 'save_as'

    @staticmethod
    def run(args):
        instance_info = file_handler.save_file_as()

        if instance_info is None:
            return f'This action is not available at the moment'

        file_info = instance_info[1]
        return f'Saved a file with id {instance_info[0]} called \'{file_info[0]}\' at {file_info[1]} with type {file_info[2]}.'

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        return f'{FileSaveAsCommand.get_name()}\tSave a file as.'
