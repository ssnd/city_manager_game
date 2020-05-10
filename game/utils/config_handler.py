import yaml


class ConfigHandler:

    @staticmethod
    def open_config(path):
        with open(path) as f:
            config = yaml.safe_load(f)
        return config
