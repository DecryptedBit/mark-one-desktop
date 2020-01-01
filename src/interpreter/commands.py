from abc import ABC, abstractmethod, ABCMeta

from src import file_handler


main_window = None


def initialize(main_window_inst):
    global main_window
    main_window = main_window_inst


def get_commands():
    return [command for command in BaseCommand.__subclasses__()]


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
    def get_linked_commands():
        pass

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        pass


class HelpCommand(BaseCommand):
    @staticmethod
    def get_name():
        return 'help'

    @staticmethod
    def run(args):
        return '\n'.join(command.get_command_documentation() for command in get_commands())

    @staticmethod
    def get_linked_commands():
        return None

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
        main_window.terminal_widget.output_edit.clear()
        return ""

    @staticmethod
    def get_linked_commands():
        return None

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
    def get_linked_commands():
        return None

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        return f'{SayCommand.get_name()}\tRepeat a sentence'


class CreateCommand(BaseCommand):
    @staticmethod
    @abstractmethod
    def get_name():
        return 'create'

    @staticmethod
    @abstractmethod
    def run(args):
        linked_commands = CreateCommand.get_linked_commands()

        if args:
            return linked_commands[args[0]].run(args[1:])
        else:
            return "Syntax of this command is incorrect, consider the following help:\n" + \
                   "------------------------------------------------\n" + \
                   CreateCommand.get_command_documentation()

    @staticmethod
    @abstractmethod
    def get_linked_commands():
        return {command.get_name(): command for command in CreateCommand.__subclasses__()}

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        documentation = f'{CreateCommand.get_name()}\tCreate any of the following:'
        documentation += f'\n- ' + "".join(command.get_command_documentation() for command in CreateCommand.get_linked_commands().values())
        return documentation


class CreateFileCommand(CreateCommand):
    @staticmethod
    def get_name():
        return 'file'

    @staticmethod
    def run(args):
        file_handler.create_file()
        return "Created a file called 'New file'."

    @staticmethod
    def get_linked_commands():
        return None

    @staticmethod
    @abstractmethod
    def get_command_documentation():
        return f'{CreateFileCommand.get_name()}\tCreate a new file.'
