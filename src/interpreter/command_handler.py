from src.interpreter import command_helper


def initialize(main_window_inst):
    command_helper.initialize(main_window_inst)


def manufacture(text):
    tokens = text.lower().strip().split()
    command = tokens.pop(0)
    return interpret(command, tokens)


def interpret(command_called, arguments):
    for command_name, command in command_helper.command_list.items():
        # If the given command name is equal to a command present in the command_list
        if command_called == command_name:
            return command.run(arguments)

    return "Unknown command, type help for a list of available commands"
