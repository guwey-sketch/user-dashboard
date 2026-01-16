import os
import json
from pathlib import Path

class FileUtils:
    @staticmethod
    def get_config_file_path():
        return os.path.join(Path.home(), '.user-dashboard/config.json')

    @staticmethod
    def load_config_file():
        try:
            with open(FileUtils.get_config_file_path(), 'r') as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    @staticmethod
    def save_config_file(config):
        with open(FileUtils.get_config_file_path(), 'w') as config_file:
            json.dump(config, config_file, indent=4)

    @staticmethod
    def get_data_file_path():
        return os.path.join(os.path.dirname(__file__), 'data.json')

    @staticmethod
    def load_data_file():
        try:
            with open(FileUtils.get_data_file_path(), 'r') as data_file:
                return json.load(data_file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}