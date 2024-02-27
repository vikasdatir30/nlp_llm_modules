import tomli
import os


def get_config(config_file_path):
    if os.path.isfile(config_file_path):
        with open(config_file_path, mode='rb') as fptr:
            return tomli.load(fptr)
    else:
        return Exception('Config File not found')
