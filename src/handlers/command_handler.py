import importlib
import pkgutil

from src import commands
from src.commands import base_command

command_list = {}
incorrect_command_syntax_notice = "Syntax of this command is incorrect, consider the following help:\n" \
                                + "------------------------------------------------\n"


def initialize():
    global command_list

    # Import all command modules
    package = commands
    for importer, command_module, is_package in pkgutil.walk_packages(
            path=package.__path__, prefix=package.__name__ + '.', onerror=lambda x: None):
        try:
            importlib.import_module(command_module)
            print(f'Found command module: {command_module}')
        except Exception as e:
            print(f'Something went wrong in {command_module} - {e}')

    command_list = {command.get_name(): command for command in base_command.BaseCommand.__subclasses__()}


def manufacture(text):
    tokens = text.lower().strip().split()
    command = tokens.pop(0)
    return interpret(command, tokens)


def interpret(command_called, arguments):
    for command_name, command in command_list.items():
        # If the given command name is equal to a command present in the command_list
        if command_called == command_name:
            return command.run(arguments)

    return "Unknown command, type help for a list of available commands"


def get_linked_commands(master_command):
    return {command.get_name(): command for command in master_command.__subclasses__()}


def create_master_command_documentation(master_command, command_documentation, linked_commands=None):
    if linked_commands is None:
        linked_commands = get_linked_commands(master_command)

    documentation = f'{master_command.get_name()}\t{command_documentation}:'

    if linked_commands:
        for command in linked_commands.values():
            documentation += f'\n- {command.get_documentation()}'

    else:
        documentation += f'\n- No commands are linked to this master command yet.'

    return documentation
