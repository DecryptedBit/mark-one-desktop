import os

from src import widget_manager


def initialize():
    set_pandoc_path(widget_manager.settings.value("flavors/pandoc_path", None, type=str))


def set_pandoc_path(path):
    print("Given executable path: " + path)

    if path is not None:
        os.environ.setdefault('PYPANDOC_PANDOC', os.path.normpath(path))
