"""
配置文件
"""
import os
import logging.handlers

# print(__file__)
# print('>>>>>>', os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 工程根目录绝对路径


def config_log():
    """日志模块配置方法"""
    # 初始化日志器
    logger = logging.getLogger()

    # 修改日志输出等级
    logger.setLevel(level=logging.INFO)

    # 初始化处理器
    # 控制台
    sh = logging.StreamHandler()
    # 文件
    th = logging.handlers.TimedRotatingFileHandler(filename=BASE_DIR + '/log/info.log',
                                                   when='S',
                                                   interval=10,
                                                   backupCount='3')

    # 初始化格式器
    fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt=fmt)

    # 添加格式器到处理器
    sh.setFormatter(formatter)
    th.setFormatter(formatter)

    # 添加处理器到日志器
    logger.addHandler(sh)
    logger.addHandler(th)
