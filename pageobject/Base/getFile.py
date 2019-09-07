import yaml, os


class GetFile:

    def __init__(self):
        pass

    def get_yml_data(self, name):
        """
        读取yaml文件数据
        :param name: 待读取文件名字
        :return: 返回数据
        """
        with open("./Data" + os.sep + name, "r",encoding="utf-8") as f:
            return yaml.safe_load(f)
