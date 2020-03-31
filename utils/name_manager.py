# coding=utf-8
import re

def filter_name(name):
    """
    过滤文件名中的无效字符
    :param name:
    :return:
    """
    return re.sub(r"[\n]", "-", name)
