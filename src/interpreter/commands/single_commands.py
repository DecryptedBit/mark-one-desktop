from abc import abstractmethod

from src.interpreter import command_helper
from src.interpreter.commands.base_command import BaseCommand


class HelpCommand(BaseCommand):
    @staticmethod
    def get_name():
        return 'help'

    @staticmethod
    def run(args):
        return '\n'.join(command.get_command_documentation() for command in command_helper.command_list.values())

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        return f'{HelpCommand.get_name()}\tShows all commands with documentation'


class ClearCommand(BaseCommand):
    @staticmethod
    def get_name():
        return 'clear'

    @staticmethod
    def run(args):
        command_helper.main_window.terminal_widget.output_edit.clear()
        return ""

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        return f'{ClearCommand.get_name()}\tClear the terminal'


class SayCommand(BaseCommand):
    @staticmethod
    def get_name():
        return 'say'

    @staticmethod
    def run(args):
        return '"' + ' '.join(args) + '"'

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        return f'{SayCommand.get_name()}\tRepeat a sentence'
