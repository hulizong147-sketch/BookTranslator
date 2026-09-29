import json
from enum import Enum, auto
import pandas as pd


class ContentType(Enum):
    TEXT = auto()
    TABLE = auto()
    IMAGE = auto()


class Content:
    """
    书中的文本内容
    """

    def __init__(self, content_type, original, translation=None):
        """
        内容的初始化
        :param content_type: 类型
        :param original: 原文
        :param translation: 翻译之后的
        """
        self.content_type = content_type
        self.original = original
        self.translation = translation
        self.status = False  # 翻译完成的状态

    def set_translation(self, translation, status):
        """
        设置翻译之后的文本 和 翻译状态
        :param translation:
        :param status:
        :return:
        """
        if self.content_type == ContentType.TEXT and status:
            self.translation = translation
            self.status = status

    def get_original_to_string(self):
        return self.original


class TableContent:
    """
    书中的表格内容
    """

    def __init__(self, content_type, original, translation=None):
        """
        内容的初始化
        :param content_type: 类型
        :param original: 原文
        :param translation: 翻译之后的
        """
        self.content_type = content_type
        self.original = pd.DataFrame(original)
        self.translation = translation
        self.status = False  # 翻译完成的状态

    def set_translation(self, translation, status):
        """
        设置翻译之后的文本 和 翻译状态
        :param translation:
        :param status:
        :return:
        """
        if self.content_type == ContentType.TABLE and status:
            text = translation.strip()
            data = json.loads(text)
            self.translation = pd.DataFrame(data)
            self.status = status

    def get_original_to_string(self):
        return json.dumps(self.original.values.tolist(), ensure_ascii=False)