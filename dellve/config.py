import click
import os
import os.path
import pkg_resources as pr

# Constants and default config values (for internal use only)

APP_NAME = 'dellve'
DEFAULT_APP_DIR = click.get_app_dir(APP_NAME)
DEFAULT_HTTP_PORT = 9999
DEFAULT_BENCHMARKS = pr.iter_entry_points(group='dellve.benchmarks', name=None)
DEFAULT_PID_FILE = os.path.join(DEFAULT_APP_DIR, 'dellve.pid')
DEFAULT_CONFIG_FILE = os.path.join(DEFAULT_APP_DIR, 'config.yaml')


# Private module members (for internal use only)
#
# Note: '__config' is a private storage for configuration values that must be
#       accessed through config.get and config.set functions; please, don't
#       rely on default values defined above, as they may be overwritten by
#       user defined config file or command line options.

__config = {
    'app-dir':      DEFAULT_APP_DIR,
    'http-port':    DEFAULT_HTTP_PORT,
    'benchmarks':   DEFAULT_BENCHMARKS,
    'pid-file':     DEFAULT_PID_FILE
}


def _load_yaml(file):
    """Loads a YAML-encoded configuration file.

    Args:
        file (file): Configuration file object.
    """
    import yaml
    data = yaml.load(file)
    if data:
        __config.update(data)


def _load_json(file):
    """Loads a JSON-encoded configuration file.

    Args:
        file (file): Configuration file object.
    """
    import json
    data = json.load(file)
    if data:
        __config.update(data)


# Public module members


def load(file):
    """Loads a configuration file with JSON (.json) or YAML (.yaml, .yml)
    encoding.

    Args:
        file (file): Configuration file object.

    Raises:
        IOError: IOError is raised if provided file isn't of recognized format.
    """
    if file.name.endswith('.json'):
        _load_json(file)
    elif file.name.endswith(('.yml', '.yaml')):
        _load_yaml(file)
    else:
        raise IOError('Couldn\'t load configuration file: %s' % file.name)


def get(name):
    """Gets value of a configuration parameter.

    Args:
        name (str): Parameter's name.

    Returns:
        object: Parameter's value.
    """
    return __config[name]


def set(name, value):
    """Sets value of a configuration parameter.

    Args:
        name (str): Parameter's name.
        value (object): Parameter's value.
    """
    __config[name] = value
