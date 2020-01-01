from src.interpreter import commands

command_list = []


def initialize(main_window_inst):
    global command_list

    commands.initialize(main_window_inst)

    command_list = commands.get_commands()
    print(command_list)


def print_command_list():
    print(command_list)


def manufacture(text):
    tokens = text.lower().strip().split()
    command = tokens.pop(0)
    return interpret(command, tokens)


def interpret(command_called, arguments):
    for command in command_list:
        # If the given command name is equal to a command present in the command_list
        if command_called == command.get_name():
            return command.run(arguments)

    return "Unknown command, type help for a list of available commands"
