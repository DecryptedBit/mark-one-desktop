from src import widget_manager
from src.handlers import command_handler
from src.commands.base_command import BaseCommand


class FileCommand(BaseCommand):
    @staticmethod
    def get_name():
        return 'file'

    @staticmethod
    def run(args):
        linked_commands = command_handler.get_linked_commands(FileCommand)

        if args and args[0] in linked_commands:
            return linked_commands[args[0]].run(args[1:])

        return command_handler.incorrect_command_syntax_notice + FileCommand.get_documentation(linked_commands)

    @staticmethod
    def get_documentation(linked_commands=None):
        return command_handler.create_master_command_documentation(FileCommand, "Do any of the following file actions", linked_commands)


class FileNewCommand(FileCommand):
    @staticmethod
    def get_name():
        return 'new'

    @staticmethod
    def run(args):
        result = widget_manager.markup_editor_widget.create_new_file()

        if result:
            return f'Created a new file: {result}'
        else:
            return 'Failed trying to create file.'

    @staticmethod
    def get_documentation():
        return f'{FileNewCommand.get_name()}\tCreate a new file.'


class FileOpenCommand(FileCommand):
    @staticmethod
    def get_name():
        return 'open'

    @staticmethod
    def run(args):
        result = widget_manager.markup_editor_widget.open_file()

        if result:
            return f'Opened a file: {result}'
        else:
            return 'Failed trying to open file.'

    @staticmethod
    def get_documentation():
        return f'{FileOpenCommand.get_name()}\tOpen a file.'


class FileSaveCommand(FileCommand):
    @staticmethod
    def get_name():
        return 'save'

    @staticmethod
    def run(args):
        result = widget_manager.markup_editor_widget.save_file()

        if result:
            return f'Saved a file: {result}'
        else:
            return 'Failed trying to save file.'

    @staticmethod
    def get_documentation():
        return f'{FileSaveCommand.get_name()}\tSave a file.'


class FileSaveAsCommand(FileCommand):
    @staticmethod
    def get_name():
        return 'save_as'

    @staticmethod
    def run(args):
        result = widget_manager.markup_editor_widget.save_file_as()

        if result:
            return f'Saved a file as: {result}'
        else:
            return 'Failed trying to save file as.'

    @staticmethod
    def get_documentation():
        return f'{FileSaveAsCommand.get_name()}\tSave a file as.'


class FileCloseCommand(FileCommand):
    @staticmethod
    def get_name():
        return 'close'

    @staticmethod
    def run(args):
        result = widget_manager.markup_editor_widget.close_file()

        if type(result) == str:
            return f'Closed a file: {result}'
        else:
            return 'Failed trying to close file.'

    @staticmethod
    def get_documentation():
        return f'{FileCloseCommand.get_name()}\tClose a file.'
