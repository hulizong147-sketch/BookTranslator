from argparse import Namespace

import yaml
from utils.argument_utils import ArgumentUtils


class ProjectConfig:
    """
    统一处理项目的配置   单例模式
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._config = None
        self._args = None

    def initialize(self):
        """
        初始化所有的项目配置
        :return:
        """

        if self._args is None:
            arg_utils = ArgumentUtils()
            self._args = arg_utils.parse_arg()


        if self._config is None:
            with open(self._args.config, "r") as f:
                config = yaml.safe_load(f)

        overridden = {}
        for key, value in vars(self._args).items():
            if key in config and value is not None:
                overridden[key] = value

        config.update(overridden)
        self._config = config

    def __getattr__(self, item):
        if self._config and item in self._config:
            return self._config[item]
        raise AttributeError("项目配置中没有这个属性")


if __name__ == '__main__':
    p1 = ProjectConfig()
    p1.initialize()
