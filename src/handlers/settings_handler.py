import os

from src import widget_manager


def initialize():
    settings = widget_manager.main_window.settings
    set_pypandoc_path(settings)


def set_pypandoc_path(settings):
    pandoc_path = settings.value("flavors/pandoc_path", None, type=str)
    print("Given pandoc folder path: " + pandoc_path)

    if pandoc_path is not None:
        os.environ.setdefault('PYPANDOC_PANDOC', os.path.join(os.path.normpath(pandoc_path), 'pandoc'))
