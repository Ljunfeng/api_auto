import yaml
import json
from configparser import ConfigParser
from small_FrontalGate.common.logger import logger


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件内容自动转为小写的问题。来源百度
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData():

    def __init__(self):
        pass

    def load_yaml(self, file_path):
        logger.info(f"加载 {file_path} 文件......")
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info(f"读到数据 ==>>  {data} ")
        return data

    def load_json(self, file_path):
        logger.info(f"加载 {file_path} 文件......")
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.info(f"读到数据 ==>>  {data} ")
        return data

    def load_ini(self, file_path):
        logger.info(f"加载 {file_path} 文件......")
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        return data



data = ReadFileData()
