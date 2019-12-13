from abc import ABC, abstractmethod, ABCMeta


def get_commands():
    subclasses = []
    work = [Command]

    while work:
        parent = work.pop()

        for child in parent.__subclasses__():
            # For each child that is a subclass of Command check if it is present in the set yet
            if child not in subclasses:
                subclasses.append((child.get_name(), child))
                work.append(child)

    return subclasses


class Command(ABC):
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def get_name():
        return 'N/A'

    @staticmethod
    @abstractmethod
    def run(args):
        pass


class SayCommand(Command):
    @staticmethod
    def get_name():
        return 'say'

    @staticmethod
    def run(args):
        return '"' + ' '.join(args) + '"'
