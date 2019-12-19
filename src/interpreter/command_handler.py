from src.interpreter import commands

command_list = []


def initialize():
    global command_list
    command_list = commands.get_commands()


def print_command_list():
    print(command_list)


def manufacture(text):
    tokens = text.lower().strip().split()
    command = tokens.pop(0)
    return interpret(command, tokens)


def interpret(command, arguments):
    for command_item in command_list:
        if command == command_item[0]:
            if command_item[1].check_valid_arg(arguments) is True:
                return command_item[1].run(arguments)
            else:
                return f'False arguments given for {command}, type help for help'

    return "Unknown command, type help for help"
