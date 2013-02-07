import imp
import os
import os.path

APP_DIR = '.easy-todo/'
CONFIG_FILE = 'settings.py'
APP_PATH = os.path.join(os.getenv("HOME"), APP_DIR)


def getConfig():
    __maybeCreateAppDirectory(APP_PATH)

    config_file = os.path.join(APP_PATH, CONFIG_FILE)
    try:
        settings = imp.load_source('settings', config_file)
        return getattr(settings, 'config', {})
    except IOError:
        return {}


def __maybeCreateAppDirectory(path):
    if not os.path.isdir(path):
        os.mkdir(path)
