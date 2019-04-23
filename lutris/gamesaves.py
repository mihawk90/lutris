"""Module for handling the gamesave location"""
import os
from lutris import settings


def get_gamesave_path():
    """Return the path of the gamesaves setting"""
    gamesave_path = settings.read_setting("gamesave_path")
    if gamesave_path:
        return os.path.expanduser(gamesave_path)


def save_gamesave_path(path):
    """Saves the gamesave path to the settings"""
    settings.write_setting("gamesave_path", path)
