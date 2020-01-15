import importlib
import pkgutil

from src.interpreter import commands
from src.interpreter.commands import base_command

main_window = None
command_list = {}
incorrect_command_syntax_notice = "Syntax of this command is incorrect, consider the following help:\n" \
                                + "------------------------------------------------\n"


def initialize(main_window_inst):
    global main_window, command_list
    main_window = main_window_inst

    # Import all command modules
    package = commands
    for importer, command_module, is_package in pkgutil.walk_packages(
            path=package.__path__, prefix=package.__name__ + '.', onerror=lambda x: None):
        try:
            module_source = importlib.import_module(command_module)
            print(f'Found command module: {command_module}')
        except Exception as e:
            print(f'Something went wrong in {command_module} - {e}')

    command_list = {command.get_name(): command for command in base_command.BaseCommand.__subclasses__()}


def get_linked_commands(master_command):
    return {command.get_name(): command for command in master_command.__subclasses__()}


def create_master_command_documentation(master_command, command_documentation, linked_commands=None):
    if linked_commands is None:
        linked_commands = get_linked_commands(master_command)

    documentation = f'{master_command.get_name()}\t{command_documentation}:'

    if linked_commands:
        for command in linked_commands.values():
            documentation += f'\n- {command.get_command_documentation()}'

    else:
        documentation += f'\n- No commands are linked to this master command yet.'

    return documentation
