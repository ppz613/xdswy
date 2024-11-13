"""
@Auther : Pei
@Email : zhupeipei@sailvan.com
@File : .py
@Software : Pycharem
"""

import os
import time
from pathlib import Path

from loguru import logger

import yaml

# 项目根路径
root_path = Path.cwd().parent


# 读取yaml文件
def read_conf(config_name):
    with open(file=config_name, mode='r', encoding='UTF-8') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    return cfg


"""
 日志配置
"""
log_path = Path(root_path, "logs")
t = time.strftime("%Y%m%d")
logger.add(f"{log_path}/uitest-{t}.log", rotation="500MB", encoding="utf-8", enqueue=True, retention="10 days")
